import unittest
from algoritmosGeneticos.findingWords.wordSuite import *

class MyTestCase(unittest.TestCase):
    def testStringsToArrays(self):
        s1="hola"
        s2="hipopotamo"
        self.assertEqual(stringToArray(s1),['h', 'o', 'l', 'a'])
        self.assertEqual(stringToArray(s2),['h', 'i', 'p', 'o','p','o','t','a','m','o'])

    def testArraysToStrings(self):
        A1=['g','a','t','o']
        A2=['h','o','m','e','r','o']
        self.assertEqual(arrayToString(A1),"gato")
        self.assertEqual(arrayToString(A2),"homero")

    def testMatchesArray(self):
        A1=['g','a','t','o']
        A2=['p','a','t','o']
        A3=['z','e','p','i']

        self.assertEqual(matchArray(A1,A2),3)
        self.assertEqual(matchArray(A1,A3),0)


    def testMatchesString(self):
        s1="perros"
        s2="aaraaa"
        s3="cerdos"
        self.assertEqual(matchString(s1,s2),1)
        self.assertEqual(matchString(s1,s3),4)





if __name__ == '__main__':
    unittest.main()
