import pandas as pd
import numpy as np
from abc import ABC, abstractmethod


df = pd.read_csv(
    "2_Intermediate_Project/app11_hotelbooking/hotels.csv",
    dtype={
        "id": str,
    },
)
df.index += 1


class Hotel:
    watermark = "hello world"

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

    @classmethod
    def get_hotel_len(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""\nThank you for your reservation! \nHere are your booking details: \nName: {self.customer_name} \nHotel: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


class SpaReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""\nThank you for your SPA reservation! \nHere are your SPA booking details: \nName: {self.customer_name} \nHotel: {self.hotel.name}
        """
        return content


hotel1 = Hotel(hotel_id="134")

print(hotel1.get_hotel_len(data=df))
