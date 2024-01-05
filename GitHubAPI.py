import requests
import matplotlib.pyplot as plt

# Set up the endpoint and parameters for the GitHub API request to search repositories
search_url = 'https://api.github.com/search/repositories'
search_params = {
    'q': 'stars:>1',  # Find repositories with stars greater than 1
    'sort': 'stars',  # Sort by number of stars
    'order': 'desc',  # Order by descending (most stars first)
    'per_page': 20    # Limit results to top 20
}

# Send a GET request to the GitHub API
response = requests.get(search_url, params=search_params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response into a Python dictionary
    search_results = response.json()
    
    # Initialize lists to hold repository names and star counts
    repo_names = []
    stars = []
    
    # Loop through each item in the search results
    for repo in search_results['items']:
        # Add the repo name and star count to the respective lists
        repo_names.append(repo['name'])
        stars.append(repo['stargazers_count'])

    # Create a horizontal bar chart
    plt.figure(figsize=(12, 8))  # Set the figure size
    plt.barh(repo_names, stars, color='skyblue')  # Create horizontal bars
    plt.xlabel('Stars')  # Set the x-axis label
    plt.ylabel('Repository')  # Set the y-axis label
    plt.title('Top 20 Most Starred GitHub Repositories')  # Set the title
    plt.gca().invert_yaxis()  # Invert the y-axis to show the top repo at the top
    plt.show()  # Display the plot
else:
    print("Failed to fetch data:", response.status_code)
