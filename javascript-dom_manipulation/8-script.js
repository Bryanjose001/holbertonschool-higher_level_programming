document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    // Fetch the translation from the API
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json(); // Parse the JSON response
    })
    .then(data => {
    // Update the element with id 'hello' with the translated text
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
});
