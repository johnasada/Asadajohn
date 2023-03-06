// Select the HTML element to manipulate
// const date1 = document.querySelector("#date1");
const date2 = document.querySelector("#date2");
// Try to complete the method with options
try {
  const year = {
    year: "numeric",
  };
  const options = {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
    hour: "numeric",
    minute: "numeric",
  };
  // date1.innerHTML = `<span class="highlight">${new Date().toLocaleDateString(
  //   "en-US",
  //   options
  // )}</span>`;
  date2.innerHTML = ` © ${new Date().toLocaleDateString("en-US", year)}</span>`;
} catch (e) {
  console.log("Error with code or your browser does not support Locale");
}
