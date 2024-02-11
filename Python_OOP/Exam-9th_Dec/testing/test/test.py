import unittest
from project.railway_station import RailwayStation  # Replace 'your_module' with the actual module name

class TestRailwayStation(unittest.TestCase):

    def test_constructor(self):
        station = RailwayStation("TestStation")
        self.assertEqual(station.name, "TestStation")
        self.assertEqual(len(station.arrival_trains), 0)
        self.assertEqual(len(station.departure_trains), 0)

    def test_name_property_valid(self):
        station = RailwayStation("TestStation")
        self.assertEqual(station.name, "TestStation")

    def test_name_property_invalid(self):
        with self.assertRaises(ValueError):
            station = RailwayStation("abc")  # Should raise ValueError

    def test_new_arrival_on_board(self):
        station = RailwayStation("TestStation")
        station.new_arrival_on_board("Train123")
        self.assertEqual(len(station.arrival_trains), 1)
        self.assertEqual(station.arrival_trains[0], "Train123")

    def test_train_has_arrived_valid(self):
        station = RailwayStation("TestStation")
        station.new_arrival_on_board("Train123")
        result = station.train_has_arrived("Train123")
        self.assertEqual(result, "Train123 is on the platform and will leave in 5 minutes.")
        self.assertEqual(len(station.arrival_trains), 0)
        self.assertEqual(len(station.departure_trains), 1)

    def test_train_has_arrived_invalid(self):
        station = RailwayStation("TestStation")
        station.new_arrival_on_board("Train123")
        result = station.train_has_arrived("Train456")
        self.assertEqual(result, "There are other trains to arrive before Train456.")
        self.assertEqual(len(station.arrival_trains), 1)
        self.assertEqual(len(station.departure_trains), 0)

    def test_train_has_left_valid(self):
        station = RailwayStation("TestStation")
        station.new_arrival_on_board("Train123")
        station.train_has_arrived("Train123")
        result = station.train_has_left("Train123")
        self.assertTrue(result)
        self.assertEqual(len(station.departure_trains), 0)

    def test_train_has_left_invalid(self):
        station = RailwayStation("TestStation")
        station.new_arrival_on_board("Train123")
        result = station.train_has_left("Train123")
        self.assertFalse(result)
        self.assertEqual(len(station.departure_trains), 0)

if __name__ == '__main__':
    unittest.main()
