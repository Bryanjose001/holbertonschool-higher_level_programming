document.addEventListener('DOMContentLoaded', () => {
  const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  // Select the element with id 'fetch_character'
  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json(); // Parse JSON from response
    })
    .then(data => {
// Update the element with id 'character' with the name from the API
      document.getElementById('character').textContent = data.name;
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
});
