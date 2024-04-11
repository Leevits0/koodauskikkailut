'use strict';
//teht01
console.log("I'm printing to console!");

//teht02
name = prompt("Anna nimi:");
const nimi = document.querySelector("p");
console.log(nimi);
nimi.textContent = 'Hello, ' + name + "!";

//teht03
const int1 = parseInt(prompt("Anna ensimmäinen kokonaisluku"));
console.log(int1)
const  int2 = parseInt(prompt("Anna toinen kokonaisluku"))
console.log(int2)
const int3 = parseInt(prompt("Anna kolmas kokonaisluku"))
console.log(int3)

const summa = document.querySelectorAll("p");
console.log(summa);
summa[1].textContent = int1 + int2 + int3;

const tulo = document.querySelectorAll("p");
console.log(tulo);
tulo[2].textContent = int1 * int2 * int3;

const keskiarvo = document.querySelectorAll("p");
console.log(keskiarvo);
keskiarvo[3].textContent = (int1 + int2 + int3) / 3;

//teht4
const HarryPotter = prompt("Kerro nimesi kouluun:");
const number = (Math.floor(Math.random()*4+1));
let huone;

if (number === 1)
  huone = "You are Ravenclaw"
 else
  if (number === 2)
    huone = "Hufflepuff"
   else
    if (number === 3)
      huone = "Slytherin"
     else
      if (number === 4)
        huone = "Gryffindor"
const huoneisto = document.querySelectorAll("p");
console.log(huoneisto);
huoneisto[4].textContent = HarryPotter + ", You are " + huone +"!";
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
karkausvuosi[5].textContent = "Vuosi: " + year + vuosiluku;


// 0 + 2 + 4 + 6 + 8 + 10 + 12 + 14

//for (let i = 10;  i <= 1; --i){
 // console.log(i);
//}










