const numbers = [];

while (true) {
  const input = parseInt(prompt("Enter a number (enter 0 to stop):"));

  if (isNaN(input)) {
    alert("Invalid input. Please enter a number.");
  } else if (input === 0) {
    break;
  } else {
    numbers.push(input);
  }
}

if (numbers.length > 0) {
  numbers.sort((a, b) => b - a);
  console.log("Numbers entered (from largest to smallest):", numbers);
} else {
  console.log("No numbers were entered.");
}
