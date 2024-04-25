const targetElement = document.getElementById("target");

const lista = `
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
`;

targetElement.innerHTML = lista;
targetElement.classList.add("my-list")