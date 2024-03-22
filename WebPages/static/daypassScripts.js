var submitButton = document.getElementById('processButton');
submitButton.disabled = true;
submitButton.style.backgroundColor = 'red';
submitButton.style.color = "white";
submitButton.value = 'A file must be uploaded';

var fileUpload = document.getElementById('fileUpload')
var allowedExtensions = /(\.xml)$/i;

function checkInputs() {
    var filePath = fileUpload.value;
    if (!filePath){
        submitButton.disabled = true;
        submitButton.style.backgroundColor = 'red';
        submitButton.style.color = "white";
        submitButton.value = 'A file must be uploaded'
    }
    else if(!allowedExtensions.exec(filePath)){
        alert('Please upload.xml file only.');
        fileUpload.value = '';
        return false;
    }
    else if (!fileUpload.value) {
        submitButton.disabled = true;
        submitButton.style.backgroundColor = 'red';
        submitButton.style.color = "white";
        submitButton.value = 'A file must be uploaded'
    }
    else {
        submitButton.disabled = false;
        submitButton.style.backgroundColor = '';
        submitButton.style.color = "";
        submitButton.value = 'Process';
    }
}

fileUpload.onchange = checkInputs;
