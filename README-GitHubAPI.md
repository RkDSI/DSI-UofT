# GitHub Repository Star Visualizer

This Python script uses the GitHub REST API to fetch the top 20 most starred public GitHub repositories and visualizes them in a horizontal bar chart.

## Features

- **GitHub API Integration**: Retrieve real-time data of the most starred repositories.
- **Data Visualization**: Uses `matplotlib` to create a bar chart displaying the repositories and their star counts.

## How It Works

The script performs the following steps:

1. Sends a GET request to the GitHub API's search endpoint.
2. Extracts the repository names and star counts from the response.
3. Plots a horizontal bar chart with the names of the repositories on the y-axis and the number of stars on the x-axis.

## Requirements

To run this script, you'll need:

- Python 3
- `requests` library
- `matplotlib` library

## Usage

To execute the script, simply run `python GitHubAPI.py` in your terminal.

## Visual Output

The resulting plot will display the top 20 most starred GitHub repositories, with the x-axis representing the number of stars and the y-axis representing the repository names.

## Note

The GitHub API has rate limits. For unauthenticated requests, the rate limit allows for up to 60 requests per hour. If you need to make more requests, you should authenticate with a GitHub token.

## Author
Reza Kopaee

