//teht 5

const year = parseInt(prompt("Anna vuosiluku"));
let vuosiluku;

if (year % 4 === 0) {
  if (year % 100 !== 0 || year % 400 === 0) {
    vuosiluku = " on karkausvuosi";
  } else {
    vuosiluku = " ei ole karkausvuosi";
  }
} else {
  vuosiluku = " ei ole karkausvuosi";
}
const karkausvuosi = document.querySelectorAll("p");
karkausvuosi[0].textContent = "Vuosi: " + year + vuosiluku;

