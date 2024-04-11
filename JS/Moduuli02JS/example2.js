// JS mod 2 - taulukot

const names = [];
names [0] = "Aku";
names [1] = "Iines";

console.log(names[2])

//Taulukon loppuun lisääminen
names.push("Hannu");
console.log(names)

//Taulukon viimeisen arvon poistaminen
const lastName = names.pop();
console.log(names);
console.log(lastName);
names.unshift("Minni");


const ages = [4, 55, 36];
console.log(ages,length)

for (let i = 0; i < ages.length; i++) {
  console.log(ages[i], names[i]);
}
//Tulostetaan viimeisestä ensimmäiseen

for (let i = ages.length - 1; i >= 0; i--) {
  console.log(ages[i], names[i]);
}

for (const name of names ) {
  console.log("Nimi: " + name);
}

ages.reverse()
console.log(ages)

// Arvon etsiminen taulukosta

const searchParam = "Aku";
if (names.indexOf(searchParam)){
  console.log(searchParam + " löytyi");
  //Katsotaan missä kohtaa taulukko löydetty alkion arvo on
  console.log(names.indexOf(searchParam))
} else {
  console.log(searchParam + " ei löytynyt.")
}

// Taulukon järjestäminen aakkosjärjestykseen
ages.sort();
console.log(ages);

const person1 = {
  age : 76,
  name: "Roope",
};
const person2 = {
  name: "Aku",
  age: 55,
}
person2.lastName = "Ankka"
person2.name = "Donald";
console.log(person1,person2)
delete person2.lastName;
console.log(person1,person2)


//Sijoitetaan olito taulukkoon:
const persons = [person1, person2];
persons.push({name: names[0], age:ages[0]});
console.log(persons)


//Viittaaminen ominaisuuksiin joko person.name tai person["name"]

for (const person of persons) {
  console.log(`"Nimi: " ${person.name}, ${person['age']} v.`);
}