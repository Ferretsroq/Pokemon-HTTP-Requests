from lxml import html
import requests
import json
from fractions import Fraction

def PrintData(section, name):
    for block in section:
        print block['ranking'], block[name], block['usageRate']
    print "\n ---------- \n"

def GetData(pokemonID):
    requestDataList = [
        'languageId=2',
        'seasonId=114',
        'battleType=5',
        'timezone=EST',
        'pokemonId=%d-0' % (pokemonID),
        'displayNumberWaza=20',
        'displayNumberTokusei=3',
        'displayNumberSeikaku=20',
        'displayNumberItem=20',
        'displayNumberLevel=20',
        'displayNumberPokemonIn=20',
        'displayNumberPokemonDown=20',
        'displayNumberPokemonDownWaza=20',
        'timeStamp=1453422223192'
        ]
    requestDataString = "&".join(requestDataList)
    pokemonData = json.loads(requests.post(url, data=requestDataString, headers=headersDictionary).text)
    return pokemonData

def GetFormeData():
    returnList = []
    pokemonWithFormes = {
        'Rotom-H' : '479-1',
        'Rotom-W' : '479-2',
        'Rotom-Frost' : '479-3',
        'Rotom-Fan' : '479-4',
        'Rotom-M' : '479-5',
        'Giratina-O' : '487-1',
        'Tornadus-T' : '641-1',
        'Thundurus-T' : '642-1',
        'Landorus-T' : '645-1',
        'Kyurem-W' : '646-1',
        'Kyurem-B' : '646-2',
        'Meowstic-F' : '678-1',
        'Gourgeist-Small' : '711-1',
        'Gourgeist-Large' : '711-2',
        'Gourgeist-Super' : '711-3'
        }
    for pokemon in pokemonWithFormes:
        requestDataList = [
        'languageId=2',
        'seasonId=114',
        'battleType=5',
        'timezone=EST',
        'pokemonId=%s' % (pokemonWithFormes[pokemon]),
        'displayNumberWaza=20',
        'displayNumberTokusei=3',
        'displayNumberSeikaku=20',
        'displayNumberItem=20',
        'displayNumberLevel=20',
        'displayNumberPokemonIn=20',
        'displayNumberPokemonDown=20',
        'displayNumberPokemonDownWaza=20',
        'timeStamp=1453422223192'
        ]
        requestDataString = "&".join(requestDataList)
        print "Now obtaining %s!" % (pokemon)
        pokemonData = json.loads(requests.post(url, data=requestDataString, headers=headersDictionary).text)
        pokemonData['rankingPokemonInfo']['name'] = pokemon
        print "We obtained %s!" % (pokemon)
        returnList.append(Pokemon(pokemonData))
    return returnList
        
class Pokemon:
    def __init__(self, pokemonData):
        self.thisPokemonName = pokemonData['rankingPokemonInfo']['name']
        if(pokemonData['rankingPokemonTrend']):
            self.thisPokemonRanking = pokemonData['rankingPokemonInfo']['ranking']
            self.movesThatThisPokemonKOsWith = pokemonData['rankingPokemonSuffererWaza']
            self.pokemonThatThisPokemonKOs = pokemonData['rankingPokemonSufferer']
            self.pokemonOnTheSameTeamWithThisPokemon = pokemonData['rankingPokemonIn']
            self.movesThatThisPokemonUses = pokemonData['rankingPokemonTrend']['wazaInfo']
            self.itemsThatThisPokemonUses = pokemonData['rankingPokemonTrend']['itemInfo']
            self.abilitiesThatThisPokemonUses = pokemonData['rankingPokemonTrend']['tokuseiInfo']
            self.naturesThatThisPokemonUses = pokemonData['rankingPokemonTrend']['seikakuInfo']
            self.pokemonThatKOThisPokemon = pokemonData['rankingPokemonDown']
            self.movesThatKOThisPokemon = pokemonData['rankingPokemonDownWaza']
            self.listOfPercentages = []
            self.listOfDenominators = []
            self.PopulatePercentages(self.movesThatThisPokemonKOsWith)
            self.PopulatePercentages(self.movesThatThisPokemonUses)
            self.PopulatePercentages(self.itemsThatThisPokemonUses)
            self.PopulatePercentages(self.abilitiesThatThisPokemonUses)
            self.PopulatePercentages(self.naturesThatThisPokemonUses)
            self.PopulatePercentages(self.movesThatKOThisPokemon)
    def __repr__(self):
        return self.thisPokemonName
    def PopulatePercentages(self, numericalData):
        if(numericalData):
            for element in numericalData:
                self.listOfPercentages.append(element['usageRate']/100)
            for percentage in self.listOfPercentages:
                self.listOfDenominators.append((Fraction(percentage).limit_denominator()).denominator)

