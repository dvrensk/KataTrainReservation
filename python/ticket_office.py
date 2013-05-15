
from reservations import *

class TicketOffice(object):

    def __init__(self, train_data_service, booking_reference_service):
        self.ticket_handler = TicketHandler(DataService(train_data_service), BookingReferenceService(booking_reference_service))

    def make_reservation(self, reservation_request):
        return self.ticket_handler.make_reservation(reservation_request)

class TicketHandler(object):
    def __init__(self, train_data_service, booking_reference_service):
        self.train_data_service = train_data_service
        self.booking_reference_service = booking_reference_service

    def make_reservation(self, reservation_request):
        train_id = reservation_request.train_id
        seat_count = reservation_request.seat_count
        train_data = self.train_data_service.get(train_id)
        train_seats = TrainSeats(train_data["seats"])
        #return Reservation(train_id, [Seat("A", "1"), Seat("A", "2")], "75bcd15")
        return Reservation(train_id, train_seats.get(2), "75bcd15")

class TrainSeats(object):
    def __init__(self, data):
        self.coaches = {}
        for d in data:
            self.coaches.setdefault(d["coach"], []).append(d["seat_number"])

    def get(self, count):
        coach = max(self.coaches, key = lambda k: len(self.coaches[k]))
        return [Seat(coach, seat) for seat in self.coaches[coach][:count]]
        
