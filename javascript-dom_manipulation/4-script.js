document.addEventListener('DOMContentLoaded', function () {
    // This script adds a new item to the list when the button is clicked
  const item = document.getElementById('add_item');
  const list = document.querySelector('.my_list');

  item.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';

    list.appendChild(newItem);
  });
});