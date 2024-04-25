'use strict';
const names = ['John', 'Paul', 'Jones'];

const targetElement = document.getElementById("target");
for (let i = 0; i < names.length; i++){
    const listItem = document.createElement("li")
    listItem.textContent = names[i];
    targetElement.appendChild(listItem)
}