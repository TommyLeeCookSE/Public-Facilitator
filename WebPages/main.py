from flask import Flask, render_template, request, jsonify
from scripts import moveAutomator, daypassAutomator, tractionGuest, centerstoneReporterAutomator, centerstoneCsvInput, comparisonDrawer, badgeAutomator
from werkzeug.utils import secure_filename


app = Flask(__name__, template_folder='templates')
app.secret_key = 'tommys_secret_key'
@app.route('/')
def home():
    return render_template('HomePage.html')

@app.route('/badge')
def badgeCaser():
    return render_template('BadgeUpperCaserPage.html')

@app.route('/submit_badge_csv', methods=['POST'])
def submit_badge_csv():
    data = request.form['badgeCsvForm']
    employee_list = badgeAutomator.process(data)
    return render_template('BadgeUpperCaserPage.html', employee_list=employee_list)
    

@app.route('/moves')
def movesAutomator():
    return render_template('MovesAutomator.html')

@app.route('/moveAutomatorSubmit', methods=['POST'])
def moveAutomatorSubmit():
    data = request.form['moveCsvData']  
    result = moveAutomator.process(data)  
    return render_template('MovesAutomator.html', processed_data=result, processed = True)

@app.route('/dayPassAutomator')
def dayPassAutomator():
    return render_template('DayPassAutomator.html')

@app.route('/processDayPass', methods=['POST'])
def processDayPass():
    file = request.files['fileUpload']
    filename = secure_filename(file.filename)
    file.save(filename)

    result = daypassAutomator.process(filename)
    matching_cards, non_matching_cards = result
    return render_template('DayPassAutomator.html', matching=matching_cards, non_matching=non_matching_cards)

@app.route('/processNonMatching', methods=['POST'])
def processNonMatching():
    htmlData = request.form
    daypassAutomator.processNonMatching(htmlData)
    return render_template('DayPassAutomator.html')


@app.route('/dayPassEntry')
def dayPassEntry():
    return render_template('DayPassEntry.html')

@app.route('/tractionGuestUpload', methods=['POST'])
def tractionGuestUpload():
    file = request.files['tractionFileUpload']
    filename = secure_filename(file.filename)
    file.save(filename)

    tractionGuest.tractionGuestUpload(filename)
    return render_template('DayPassEntry.html')

@app.route('/centerstoneReporter')
def centerstoneReporter():
    result = centerstoneReporterAutomator.process()
    return render_template('CenterstoneReporter.html', processedData = result)

    
@app.route('/centerstoneCsvInput.html')
def displayCenterstoneCsvInput():
    return render_template('centerstoneCsvInput.html')

@app.route('/comparisonTool.html')
def displayComparisonTool():
    result = comparisonDrawer.pullFromDatabase()
    result_list=list(result)
    return render_template('ComparisonTool.html', result_list=result_list)

@app.route('/get_comparison_data', methods=['POST'])
def get_comparison_data():
    data = request.get_json()
    date = data['date']
    result_list = comparisonDrawer.pullFromDatabase()
    for item in result_list:
        if item[0] == date:
            return jsonify(item)
        
@app.route('/compareWODates', methods=['POST'])
def compareWODates():
    first_date = request.form.get('dropdown1')
    second_date = request.form.get('dropdown2')
    listOfDates = [first_date,second_date]

    final_list_of_dates = comparisonDrawer.pullAndCompareDates(listOfDates)

    dates = comparisonDrawer.pullFromDatabase()
    result_list=list(dates)

    return render_template('ComparisonTool.html', result_list=result_list,final_list_of_dates=final_list_of_dates)

@app.route('/processCenterstoneCsvInput', methods=['POST'])
def processCenterstoneCsvInput():
    file = request.files['centerstoneFileUpload']
    filename = secure_filename(file.filename)
    file.save(filename)
    centerstoneCsvInput.saveToWorkOrderTable(filename)
    result = centerstoneReporterAutomator.process()
    return render_template('CenterstoneReporter.html', processedData=result)

@app.route('/meetingAutomator')
def meetingAutomator():
    return render_template('MeetingAutomator.html')

if __name__ == '__main__':
    app.run(debug=True)