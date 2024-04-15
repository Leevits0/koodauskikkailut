// JS MOD 2 - funktiot


//perinteinen funktion määritelmä
function doSomething() {
  console.log("doing something...")
}

doSomething();

const doSomethingMore =  () => {
  console.log("doing something else...")
  return "funktio suoritettu";
}
doSomethingMore();


const ages = [4, 55, 36];

// Vertailufunktio sort()- metodia varten
function compare(val1, val2) {
  return val1-val2;
}
console.log(compare(4, 33));
//ages.sort(compare);

//Vertailu funktio nimettömänä funktiona
ages.sort(function(val1,val2){
  return val1 - val2;
});

// vertailufunctio nuolifunctiona
ages.sort((val1, val2) => val1 -val2);
console.log(ages);

//Tulostaa array:n sisällön ja palauttaa uuden taulukon käännetyssä järjestyksesä
function logArray(array){
 // Funktion sisällä esitelty muuttuja näkyy vain funktion sisällä
 // const ages = [];
  //console.log(ages);
  console.log(array);
  const newArray = array.slice(0);
  newArray.reverse()
  return newArray;
}


const reversedAges = logArray(ages)


console.log("original "+ ages);
console.log("reversed "+ reversedAges);

//matsku esimerkki lottorivien luonnista
function doLottery (numbers, num) {
  const row = [];
  let r;
  for (let i = 0; i < num; i ++) {
    let ok = false;

    while (!ok) {
      ok = true;
      r = Math.floor(Math.random() * numbers) + 1;
      for (let j = 0; j < i + 1; j ++) {
        if (row [j] === r) {
          ok = false;
        }
      }
    }
    row[i] = r;
  }
  return row;
}

const lottery = doLottery(40,7);
for (let i = 0; i < lottery.length; i++) {
    console.log(lottery[i]);
}