//funktio osallistujien määrän ja nimien saamiseen
function participantList(){
    const amount = prompt("What is the number of current participants? : ")
    console.log(amount)
    const participants = []
    console.log(participants + " current participant amount = " + amount)
    for (let i = 0; i < amount; i++ ){
        const participantName = prompt("Participant name: ")
        participants.push(participantName)
    }
    console.log(participants.sort())

    //lista näkyviin nettisivulle
    const participantListDiv = document.getElementById("participantList");
    const ol = document.createElement("ol")
    participants.forEach(function(participant) {
        const li = document.createElement(("li"));
        li.textContent = participant
        ol.appendChild(li);
    })
    participantListDiv.appendChild(ol);
}

console.log(participantList())