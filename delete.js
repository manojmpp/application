

// ... The previous JavaScript code remains the same.

function createDeleteButton(fileName) {
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.addEventListener('click', () => {
       deleteFile(fileName);
    });
    return deleteButton;
   }
   
   function deleteFile(fileName) {
    const listItems = directoryList.getElementsByTagName('li');
    for (let i = 0; i < listItems.length; i++) {
       const listItem = listItems[i];
       if (listItem.textContent.startsWith(fileName)) {
         directoryList.removeChild(listItem);
         break;
       }
    }
   }
   
   // ... In the fileInput.addEventListener('change', ...) section:
   
   listItemContainer.appendChild(createDeleteButton(fileName));