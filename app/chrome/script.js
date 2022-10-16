async function fetchData() {
    const res=await fetch (" https://limitless-dusk-29263.herokuapp.com/recommend?bookName=1984");
    //const res=await fetch ("https://api.coronavirus.data.gov.uk/v1/data");
    const record=await res.json();
    console.log("Received following response");
    console.log(record.toString());
    document.getElementById("date").innerHTML=record;//.data[0].date;
}
fetchData();