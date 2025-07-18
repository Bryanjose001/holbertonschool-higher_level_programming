addEventListener("DOMContentLoaded", function () {
    // Function to change the color of the header element
    function changeColor() {
        document.querySelector("header").style.color = "#FF0000";
    }

    // Get the div element to which we will apply the event listener
    const divRedHeader = document.querySelector("#red_header");

    // Add the click event listener to the div element
    divRedHeader.addEventListener("click", changeColor);
});