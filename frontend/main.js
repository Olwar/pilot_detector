// api url
const api_url =
    "http://127.0.0.1:8000/";

// gets all the drone data from the fastapi
async function getapi(url) {
    const response = await fetch(url);
    var data = await response.json();
    console.log(data);
    if (response) {
        hideloader();
    }
    show(data);
}

getapi(api_url);

// Function to hide the loader
function hideloader() {
    document.getElementById('loading').style.display = 'none';
}
// Defining the table for the drone data
function show(data) {
    let tab =  
           `<tr>
                <th>id</th>
                <th>Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>X-coordinate</th>
                <th>Y-coordinate</th>
            </tr>`;
    for (r of data) {
        tab += `
        <table>
            <tr>
                <td>${r[0]}</td>
                <td>${r[1]}</td>
                <td>${r[2]}</td>
                <td>${r[3]}</td>
                <td>${r[4]}</td>
                <td>${r[5]}</td>
            </tr>
        </table>`;
    }
    document.getElementById("drones").innerHTML = tab;
}
