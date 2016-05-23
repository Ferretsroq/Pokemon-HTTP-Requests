from context import *
import unittest

class TestPokemon(unittest.TestCase):
	def setUp(self):
		unittest.TestCase.setUp(self)
		self.mypokemon = Pokemon(mockDataSource)
	def tearDown(self):
		unittest.TestCase.tearDown(self)
	def testName(self):
		self.assertEqual(self.mypokemon.thisPokemonName,'Name','Wrong name reported')
	def testNumber(self):
		self.assertEqual(self.mypokemon.totalNumberOfThisPokemon,1,'Wrong number reported')

mockDataFile = shelve.open('./testData')
mockDataSource = mockDataFile['mockData']
unittest.main()
