import requests

def findCountries(region, keyword):
    url = f"https://jsonmock.hackerrank.com/api/countries/search?region={region}&name={keyword}"
    result = []
    page = 1

    try:
        while True:
            # Make API request
            response = requests.get(f"{url}&page={page}")
            response.raise_for_status()  # Raise an error if the request fails
            data = response.json()
            
            # Debugging: Print the response structure
            if "data" not in data:
                print(f"Error: Unexpected response structure on page {page}: {data}")
                break
            
            # Process data if present
            for country in data["data"]:
                if keyword.lower() in country["name"].lower():
                    result.append((country["name"], country["population"]))

            # Exit loop if no more pages
            if page >= data.get("total_pages", 0):
                break
            page += 1

        # Sort results by population (asc) and name (asc for ties)
        result.sort(key=lambda country: (country[1], country[0]))

        # Format and return output
        return [f"{name},{population}" for name, population in result]
    
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise  # Re-raise the error after logging for debugging
