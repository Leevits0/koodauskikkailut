'use script';
// jos html tiedosto tyhjä niin paina (! + tab)
console.log("I have awaken!")


let name = 'Leevi';
const names = [' Aku',' Iines', ' Heluna'];

let age, height;
age = 5.1;
console.log(age, typeof age, height, typeof height)

// Muutetaan number -> string
age = age.toString();
console.log(age);
// Muutetaan string --> number
//age = "viisi vuotta";
//age = parseInt(age); // ottaa vaan kokonaisosan
age = parseFloat(age);
console.log(age, typeof age);
const ageAdd = 3;

//lisätään arvoon 1
age++
// sama asia
// age = age + 1;
// age += 1;

console.log((age + ageAdd));

console.log(name + "n ikä on " + age + " vuotta. ");
console.log(`${name}n ikä on ${age} vuotta.`);
//$ merkin saa painamalla (option + 4)
// Toimii samalla tavalla kuin pythonin print(f"blaa {ballall}")
// mutta pitää olla `sisällä`


const isUnderAge = true;
console.log(isUnderAge, typeof isUnderAge)


console.log('Moikka ' + name);
console.log('Tulostetaan kaikki nimet',name , names);

//alert('Moi ' + name);
//alert("Toinen alertti");

const firstParagrapghElement = document.querySelector("p");
console.log(firstParagrapghElement);
firstParagrapghElement.textContent = 'Moikka ' + name;

const allParagraphElements = document.querySelectorAll("p");
console.log(allParagraphElements);
allParagraphElements[2].textContent = "kolmas tekstikappale";
allParagraphElements[3].textContent = names;

name = "Aku";
// syötteen suoraan lukeminen JS
// name = prompt("Anna nimi");
// console.log(name, typeof name);

// Math
console.log(Math.random())

//arvotaan arvo väliltä 1-6
console.log(Math.floor(Math.random()*6+1))



//const data = fetch("http://localhost:3000/airports");
///////////////
// const = muuttuja
// let = muuttuja jota muokataan myöhemmin koodissa
// prompt = samankaltainen, kuin pythonin "input"
// console.log = kirjaa koodin nettisivun konsoliin
///////////////

//esimerkki pe tunti iltapäivä
const numerojoku = prompt("Anna numero")
if (numerojoku % 3 === 0){
  console.log("numero "+numerojoku+ " on jaollinen kolmella")
  if(numerojoku % 5 === 0){
    console.log("numero " +numerojoku+ " on jaollinen viidellä")}
    else{
      console.log(numerojoku+ " ei ole jaollinen kolmella ja viidellä")}}


const age = prompt("Anna ikä")


for (let i = 10;  i <= 1; --i){
  console.log(i)
}

for (let i = 0; i<=100; i++) {
  if (i % 7 == 0) {
    console.log(i);
  }
}

for (let i = 0; i<=100; i+=7){
  console.log(i)
}

const lempinumero = parseInt(prompt("Anna lempinumerosi"))
console.log(`Sinun lempinumero on: + ${lempinumero}`)
