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
huoneisto[0].textContent = HarryPotter + ", You are " + huone +"!";