document.addEventListener('DOMContentLoaded', () => {
  // Select the element with id 'update_header'
  const updateHeader = document.getElementById('update_header');
    // Select the header element
  const headerElement = document.querySelector('header');

  updateHeader.addEventListener('click', () => {
    headerElement.textContent = 'New Header!!!';
  });
});
