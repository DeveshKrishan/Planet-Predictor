# NASA API Documentation
# https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf

import requests
import time

class NasaScraper:
    def __init__(self) -> None:
        self.request_count = 0
    def search_nasa_image_database(self, planet):
        url = f"https://images-api.nasa.gov/search?q={planet}&media_type=image"
        # https://api.nasa.gov/?ref=swiftbeta
        if self.request_count >= 950:  # below limit
            time.sleep(3600)  # Sleep for one hour
            self.request_count = 0  # Reset the counter after the pause
        response = requests.get(url)
        self.request_count += 1