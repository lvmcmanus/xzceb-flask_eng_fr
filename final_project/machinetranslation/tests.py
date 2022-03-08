import unittest

import translator

class EnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.english_to_french(""), "") 
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")  
        self.assertNotEqual(translator.english_to_french(""), "Bonjour")  
        

class FrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.french_to_english(""), "") 
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")  
        self.assertNotEqual(translator.french_to_english(""), "Hello")  
        
unittest.main()