def orderByRanking(listOfPokemon):
	numberOfRankedPokemon = 0
	rankingNotFound = 0
	numberOfPokemonWithoutThisRanking = 0
	lowestNumber = 1
	for pokemon in listOfPokemon:
		if(hasattr(pokemon, 'thisPokemonRanking')):
			numberOfRankedPokemon+=1
	orderedList = []
	print numberOfRankedPokemon
	while(len(orderedList) < numberOfRankedPokemon):
		numberOfPokemonWithoutThisRanking = 0
		if(rankingNotFound==1): lowestNumber+=1
		print "We are looking for rank %d" % (lowestNumber)
		for pokemon in pokemonList:
			if(hasattr(pokemon, 'thisPokemonRanking')):
				if(pokemon.thisPokemonRanking == lowestNumber):
					orderedList.append(pokemon)
					lowestNumber+=1
					rankingNotFound = 0
					print pokemon, pokemon.thisPokemonRanking
				else:
					numberOfPokemonWithoutThisRanking+=1
					if(numberOfPokemonWithoutThisRanking == numberOfRankedPokemon):
						rankingNotFound = 1

	return orderedList

headersDictionary = {
	'Accept' : '*/*',
	'Accept-Encoding' : 'gzip, deflate',
	'Accept-Language' : 'en-US,en;q=0.8',
	'Connection' : 'keep-alive',
	'Content-Length' : '288',
	'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie' : '__ulfpc=201507141648558514; __utma=234147713.44858212.1436906933.1450754425.1450754425.1; __utmz=234147713.1450754425.1.1.utmcsr=pokemon-gl.com|utmccn=(referral)|utmcmd=referral|utmcct=/; region=1; language_id=2; site=2; JSESSIONID=DD14469E9FCCB8E77EC19C37921BE293; AWSELB=99C3FF770EA3504C46F25D799674203D12E259AC7AF523A441BC83B81A7A34CC74546EE73334E1A5AE0296D9AE6D620857C9DF385445A267DB7E496BEA70327F1D05B86B1023FF697977A00E295CBB8437E703A8CE; _ga=GA1.2.44858212.1436906933; _gat=1; NO_MEMBER_DATA=%7B%22language_id%22%3A2%2C%22site%22%3A2%2C%22region%22%3A1%7D',
		'Host' : '3ds.pokemon-gl.com',
	'Origin' : 'http://3ds.pokemon-gl.com',
	'Referer' : 'http://3ds.pokemon-gl.com/battle/oras/',
	'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
	}

url = "http://3ds.pokemon-gl.com/frontendApi/gbu/getSeasonPokemonDetail"


pokemonList = [0]
alternateFormesList = GetFormeData()

for dexNumber in range(720):
    pokemonList.append(Pokemon(GetData(dexNumber+1)))
    print unicode(pokemonList[dexNumber+1])

pokemonList = pokemonList + alternateFormesList

orderedListByRank = orderByRanking(pokemonList)
print orderedListByRank

print "Length of ordered list: %d" % len(orderedListByRank)
for x in orderedListByRank:
    print x.thisPokemonRanking, x.thisPokemonName
