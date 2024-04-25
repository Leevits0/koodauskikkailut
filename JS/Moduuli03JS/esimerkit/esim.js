function locationSuccess(location){
  console.log("Käyttäjä paikannettu ", location)
}

function locationError(error) {
  console.log("paikannus epäonnistui ", error)
}

const options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
}
//Käytetään tapahtumakäsittelijänä, kun-p näppäintä painetaan
function locateUser(event) {
  console.log("näppäintapahtuma", event)
  if (event.keypress === "p") {
    navigator.geolocation.getCurrentPosition(locationSuccess, locationError, options)
  }
}


const buttonElement = document.querySelector("button");

buttonElement.addEventListener("click", function(event){
  //pysäytetään click-eventin eteneminen dom-puussa tähän
  event.stopPropagation();
  console.log("Button clicked")
})


document.addEventListener("keypress",locateUser)


//Hiiren liikutus
function hiirenLiikutus(MouseEvent){
document.addEventListener("mousemove", (MouseEvent) => {
  console.log(MouseEvent)
  })
}

document.addEventListener("contextmenu", function(event){
  console.log(event);
  event.preventDefault();
  alert("Ähäkutti")
})
// koko dokumentin
document.addEventListener("click", function(event){
  console.log("sivua klikattu" + event);
})