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

async function load_pic() {
    
    const url = 'http://127.0.0.1:8000/img'

    const options = {
        method: "GET"
    }

    let response = await fetch(url, options)

    if (response.status === 200) {
        
        const imageBlob = await response.blob()
        const imageObjectURL = URL.createObjectURL(imageBlob);

        const image = document.createElement('img')
        image.src = imageObjectURL

        const container = document.getElementById("your-container")
        container.append(image)
    }
    else {
        console.log("HTTP-Error: " + response.status)
    }
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
              <th>id</th>
              <th>Name</th>
              <th>Email</th>
              <th>Phone</th>
              <th>X-coordinate</th>
              <th>Y-coordinate</th>
             </tr>`;
    
    // Loop to access all rows 
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
    // Setting innerHTML as tab variable
    document.getElementById("drones").innerHTML = tab;
}
