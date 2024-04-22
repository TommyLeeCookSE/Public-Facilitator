import sqlite3
import pandas as pd

def update_building_names():
    try:
        # Connect to your SQLite database (replace 'your_database.db' with your actual database file)
        conn = sqlite3.connect(r'WebPages/facilities.db')
        cursor = conn.cursor()

        # Retrieve data from empty_building_table
        cursor.execute("SELECT asset_name, building FROM asset_building_table")
        empty_building_data = cursor.fetchall()

        # Update asset_building_table
        for asset_name, building in empty_building_data:
            cursor.execute("UPDATE empty_building_table SET building = ? WHERE asset_name = ?", (building, asset_name))

        # Commit the changes
        conn.commit()
        print("Building names updated successfully!")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

# Call the function to update building names
# update_building_names()
        
def export_table_to_csv():
    try:
        # Connect to your SQLite database (replace 'your_database.db' with your actual database file)
        conn = sqlite3.connect(r'WebPages/facilities.db')

        # Read data from your table into a pandas DataFrame
        query = "SELECT * FROM empty_building_table"  # Replace 'your_table_name' with the actual table name
        df = pd.read_sql_query(query, conn)

        # Write the DataFrame to a CSV file
        df.to_csv('output.csv', index=False)  # Replace 'output.csv' with your desired output file name

        print("Data exported to 'output.csv' successfully!")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        conn.close()

# Call the function to export the table
export_table_to_csv()