#  For Regular Seats
class RegularSeat(Seat):
    def get_price(self):
        return super().get_price()

# For VIP Seats +  Extra Charge
class VIPSeat(Seat):
    def get_price(self):
        base_price = super().get_price()
        return base_price + 100 