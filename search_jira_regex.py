import requests
#import getpass

# Replace these with your Jira project details
JIRA_BASE_URL = "https://issues.apache.org/jira/rest/api/2/"
JIRA_PROJECT_KEY = "HIVE"
#def get_jira_credentials():

def search_jira_issues(query_string, use_regex=False):
    headers = {"Content-Type": "application/json"}
    # Construct the JQL (Jira Query Language) to search for bugs containing the query_string
    if use_regex:
        jql = f'project={JIRA_PROJECT_KEY} AND issuetype=Bug AND description ~ "{query_string}" ORDER BY Updated'
    else:
        jql = f'project={JIRA_PROJECT_KEY} AND issuetype=Bug AND text ~ "{query_string}" ORDER BY Updated'
    # Search API endpoint
    url = f"{JIRA_BASE_URL}search"
    # Parameters for the search request
    params = {
        "jql": jql,
        "maxResults": 100  # Adjust this to retrieve more or fewer results
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()["issues"]
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
    return None
def main():
    query_string = input("Enter the string to search for in bug descriptions: ")
    use_regex = input("Use regex search? (y/n): ").lower() == "y"
    bugs = search_jira_issues(query_string, use_regex)
    if bugs:
        print(f"Found {len(bugs)} bugs with matching string:")
        for bug in bugs:
            print(f"{bug['key']}: {bug['fields']['summary']}")
    else:
        print("No bugs found with the given query.")
if __name__ == "__main__":
    main()