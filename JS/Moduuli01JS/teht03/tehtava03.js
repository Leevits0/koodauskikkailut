//teht03
const int1 = parseInt(prompt("Anna ensimmäinen kokonaisluku"));
console.log(int1)
const  int2 = parseInt(prompt("Anna toinen kokonaisluku"))
console.log(int2)
const int3 = parseInt(prompt("Anna kolmas kokonaisluku"))
console.log(int3)

const summa = document.querySelectorAll("p");
console.log(summa);
summa[0].textContent = int1 + int2 + int3;

const tulo = document.querySelectorAll("p");
console.log(tulo);
tulo[1].textContent = int1 * int2 * int3;

const keskiarvo = document.querySelectorAll("p");
console.log(keskiarvo);
keskiarvo[2].textContent = (int1 + int2 + int3) / 3;
