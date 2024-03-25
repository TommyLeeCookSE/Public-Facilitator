from bs4 import BeautifulSoup
import sqlite3, os
from datetime import datetime
from flask import request
from werkzeug.utils import secure_filename
from pathlib import Path

def process(filename):
    cards = []   #Loads all the cards from DB into this file..
    cards_dict = {}     #Create a dict to store all the card objects for easier comparison
    matching_cards = []
    non_matching_cards = []

    class Card:
        def __init__(self, card_id, card_number, date_last_activated, expiration,last_used_by_eid, last_used_by, last_used_date):
            self.card_id = card_id
            self.card_number = card_number
            self.date_created = date_last_activated
            self.last_used_by_eid = last_used_by_eid
            self.expiration = expiration
            self.last_used_by = last_used_by
            self.last_used_date = last_used_date

    conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db') #Connected to daypass db
    connCursor = conn.cursor()
    connCursor.execute("SELECT * FROM daypasses")
    rows = connCursor.fetchall()
    
    for row in rows: #Makes objects from daypass db
        card = Card(row[0], row[1], row[2], row[3],row[4],row[5],row[6])
        cards.append(card)
    cards.sort(key=lambda card: card.card_id)     #Sort the cards from their ID

    for card in cards: #Add card objects to dict with cardID as the key
        cards_dict[card.card_id] = card

    with open(filename, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'xml') 
    credentials = soup.find_all('SoftwareHouse.NextGen.Common.SecurityObjects.Credential')

    
    for card in credentials:
        card_id = int(card.find('CardNumber').text)
        expiration_date = card.find('ExpirationDateTime').text
        
        if card_id in cards_dict:
            cards_dict[card_id].expiration = expiration_date
            matching_cards.append(cards_dict[card_id])
        else:
            new_card = Card(card_id, None, None, expiration_date, None, None,None)
            non_matching_cards.append(new_card)
                
    for object in matching_cards:   #Reupdate the database with the newly updated card dates and close connection
        object.date_last_activated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        object.expiration = expiration_date
        connCursor.execute("UPDATE daypasses SET date_last_activated = ? WHERE card_id = ?", (object.date_last_activated, object.card_id))
        connCursor.execute("UPDATE daypasses SET expiration = ? WHERE card_id = ?", (object.expiration, object.card_id))

    conn.commit()
    conn.close()

    #Remove file
    if len(non_matching_cards) == 0:
        os.remove(filename)
    return matching_cards, non_matching_cards


def processNonMatching(data):
    conn = sqlite3.connect(r'C:\Users\Tommy_Cook\OneDrive - Edwards Lifesciences\Documents\Scripts\Facilitator\WebPages\facilities.db')
    connCursor = conn.cursor()
    connCursor.execute("SELECT * FROM daypasses")

    for cardID,cardNumber in data.items():
        connCursor.execute("INSERT INTO daypasses (card_ID, card_Number) VALUES (?,?)", (cardID, cardNumber))
        conn.commit()
    connCursor.execute("DELETE FROM daypasses WHERE card_number = ''")

    conn.close()

    
