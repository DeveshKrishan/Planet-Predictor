# NASA API Documentation
# https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf

import requests
import time

class NasaScraper:
    def __init__(self) -> None:
        self.request_count = 0
    def search_nasa_image_database(self, planet):
        '''Searches for an image using NASA Image and Video Library API to grab links for each image.'''
        url = f"https://images-api.nasa.gov/search?q={planet}&media_type=image"
        # https://api.nasa.gov/?ref=swiftbeta
        if self.request_count >= 950:  # below limit
            time.sleep(3600) 
            self.request_count = 0  
        response = requests.get(url)
        if (response.status_code == 200):
            data = response.json()
        for i, item in enumerate(data['collection']['items'][:5]): # limit to 5 pages
            image_url = item['links'][0]['href']
            print(image_url)
        self.request_count += 1


if __name__ == '__main__':
    nasa_scaper = NasaScraper()
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    for planet in planets:
        nasa_scaper.search_nasa_image_database(planet)
