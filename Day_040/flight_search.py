import requests
from data_manager import *
import datetime
from flight_data import *
import pprint


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.apikey = os.environ.get("apikey")

    def location(self, term):
        self.tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"
        parameter = {
            "term": term
        }
        header = {
            "apikey": self.apikey
        }
        response = requests.get(self.tequila_endpoint,
                                parameter, headers=header)
        response = response.json()
        code = response["locations"][0]["code"]
        return code

    def search_ticket(self, iata):
        self.tequila_endpoint = "https://api.tequila.kiwi.com/v2/search"
        now = datetime.datetime.now()
        self.now = now.strftime('%d/%m/%Y')
        diff = datetime.timedelta(days=180)
        after = diff + now
        self.after = after.strftime('%d/%m/%Y')

        parameter = {
            "fly_from": "KR",
            "fly_to": iata,
            "date_from": self.now,
            "date_to": self.after,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 7,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "KRW",
        }
        header = {
            "apikey": self.apikey
        }
        response = requests.get(url=self.tequila_endpoint,
                                params=parameter, headers=header)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {parameter['fly_to']}.")
            parameter["max_stopovers"] = 2
            response = requests.get(
                url=self.tequila_endpoint,
                params=parameter,
            )
            try:
                data = response.json()["data"][0]
            except:
                print("nothing else")
                return None
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                step_overs=0,
                via_city=""
            )

            return flight_data
