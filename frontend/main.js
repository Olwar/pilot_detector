// api url
const api_url =
    "https://134-122-52-132.sslip.io/";

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

// updates the table without manual refresh
function startLiveUpdate() {
    setInterval(function() {
        getapi(api_url);
    }, 2000);
}

document.addEventListener('DOMContentLoaded', function () {
    startLiveUpdate();
});

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
