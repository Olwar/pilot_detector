// api url
const api_url = 
      "http://127.0.0.1:8000/";
  
// Defining async function
async function getapi(url) {
    
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
    if (response) {
        hideloader();
    }
    show(data);
}
// Calling that async function
getapi(api_url);
  
// Function to hide the loader
function hideloader() {
    document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
    let tab =
        `<tr>
          <th>Name</th>
          <th>Email</th>
          <th>Phone</th>
          <th>X-coordinate</th>
          <th>Y-coordinate</th>
         </tr>`;
    
    // Loop to access all rows 
    for (r of data) {
    tab += `<tr> 
    <td>${r[0]}</td>
    <td>${r[1]}</td>
    <td>${r[2]}</td> 
    <td>${r[3]}</td>
    <td>${r[4]}</td>   
    </tr>`;
    }
    // Setting innerHTML as tab variable
    document.getElementById("drones").innerHTML = tab;
}