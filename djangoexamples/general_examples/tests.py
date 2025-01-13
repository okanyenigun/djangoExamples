from django.test import TestCase
from general_examples.models import Animal, Vehicle


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')    


class VehicleTestCase(TestCase):
    def setUp(self):
        Vehicle.objects.create(name="Tesla Model S", top_speed=250, is_electric=True)
        Vehicle.objects.create(name="Toyota Corolla", top_speed=180, is_electric=False)
        Vehicle.objects.create(name="Bugatti Chiron", top_speed=420, is_electric=False)

    def test_vehicle_description(self):
        """Test the description method of Vehicle"""
        tesla = Vehicle.objects.get(name="Tesla Model S")
        self.assertEqual(tesla.description(), "Tesla Model S can go up to 250 km/h.")

    def test_vehicle_is_fast(self):
        """Test the is_fast method of Vehicle"""
        bugatti = Vehicle.objects.get(name="Bugatti Chiron")
        toyota = Vehicle.objects.get(name="Toyota Corolla")

        self.assertTrue(bugatti.is_fast())  # Bugatti is fast
        self.assertFalse(toyota.is_fast())  # Toyota is not fast

    def test_vehicle_electric_status(self):
        """Test if a vehicle is electric or not"""
        tesla = Vehicle.objects.get(name="Tesla Model S")
        bugatti = Vehicle.objects.get(name="Bugatti Chiron")

        self.assertIs(tesla.is_electric, True)  # Tesla is electric
        self.assertIs(bugatti.is_electric, False)  # Bugatti is not electric

    def test_vehicle_count(self):
        """Test the count of vehicles"""
        count = Vehicle.objects.count()
        self.assertEqual(count, 3)  # Assert the number of vehicles is 3

    def test_vehicle_in_database(self):
        """Test if a specific vehicle exists in the database"""
        self.assertTrue(Vehicle.objects.filter(name="Tesla Model S").exists())
        self.assertFalse(Vehicle.objects.filter(name="Ford Mustang").exists())

    def test_vehicle_order(self):
        """Test the order of vehicles based on top speed"""
        vehicles = Vehicle.objects.all().order_by('-top_speed')
        self.assertEqual(vehicles[0].name, "Bugatti Chiron")  # Fastest vehicle
        self.assertEqual(vehicles.last().name, "Toyota Corolla")  # Slowest vehicle

    def test_vehicle_top_speed(self):
        """Test top speed of a vehicle"""
        toyota = Vehicle.objects.get(name="Toyota Corolla")
        self.assertGreater(toyota.top_speed, 100)  # Speed > 100
        self.assertLess(toyota.top_speed, 200)  # Speed < 200

    def test_vehicle_top_speed_range(self):
        """Test if all vehicles have top speeds in a realistic range"""
        vehicles = Vehicle.objects.all()
        for vehicle in vehicles:
            self.assertIn(vehicle.top_speed, range(100, 500))  # Speed should be between 100 and 500

    def test_vehicle_attributes(self):
        """Test that a vehicle has specific attributes"""
        tesla = Vehicle.objects.get(name="Tesla Model S")
        self.assertIsInstance(tesla.name, str)  # Name is a string
        self.assertIsInstance(tesla.top_speed, int)  # Top speed is an integer
        self.assertIsInstance(tesla.is_electric, bool)  # is_electric is a boolean

    def test_vehicle_contains_correct_names(self):
        """Test that the database contains specific vehicle names"""
        vehicle_names = list(Vehicle.objects.values_list('name', flat=True))
        self.assertListEqual(
            vehicle_names, 
            ["Tesla Model S", "Toyota Corolla", "Bugatti Chiron"]
        )

    def test_vehicle_database_integrity(self):
        """Test that all vehicle entries in the database are unique"""
        vehicles = Vehicle.objects.values_list('name', flat=True)
        self.assertCountEqual(
            vehicles, 
            ["Tesla Model S", "Toyota Corolla", "Bugatti Chiron"]
        )  # Ensures all names are unique


class HomePageTestCase(TestCase):
    def test_home_page(self):
        # Simulate a GET request to the home view
        response = self.client.get('/general/home/')
        
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        
        # Check the response content
        self.assertContains(response, "Welcome to the homepage!")