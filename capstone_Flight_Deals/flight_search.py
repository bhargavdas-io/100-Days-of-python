import os
import requests
from dotenv import load_dotenv

load_dotenv()
amadeus_token_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
amadeus_get_url = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
amadeus_flight_endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'


class FlightSearch:

    def __init__(self):
        self._api_key = os.environ['AM_API_KEY']
        self._api_secret = os.environ['AM_API_SECRET']
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-type': 'application/x-www-form-urlencoded',
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=amadeus_token_url, headers=header, data=body)
        json = response.json()
        access_token = json['access_token']
        return access_token

    def get_destination_code(self, city_name):
        print(f"Using this token: {self._token}")
        header = {
            'Authorization': f'Bearer {self._token}'
        }
        query = {
            'keyword': city_name,
            'max': '2',
            'include': 'AIRPORTS',

        }

        request = requests.get(url=amadeus_get_url, params=query, headers=header)
        print(f"Status code {request.status_code}. Airport IATA: {request.text}")
        try:
            code = request.json()["included"]["airports"]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "INR",
            "max": "10",
        }

        response = requests.get(
            url=amadeus_flight_endpoint,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
