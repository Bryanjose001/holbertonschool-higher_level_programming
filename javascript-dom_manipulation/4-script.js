addEventListener("DOMContentLoaded", function () {
    addItem = () => {
        const newItem = document.createElement("li");
        newItem.innerText = "Item";
        // Appending new <li> element to <ul> 'my_list'
        document.querySelector(".my_list").append(newItem);
    };

    const addItemElement = document.querySelector("#add_item");
    addItemElement.addEventListener("click", addItem);
});