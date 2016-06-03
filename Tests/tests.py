from context import *
import unittest

class TestPokemon(unittest.TestCase):
	def setUp(self):
		unittest.TestCase.setUp(self)
		mockDataShelf = shelve.open('./ActualData')
		mockData = mockDataShelf['data']
		self.mockPokemon = mockDataShelf['pokemon']
		mockDataShelf.close()
		self.mypokemon = Pokemon(mockData)
	def tearDown(self):
		unittest.TestCase.tearDown(self)
	def testName(self):
		self.assertEqual(self.mypokemon.thisPokemonName,'Groudon','Wrong name reported')
	def testNumber(self):
		self.assertEqual(self.mypokemon.totalNumberOfThisPokemon,162698,'Wrong number reported')
	def testPercentages(self):
		self.assertEqual(self.mypokemon.listOfPercentages, self.mockPokemon.listOfPercentages, 'Incorrect percentages reported')
	def testRanking(self):
		self.assertEqual(self.mypokemon.thisPokemonRanking, 1, 'Wrong ranking reported')
	def testMovesThatKOWith(self):
		self.assertEqual(self.mypokemon.movesThatThisPokemonKOsWith, self.mockPokemon.movesThatThisPokemonKOsWith,'Incorrect moves that this pokemon KOs with')
	def testGCD(self):
		self.assertEqual(gcd(3,7),1,'Greatest Common Denominator not correct')
	def testLCM(self):
		self.assertEqual(lcm(3,7),21,'Least Common Multiple not correct')
	def testLCMForList(self):
		self.assertEqual(lcmForList([3,7,10]),210,'Least Common Multiple for lists not correct')
	def testPokemonKOd(self):
		self.assertEqual(self.mypokemon.pokemonThatThisPokemonKOs, self.mockPokemon.pokemonThatThisPokemonKOs,'Incorrect KO\'d Pokemon')
	def testTeamPokemon(self):
		self.assertEqual(self.mypokemon.pokemonOnTheSameTeamWithThisPokemon, self.mockPokemon.pokemonOnTheSameTeamWithThisPokemon,'Incorrect teammates')
	def testItems(self):
		self.assertEqual(self.mypokemon.itemsThatThisPokemonUses, self.mockPokemon.itemsThatThisPokemonUses, 'Incorrect items')
	def testAbilities(self):
		self.assertEqual(self.mypokemon.abilitiesThatThisPokemonUses, self.mockPokemon.abilitiesThatThisPokemonUses, 'Incorrect abilities')
	def testNatures(self):
		self.assertEqual(self.mypokemon.naturesThatThisPokemonUses, self.mockPokemon.naturesThatThisPokemonUses, 'Incorrect natures')
	def testPokemonThatKO(self):
		self.assertEqual(self.mypokemon.pokemonThatKOThisPokemon, self.mockPokemon.pokemonThatKOThisPokemon, 'Incorrect Pokemon that KO')
	def testMovesThatKO(self):
		self.assertEqual(self.mypokemon.movesThatKOThisPokemon, self.mockPokemon.movesThatKOThisPokemon, 'Incorrect moves that KO this pokemon')
	


unittest.main()
