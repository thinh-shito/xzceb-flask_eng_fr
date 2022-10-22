import unittest
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):

    def test1(self):
        self.assertEqual(english_to_french('IBM is the best'),'IBM est le meilleur')
        self.assertEqual(french_to_english('IBM est le meilleur'),'IBM is the best')
    
    def test2(self):
        self.assertEqual(english_to_french('This course is good'), 'Ce cours est bon')
        self.assertEqual(french_to_english('Ce cours est bon'), 'This course is good')
    
    def test3(self):
        self.assertNotEqual(english_to_french('The test is good'),'Le test est mauvais')
        self.assertNotEqual(french_to_english('Le test est mauvais'),'The test is good')
    
    def test4(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(french_to_english(None), None)
    
    def test5(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    
   
unittest.main()
        