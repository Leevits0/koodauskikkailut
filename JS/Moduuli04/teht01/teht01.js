
document.getElementById("searchform").addEventListener("submit", function(event){
  event.preventDefault()
})
const inputvalue = document.getElementById("query").value;

fetch(`https://api.tvmaze.com/search/shows?q=${inputvalue}`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
})
  .catch(error => {
    console.error("Error ", error);
})

