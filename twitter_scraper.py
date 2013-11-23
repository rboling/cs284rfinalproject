from TwitterAPI import TwitterAPI
import json

def scrape_data(consumer_key, consumer_secret, access_token_key, access_token_secret):
	theData = {}
	api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
	r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
	with open('prelimData.json', 'w') as outfile:
		counter = 0
		#while counter < 1:
		for item in r.get_iterator():
			if counter > 20:
				break
			else:
				newDict = {}
				for key in item:
					try:
						print "in the try"
						newDict[str(key)] = str(item[key])
					except:
						print "in the except"
						newDict[str(key)] = item[key].encode('utf-8')	
				print "out of here"				
				theData[counter] = newDict
				counter += 1
		json.dump(theData, outfile, sort_keys=True, indent=4, separators=(',', ': '))
if __name__ == "__main__":
	scrape_data('hi5jYIvEJhD0iHTQHiV9g', 'SOGiEhgsUj5fluaFnuAab5l333nIpHlloNpbecBR8', '1143117294-vwm1KW1NvEJ0Zty9OCHMT0pkbA6j32M8F5tcfz3', 'zX88PdUuk3WFC1XaKMbMHgIEDHAHV5nLqaPU7293XxCN5')