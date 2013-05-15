import unittest

from mockito import *
from reservations import *
from ticket_office import *

class TestTicketOffice(unittest.TestCase):

    def _test_reserve_seats(self):
        office = TicketOffice(train_data_service = "http://localhost:8081", 
                              booking_reference_service = "http://localhost:8082")
        request = ReservationRequest(train_id="express_2000", seat_count=4)
        
        reservation = office.make_reservation(request)
        
        self.assertEqual(4, len(reservation.seats))
        self.assertEqual("A", reservation.seats[0].coach)
        self.assertEqual("75bcd15", reservation.booking_reference)

    def test_reserve_seats_internal(self):
        train = { "seats": [{ "coach" : "A", "seat_number" : "1" },
                            { "coach" : "A", "seat_number" : "2" }]}
        data_service = mock()
        when(data_service).get("express_2000").thenReturn(train)
        ref_service = mock() ; when(ref_service).get().thenReturn('75bcd15')
        handler = TicketHandler(train_data_service = data_service,
                               booking_reference_service = ref_service)
        request = ReservationRequest(train_id="express_2000", seat_count=2)
        reservation = handler.make_reservation(request)
        
        self.assertEqual(2, len(reservation.seats))
        self.assertEqual("A", reservation.seats[0].coach)
        self.assertEqual("75bcd15", reservation.booking_reference)

    def test_train_seats(self):
        seats = TrainSeats([{ "coach" : "A", "seat_number" : "1" },
                            { "coach" : "A", "seat_number" : "2" }])
        self.assertEqual(seats.coaches, {"A": ["1", "2"]})

    def test_trains_seats_get(self):
        seats = TrainSeats([{ "coach" : "A", "seat_number" : "1" },
                            { "coach" : "A", "seat_number" : "2" }])
        seat = seats.get(1)
        assert seat[0].coach == "A" 
        assert seat[0].seat_number == "1" 

if __name__ == '__main__':
    unittest.main()
