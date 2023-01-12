

const date1 = document.querySelector("#date1");

date1.innerHTML = new Date().getFullYear();


// Getting the last modified date

const date2 = document.querySelector("#date2");

date2.innerHTML = new Date(document.lastModified).toLocaleDateString("en-US");