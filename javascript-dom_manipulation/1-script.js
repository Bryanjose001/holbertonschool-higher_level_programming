/*
This script listens for a click event on an element with the ID 'red_header'
*/

// Wait for the DOM to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function () {
  const redHeader = document.getElementById('red_header');
  redHeader.addEventListener('click', function () {
    document.querySelector('header').style.color = '#FF0000';
  });
});