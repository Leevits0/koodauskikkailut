const amount = prompt("How many dice would you like to throw?")
console.log(amount);

let sum = 0;

for (let i = 0; i < amount; i++ ){
    const noppaLuku = (Math.floor(Math.random()*6+1))
    console.log(noppaLuku)
    sum += noppaLuku;
}
console.log("Total sum from dice rolls = " + sum);

const lopputulos = document.querySelector("p");
lopputulos.textContent = "Total sum from dice rolls = " + sum;


