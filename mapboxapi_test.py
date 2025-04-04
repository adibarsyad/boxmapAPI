import requests

def test_endpoint(api_name, url, params):
    """
    Tests a specific Mapbox API endpoint with the provided access token.
    
    :param api_name: Name of the API being tested.
    :param url: Endpoint URL.
    :param params: Dictionary of parameters including the access token.
    """
    try:
        response = requests.get(url, params=params)
        print(f"\nTesting {api_name}...")
        print(f"URL: {response.url}")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"⚠️ {api_name} is VULNERABLE: Accessible from unauthorized hosts.")
        elif response.status_code == 403:
            print(f"✅ {api_name} is SECURE: Access is properly restricted.")
        else:
            print(f"❓ {api_name} returned unexpected status code {response.status_code}.")
    except Exception as e:
        print(f"❌ Error testing {api_name}: {e}")

def check_mapbox_token_security(access_token):
    """
    Checks the security of the provided Mapbox access token across various APIs.
    
    :param access_token: Mapbox access token to be tested.
    """
    # Define Mapbox API endpoints to test
    api_endpoints = {
        "Geocoding API": "https://api.mapbox.com/geocoding/v5/mapbox.places/Paris.json",
        "Directions API": "https://api.mapbox.com/directions/v5/mapbox/driving/-73.9857,40.7484;-73.9680,40.7851",
        "Static Images API": "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/-73.9857,40.7484,14/400x400",
        "Vector Tiles API": "https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/14/4823/6160.vector.pbf",
        "Raster Tiles API": "https://api.mapbox.com/v4/mapbox.satellite/14/4823/6160.jpg",
        "Styles API": "https://api.mapbox.com/styles/v1/mapbox/streets-v11",
        "Tilequery API": "https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/tilequery/-73.9857,40.7484.json",
        "Uploads API": "https://api.mapbox.com/uploads/v1",
        "Datasets API": "https://api.mapbox.com/datasets/v1",
        "Fonts API": "https://api.mapbox.com/fonts/v1/mapbox/Arial Unicode Regular/0-255.pbf",
        "Search Box API": "https://api.mapbox.com/search/searchbox/v1/suggest?q=coffee&language=en&limit=5",
        "Map Matching API": "https://api.mapbox.com/matching/v5/mapbox/driving/-73.9857,40.7484;-73.9680,40.7851",
        "Isochrone API": "https://api.mapbox.com/isochrone/v1/mapbox/driving/-73.9857,40.7484",
        "Matrix API": "https://api.mapbox.com/directions-matrix/v1/mapbox/driving/-73.9857,40.7484;-73.9680,40.7851",
    }

    params = {"access_token": access_token}

    for api_name, url in api_endpoints.items():
        test_endpoint(api_name, url, params)

if __name__ == "__main__":
    token = input("Enter your Mapbox Access Token: ").strip()
    check_mapbox_token_security(token)
