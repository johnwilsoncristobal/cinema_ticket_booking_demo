# PDF or Digital Ticket
class DigitalTicket(Ticket):
    def to_pdf(self):
        super().to_pdf() 

# Paper Ticket
class PaperTicket(Ticket):
    def to_pdf(self):
        with open("ticket.txt", "w") as f:
            f.write(f"Ticket ID: {self.id}\n")
            f.write(f"Name: {self.user.name}\n")
            f.write(f"Seat No: {self.seat_number}\n")
            f.write(f"Price: {self.price}\n")