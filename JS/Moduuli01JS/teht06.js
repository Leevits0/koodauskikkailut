
const confirmRoot = confirm("Should I calculate square root?")

if (confirmRoot === true){
    const number = prompt("Give the number that you want a square root of: ")
    const sqRoot = Math.sqrt(parseFloat(number))
    const result = document.querySelector("p");
    sqRoot[0].textContent = "Squareroot of "+ number + "is " + sqRoot;
}
if (confirmRoot === false){
    alert("Square root is not calculated.")
} else {

}
