
const confirmRoot = confirm("Should I calculate square root?")

if (confirmRoot === true){
    const number = prompt("Give the number that you want a square root of: ")
    if (number < 0){
        alert("The square root of a negative number is not defined")
    }
    const sqRoot = Math.sqrt(parseFloat(number))
    const result = document.querySelector("p");
    result.textContent = "Square root of "+ number + " is " + sqRoot;
}
else if (confirmRoot === false){
    alert("Square root is not calculated.")
}
