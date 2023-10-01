# Flask API - Random Compliment Generator

## Overview

The Flask API - Random Compliment Generator is a simple web service built with Flask that provides random compliments when requested. It's a fun and lighthearted API that can be integrated into various applications to spread positivity.

## Features

- Generates random compliments.
- Provides a RESTful API endpoint to retrieve compliments.
- Easy to use and integrate into applications.

## Installation

1. **Clone the Repository:**  
   Clone this repository to your local machine:


2. **Install Dependencies:**  
Navigate to the project directory and install the required dependencies:


## Usage

1. **Run the Flask Application:**  
Start the Flask application to run the API:


The API will run by default on `http://localhost:5000`.

2. **Access the API:**  
To retrieve a random compliment, make a GET request to the following endpoint:

The API will respond with a JSON object containing the compliment.

Example Response:
```json
{
    "compliment": "You're amazing! Keep up the great work."
}

