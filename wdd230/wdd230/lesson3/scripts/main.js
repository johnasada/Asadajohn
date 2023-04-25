//Create the lastdate object
let lastdate = new Date(document.lastModified);

//Old way of doing this.
//Create the months so that Jan does not = 0
//const months = [
    //  "1",
    //  "2",
    //  "3",
    //  "4",
    //  "5",
    //  "6",
    //  "7",
    //  "8",
    //  "9",
    //  "10",
    //  "11",
    //  "12"
//];

//Method to create the updatetime object
//const month = months[lastdate.getMonth()];

//New way of doing this.
let month = lastdate.getMonth();
//Add one so that the month is actually the month.
month += 1;

const year = lastdate.getFullYear(); 
const day = lastdate.getDate();

const hour = lastdate.getHours();
const minute = lastdate.getMinutes();
const seconds = lastdate.getSeconds();
const fulltime = `${hour}:${minute}:${seconds}`;

const updatetime = `${month}/${day}/${year} ${fulltime}`;

//Send back to HTML
document.querySelector("#moddate").textContent = updatetime;
