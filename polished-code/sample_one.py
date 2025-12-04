import time
import requests
from typing import List, Dict, Any, Optional

def getUsers(url: str, active: bool = True) -> Optional[List[Dict[str, Any]]]:
    """
    Fetches users from the provided URL and filters them based on active status.

    Args:
        url: The API endpoint to fetch users from.
        active: If True, only returns users marked as active.

    Returns:
        A list of user dictionaries if successful, or None if an error occurs.
    """
    try:
        # Added timeout to prevent the application from hanging indefinitely
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            try:
                data = response.json()
            except ValueError:
                print("Error: Failed to decode JSON response")
                return None

            if not isinstance(data, list):
                print("Error: Unexpected API response format (expected list)")
                return None

            users = []
            for user in data:
                # If filtering is enabled, strictly check for active status.
                # Otherwise, include all users.
                if active:
                    # Using .get() avoids KeyError if 'active' is missing.
                    # Comparing == True preserves original behavior (e.g. 1 == True).
                    if user.get("active") == True:
                        users.append(user)
                else:
                    users.append(user)

            for user in users:
                # Safely access 'name' to prevent crashes on malformed data
                print(f"User: {user.get('name', 'Unknown')}")
            
            return users
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Error: Network request failed: {e}")
        return None

def main():
    print("starting..")
    # Note: The URL is hardcoded as per the original script
    users = getUsers("https://example.com/api/users", True)
    
    # Preserving the sleep from the original code
    time.sleep(1)
    print("done!")

if __name__ == "__main__":
    main()