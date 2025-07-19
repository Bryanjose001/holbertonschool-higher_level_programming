document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      // Get `hello` value from response and put text into element
      const helloValue = data.hello;
      document.getElementById('hello').textContent = helloValue;
    })
  // Catch any errors that occur during the fetch
    .catch((error) => {
      console.error('Error fetching translation:', error);
    });
});
