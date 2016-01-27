from lxml import html
import requests
import json

def PrintData(section):
        for block in section:
                for element in block:
                        if(element != "sequenceNumber"):
                                if(element == "wazaName"): 
                                        print "Move", block[element]
                                else: 
                                        print element, block[element]
                print "---"

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

requestDataList = [
	'languageId=2',
	'seasonId=114',
	'battleType=5',
	'timezone=EST',
	'pokemonId=383-0',
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

url = "http://3ds.pokemon-gl.com/frontendApi/gbu/getSeasonPokemonDetail"
requestDataString = "&".join(requestDataList)
r = requests.post(url, data=requestDataString, headers=headersDictionary)
#print r.text

pokemonData = json.loads(r.text)

movesThatKOThisPokemon = pokemonData['rankingPokemonDownWaza']
movesThatThisPokemonUses = pokemonData['rankingPokemonTrend']['wazaInfo']

print "These are the moves that KO this pokemon!"
PrintData(movesThatKOThisPokemon)
print "These are the moves that this pokemon uses!"
PrintData(movesThatThisPokemonUses)
