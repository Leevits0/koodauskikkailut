function DogListReverse(){

    const amount = 6
    console.log(amount)

    const dogs = []
    console.log(dogs + " current participant amount = " + amount)

    for (let i = 0; i < amount; i++ ){
        const dogName = prompt("enter dog's name: ")
        dogs.push(dogName)
    }
    console.log(dogs.sort())
    console.log(dogs.reverse())

    //lista näkyviin nettisivulle
    const DogListReverseDiv = document.getElementById("DogListReverse");
    const ul = document.createElement("ul")
    dogs.forEach(function(dog) {
        const li = document.createElement(("li"));
        li.textContent = dog
        ul.appendChild(li);
    })
    DogListReverseDiv.appendChild(ul);
}

console.log(DogListReverse())