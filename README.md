# pilot_detector

##### This project was made for a company as a pre-assignment in the job application process.

#### The goal
Build and deploy a web application which lists all the pilots, from a given endpoint, who recently violated the NDZ perimeter (were too close to a nest).

What it looks like is up to you, but this list should

    Persist the pilot information for 10 minutes since their drone was last seen by the equipment
    Display the closest confirmed distance to the nest
    Contain the pilot name, email address and phone number
    Immediately show the information from the last 10 minutes to anyone opening the application
    Not require the user to manually refresh the view to see up-to-date information

Develop the application as if it was always operational. 

All the goals were met in this repository.

#### Information
You can see the project here: https://seraphinabot.dev/nomadikuikka/

The backend is running on DigitalOcean's cloud and constatly queries the given endpoint and builds a up-to-date SQL-database from the information.
The database is used by the FastAPI-python script that can be queried here: https://134-122-52-132.sslip.io/ . *Sslip is a DNS-service that can turn any ip-address into a domain.*
The frontend is running on GitHub Pages and redirected to a domain I own.

#### How to Launch Locally
At the root of the folder, run `bash launch.sh`. It should install all the required depencies, run fastapi, run the database-updater and run the website locally.
The main.js is quering the webserver that is running on DigitalOcean though but you can change it to the local fastapi-address in the main.js.
