
document.getElementById('csvForm').addEventListener('paste', function (pasteListener) {
    const table = document.getElementById('badgeTable');
    while(table.rows.length > 1){
        table.deleteRow(1);
    }
    const clipboardData = pasteListener.clipboardData || window.clipboardData;
    const pastedText = clipboardData.getData('text/plain');
    const clipboardLines = pastedText.split('\n'); // Split by newline characters

    clipboardLines.forEach(line => {
        let [firstName, lastName, eid, title, agencyName, costCenter, supervisorName] = line.split('\t');
        
        //Formats the Agency Name to proper CCURE standards
        if(agencyName.toUpperCase().includes("INFOSYS")){
            agencyName = "INFOSYS LIMITED";
        }
        else if(agencyName.toUpperCase().includes("ROTH")){
            agencyName = "ROTH STAFFING"
        }
        else if(agencyName.toUpperCase().includes("CONVERGINT")){
            agencyName = "CONVERGINT"
        }
        else if(agencyName.toUpperCase().includes("PACIFIC BUILDING CARE")){
            agencyName = "PACIFIC BUILDING CARE"
        }
        
        //Formats the Cost Center to only display the department
        if(costCenter.includes("-")){
            costCenter = costCenter.substring(costCenter.search("-")+1);
        }
        
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td>${firstName.toUpperCase()}</td>
            <td>${lastName.toUpperCase()}</td>
            <td>${eid.toUpperCase()}</td>
            <td>${title.toUpperCase()}</td>
            <td>${agencyName.toUpperCase()}</td>
            <td>${costCenter.toUpperCase()}</td>
            <td>${supervisorName.toUpperCase()}</td>
        `;

        document.getElementById('badgeTable').appendChild(newRow);

    });
});


function resetTable(tableId,formId) {
    const table = document.getElementById(tableId);
    while(table.rows.length > 1){
        table.deleteRow(1);
    }
    document.getElementById(formId).value = '';
}

function deleteRow(btn){
    var row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
}


