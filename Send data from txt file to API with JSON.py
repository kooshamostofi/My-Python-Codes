#!/usr/bin/env python

import os
import requests
import json  # Import the json module for formatting

# Function to read content from a feedback file and create a dictionary
def read_feedback_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        feedback_dict = {
            "title": lines[0].strip(),
            "name": lines[1].strip(),
            "date": lines[2].strip(),
            "feedback": lines[3].strip()
        }
    return feedback_dict

# Main script
if __name__ == "__main__":
    # Define the directory containing feedback files
    feedback_directory = "/data/feedback"

    # Get a list of all .txt files in the feedback directory
    feedback_files = [file for file in os.listdir(feedback_directory) if file.endswith(".txt")]

    # Iterate over each feedback file
    for feedback_file in feedback_files:
        # Construct the full path to the feedback file
        file_path = os.path.join(feedback_directory, feedback_file)

        # Read content from the feedback file and create a dictionary
        feedback_data = read_feedback_file(file_path)

        # Convert the dictionary to JSON with double quotes
        json_data = json.dumps(feedback_data)

        # Print the JSON data being sent (for debugging purposes)
        print(f"Sending JSON data for {feedback_file}: {json_data}")

        # Make a POST request to the company's website
        api_url = "http://34.42.39.245/feedback/"

        try:
            response = requests.post(api_url, json=feedback_data)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            print(f"Feedback from {feedback_file} successfully uploaded!")
        except requests.exceptions.RequestException as e:
            print(f"Error uploading feedback from {feedback_file}: {e}")
