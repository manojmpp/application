const fileInput = document.getElementById('fileInput');
const directoryList = document.getElementById('directoryList');

fileInput.addEventListener('change', (event) => {
 const file = event.target.files[0];

 const reader = new FileReader();

 reader.onload = function(event) {
    const fileDataURL = event.target.result;

    const fileBlob = dataURLtoBlob(fileDataURL);

    const fileName = file.name;

    const listItem = document.createElement('li');
    listItem.textContent = fileName;

    const listItemContainer = document.createElement('div');
    listItemContainer.appendChild(listItem);

    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(fileBlob);
    downloadLink.download = fileName;
    downloadLink.textContent = 'Download';

    listItemContainer.appendChild(downloadLink);

    directoryList.appendChild(listItemContainer);
 };

 reader.readAsDataURL(file);
});

function dataURLtoBlob(dataURL) {
 // ... The function provided in the original answer.
