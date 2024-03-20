document.getElementById("dropdown1").addEventListener("change", function() {
    var date = this.value;
    fetch('/get_comparison_data', {
        method: 'POST',
        body: JSON.stringify({date: date}),
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => updateTable(data, 0));
});

document.getElementById("dropdown2").addEventListener("change", function() {
    var date = this.value;
    fetch('/get_comparison_data', {
        method: 'POST',
        body: JSON.stringify({date: date}),
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => updateTable(data, 1));
});

function updateTable(data, rowNumber) {
    var table = document.getElementById("comparison-table");
    // Ensure the table has enough rows
    while (table.rows.length <= rowNumber + 1) { // Add 1 to skip the header row
        table.insertRow(-1); // Insert at the end of the table
    }
    // Update the specified row
    var row = table.rows[rowNumber + 1]; // Add 1 to skip the header row

    // Clear existing cells
    while (row.cells.length > 0) {
        row.deleteCell(0);
    }
    // Add new cells
    for (var i = 0; i < data.length; i++) {
        var cell = row.insertCell(i);
        cell.innerHTML = data[i];
    }
}

