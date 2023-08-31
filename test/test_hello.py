import unittest
from hello import sayHello

class TestHello(unittest.TestCase):
    
    def setUp(self) -> None:
        print("setUp...")
    
    #tearDown
    def tearDown(self) -> None:
        print("tearDown...")
    
    def test_sayHello(self):
        print("test_sayHello...")
        self.assertEqual(sayHello(), "Hello!")

    def test_sayHello_to_somebody(self):
        print("test_sayHello_to_somebody...")
        self.assertEqual(sayHello("Python"), "Hello, Pytho1n!")
    

if __name__ == "__main__":
    unittest.main()
