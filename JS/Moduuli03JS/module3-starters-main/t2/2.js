const targetElement = document.getElementById("target");

const firstItem = document.createElement("li");
const secondItem = document.createElement("li");
const thirdItem = document.createElement("li");

firstItem.textContent = "First item";
secondItem.textContent = "Second item";
thirdItem.textContent = "Third item";

secondItem.classList.add("my-item");

targetElement.appendChild(firstItem)
targetElement.appendChild(secondItem)
targetElement.appendChild(thirdItem)