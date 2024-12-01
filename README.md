Daily Quotes Fetcher
This project fetches and displays quotes from two free APIs:

Kanye West Quotes API
Programming Quotes API
It demonstrates basic usage of Python's requests module to interact with RESTful APIs.
This project was written as a school exercise to guide us with git, the readme is written in english to help everyone to understand the purpose of this repository.

Features
Fetches a random quote from Kanye West.
Fetches a random programming-related quote.
Handles API connection errors gracefully.

Prerequisites
Ensure the following tools are installed:

Python 3.11+
pip (Python package manager)
Docker (optional, for containerized setup)

Installation

Run Locally

Clone the repository:

git clone https://github.com/LordPrettyMike/ue19-lab-05
cd ue19-lab-05

Install the required Python packages:

pip install -r requirements.txt

Run the script:

python daily_quotes.py

Using Docker

Build the Docker Image
Ensure Docker is installed and running.
Build the Docker image:

docker build -t app.py .

Run the Docker Container
To run the application:

docker run app.py

Stop the Docker Container
If running the container in detached mode (-d flag), stop it using:

docker ps          # Get the container ID
docker stop <container_id>

API Resources
Kanye West Quotes: https://api.kanye.rest
Programming Quotes: https://programming-quotes-api.vercel.app/

Troubleshooting
Ensure Docker is running if using the Docker setup.
Check internet connectivity to ensure access to the APIs.
Use docker logs <container_id> to debug container issues.
