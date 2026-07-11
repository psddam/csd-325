# Name: Peter Ddamulira
# Assignment: Module 7.2 - Test Cases
# Description:
# This program tests the city_country() function using unittest.

import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for the city_country() function."""

    def test_city_country(self):
        """Verify that Santiago, Chile is formatted correctly."""
        formatted_location = city_country("santiago", "chile")
        self.assertEqual(formatted_location, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()