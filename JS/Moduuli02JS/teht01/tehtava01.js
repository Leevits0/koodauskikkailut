function numerotReverse () {
   const numerot = [];
    console.log("Numbers in normal order ")
    for (let i = 0; i < 5; i++) {
        const numero = prompt("Give a number");
        numerot.push(Number(numero))

        console.log(numerot[i])
    }
   console.log("Numbers in reverse order ")
    for (let i = numerot.length - 1; i >= 0; i--){
        console.log(numerot[i])
    }
}

console.log(numerotReverse())
