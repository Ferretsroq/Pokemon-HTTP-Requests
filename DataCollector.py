from pokemon import *

pokemonList = [0]
alternateFormesList = GetFormeData()

'''Populates the pokemonList with every pokemon'''
for dexNumber in range(720):
    pokemonList.append(Pokemon(GetData(dexNumber+1)))
    print pokemonList[dexNumber+1].thisPokemonName.decode('utf8')

pokemonList = pokemonList + alternateFormesList

'''Creates an ordered list, ordered by Battle Spot ranking'''
orderedListByRank = orderByRanking(pokemonList)
print orderedListByRank

print "Length of ordered list: %d" % len(orderedListByRank)
'''Writes the data to text files'''
for x in orderedListByRank:
    print x.thisPokemonRanking, x.thisPokemonName.decode('utf8'), x.totalNumberOfThisPokemon

dataFile = shelve.open('./Data')
dataFile['data'] = orderedListByRank
dataFile.close()
