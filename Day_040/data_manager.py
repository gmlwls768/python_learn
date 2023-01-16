import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.username = os.environ.get("username")
        self.projectName = "flightDeals"
        self.sheetName = "prices"
        self.sheety_endpoint = f"https://api.sheety.co/{self.username}/{self.projectName}/{self.sheetName}"
        self.user_endpoint = f"https://api.sheety.co/{self.username}/{self.projectName}/users"

    def return_sheet_data(self):
        response = requests.get(self.sheety_endpoint)
        sheet_data = response.json()["prices"]
        return sheet_data

    def put_sheet_data(self, iata, row):
        parameter = {
            "price": {
                "iata": iata
            }
        }
        put_endpoint = f"{self.sheety_endpoint}/{row}"
        response = requests.put(put_endpoint, json=parameter)

    def post_shee_user_data(self, Fname, Lname, email):
        parameter = {
            "user": {
                "firstName": Fname,
                "lastName": Lname,
                "email": email
            }
        }
        response = requests.post(self.post_endpoint, json=parameter)

    def get_customer_emails(self):
        customers_endpoint = self.user_endpoint
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
