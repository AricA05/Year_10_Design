import requests
results = requests.get('https://wger.de/api/v2/exercisecomment/?limit=20&offset=60')
results_json = results.json()
for p in results_json['results']:
	print(p['comment'])
#To print the required information


'''for p in results_json['results']:
    print(p['id'])
for i in results_json['results']:
	print(i['name'])'''


#https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236#:~:text=To%20interact%20with%20an%20API,in%20an%20organized%2C%20logical%20manner.

#https://wger.de/api/v2/equipment/


'''/api/v2/exercisecomment/?limit=20&offset=60'''