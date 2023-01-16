# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import *
from flight_search import *
from notification_manager import *
dm = DataManager()
sheetdata = dm.return_sheet_data()
fm = FlightSearch()

print("Welcome to Ocean's Flight Club. \nWe find the best flight deals and email you.")
user_First_name = input("What is your first name\n")
user_Last_name = input("What is your last name\n")
user_email = input("What is your email?\n")
while True:
    if user_email == input("Type your email again\n"):
        print("You're in the club!")
        break
dm.post_shee_user_data(Fname=user_First_name,
                       Lname=user_Last_name, email=user_email)

for data in range(len(sheetdata)):
    if sheetdata[data]["iata"] == "":
        city = sheetdata[data]["city"]
        iata = fm.location(city)
        dm.put_sheet_data(row=data+2, iata=iata)
    flight = fm.search_ticket(sheetdata[data]["iata"])
    try:
        if sheetdata[data]["price"] >= flight.price:
            users = dm.get_customer_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]
            n = NotificationManager()
            n.noti(
                f"Low price alert! Only £{flight.price}원 to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.", emails)
            n.noti(
                f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}", emails)
            if flight.step_overs > 0:
                n.noti(
                    f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}.")
        else:
            print("not now it still expensive")
    except AttributeError:
        pass
