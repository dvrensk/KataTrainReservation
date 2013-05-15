
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
        return None
