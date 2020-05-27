import requests
from requests_html import HTML, HTMLSession
import json
import datetime
from pprint import pprint

# Json data for saving each tweet
"""
data['tweet'].append({
                'tweet id: ': twitter,
                'tweet time: ': dataOfTime[counter],
                'tweet content: ': div.text
            })
"""
option = 0

while option != -1:
    print('Please Choose from the following options: ')
    print('1. Displaying tweets of a person')
    print('2. Saving someone\'s tweet')
    print('3. Saving and displaying tweets')
    print('4. Exit the program')

    option = input('Please enter the number here: ')

    if option == -1:
        print("Thanks for trying the tweet saver application ;)")
        break

    data = {
        'Last update': {},
        'tweet': []
    }
    twitter = input('Please enter the twitter\'s id: ')

    r = requests.get('https://twitter.com/' + twitter)

    if r.status_code == 200:  # IF WEBSITE IS ACCESSIBLE
        source = r.text
        html = HTML(html=source)
        times = html.find('a.tweet-timestamp')
        dataOfTime = []
        for a in times:  # GETTING TWEETS TIME
            dataOfTime.append(a.text)

        tweet = html.find('div.js-tweet-text-container')
        counter = 0
        for div in tweet:  # GETTING TWEETS CONTENT
            data['tweet'].append({
                'tweet id: ': twitter,  # assigning content and time into the array
                'tweet time: ': dataOfTime[counter],
                'tweet content: ': div.text
            })
            counter += 1

        # saving last update on tweets on the top of the data
        data['Last update'] = str(datetime.date.today())

        if option == '1':
            pprint(data, indent=2, stream=None, compact=False, sort_dicts=False)

        elif option == '2':
            # Saving tweets with date of each tweets in Json files named based on twitters id
            with open(twitter + '.json', 'w+') as f:
                # saving last update on tweets on the top of the files
                json.dump(data, f, indent=2)
                print("Tweets had been saved in " + twitter + ".json dictionary")

        elif option == '3':
            pprint(data, indent=2, stream=None, compact=False, sort_dicts=False)

            with open(twitter + '.json', 'w+') as f:
                json.dump(data, f, indent=2)
                print("Tweets had been saved in " + twitter + ".json dictionary")

    else:  # IF WEBSITE IS NOT ACCESSIBLE
        print('The account is private or the Website is not available, please try again ')

