addEventListener("DOMContentLoaded", function () {
    // Get red_header element
    const redHeaderElement = document.querySelector("#red_header");

    function elementAddClass() {
        // Get element an add a class to it
        document.querySelector("header").classList.add("red");
    }
    // add event to the red_header
    redHeaderElement.addEventListener("click", elementAddClass);
});