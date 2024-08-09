from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
from datetime import *
import time

load_dotenv()
notification = NotificationManager()
data = DataManager()
sheet_data = data.get_destination_data()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LHR"

for row in sheet_data:
    if row["iataCode"] == "":
        row['iataCode'] = flight_search.get_destination_code(row['city'])
        time.sleep(2)
print(sheet_data)

data.destination_data = sheet_data
data.update_iata()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: INR {cheapest_flight.price}")
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")

        notification.send_message(
            message_body=f"Low price alert.\nOnly ₹{cheapest_flight.price} to fly from\n{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} on\n{cheapest_flight.out_date} until {cheapest_flight.return_date}.")
