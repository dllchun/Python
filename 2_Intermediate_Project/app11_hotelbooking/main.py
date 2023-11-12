import pandas as pd
import numpy as np


df = pd.read_csv(
    "2_Intermediate_Project/app11_hotelbooking/hotels.csv",
    dtype={
        "id": str,
    },
)
df.index += 1

df_card = pd.read_csv(
    "2_Intermediate_Project/app11_hotelbooking/cards.csv", dtype=str
).to_dict(orient="records")

df_cards_security = pd.read_csv(
    "2_Intermediate_Project/app11_hotelbooking/card_security.csv", dtype=str
)


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


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""\nThank you for your reservation! \nHere are your booking details: \nName: {self.customer_name} \nHotel: {self.hotel.name}
        """
        return content


class SpaReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""\nThank you for your SPA reservation! \nHere are your SPA booking details: \nName: {self.customer_name} \nHotel: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {
            "number": self.number,
            "expiration": expiration,
            "holder": holder,
            "cvc": cvc,
        }

        if card_data in df_card:
            return True
        else:
            return False


# Inheritance
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[
            df_cards_security["number"] == self.number, "password"
        ].squeeze()
        if password == given_password:
            return True
        else:
            return False


if __name__ == "__main__":
    print(df)
    hotel_id = input("Enter the id of the hotel: ")
    hotel = SpaHotel(hotel_id=hotel_id)
    if hotel.available():
        credit_card = SecureCreditCard(
            number="1234567890123456",
        )
        if credit_card.validate(
            expiration="12/26",
            holder="JOHN SMITH",
            cvc="123",
        ):
            password = input("Enter your password: ")
            if credit_card.authenticate(given_password=password):
                hotel.book()
                name = input("Enter your name: ")
                reservation_ticket = ReservationTicket(
                    customer_name=name, hotel_object=hotel
                )
                print(reservation_ticket.generate())

                spa_booking = input("Do you wnat to book a spa package (yes/no): ")
                if spa_booking == "yes":
                    hotel.book_spa_package()
                    spa_ticket = SpaReservationTicket(
                        customer_name=name, hotel_object=hotel
                    )
                    print(spa_ticket.generate())
                else:
                    print("thank you for your reservation")

            else:
                print("Wrong User Authentication.")

        else:
            print("There was a problem with your payment")

    else:
        print("Hotel is not available")
