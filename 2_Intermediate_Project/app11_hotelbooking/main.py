import pandas as pd
import numpy as np


df = pd.read_csv(
    "2_Intermediate_Project/app11_hotelbooking/hotels.csv",
    dtype={
        "id": str,
    },
)
df.index += 1


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing it availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("2_Intermediate_Project/app11_hotelbooking/hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""Thank you for your reservation! \nHere are your booking details: \nName: {self.customer_name} \nHotel: {self.hotel.name}
        """
        return content


if __name__ == "__main__":
    print(df)
    hotel_id = input("Enter the id of the hotel: ")
    hotel = Hotel(hotel_id=hotel_id)
    if hotel.available():
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        print(reservation_ticket.generate())

    else:
        print("Hotel is not available")
