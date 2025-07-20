// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // API endpoint
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

  // Fetch data from the API
  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json(); // Parse response to JSON
    })
    .then(data => {
      const movies = data.results; // Array of movies
      const list = document.getElementById('list_movies'); // Get the <ul> element

      // Loop through each movie and append to the list
      movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        list.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
});
