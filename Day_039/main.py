# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import *
from flight_search import *
from notification_manager import *
dm = DataManager()
sheetdata = dm.return_sheet_data()
fm = FlightSearch()

for data in range(len(sheetdata)):
    if sheetdata[data]["iata"] == "":
        city = sheetdata[data]["city"]
        iata = fm.location(city)
        dm.put_sheet_data(row=data+2, iata=iata)
    flight = fm.search_ticket(sheetdata[data]["iata"])
    print(sheetdata[data])
    try:
        if sheetdata[data]["price"] >= flight.price:
            n = NotificationManager()
            n.noti(
                f"Low price alert! Only £{flight.price}원 to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")

        else:
            print("not now it still expensive")
    except AttributeError:
        pass
