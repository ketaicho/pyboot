# write a function that takes in user input for what they want to search
# take that input and make it into a query string
# if you get more than 1 response, take a random one of those responses
# if the string input returns nothing, alert the user of the fact

import requests
from random import randint

url = "https://icanhazdadjoke.com/search"

userInput = input("Enter the search term for the joke: ")

def request(input):
    response = requests.get(
                url,
                headers={"Accept": "application/json"},
                params={"term": input}
                )

    data = response.json()
    dataList = data["results"]
    resultLen = len(dataList)

    if resultLen == 0:
        return "O jokes found, using that term"
    elif resultLen == 1:
        resultDict = dataList[0]
        return resultDict["joke"]
    else:
        randResultDict = dataList[randint(0, resultLen-1)]
        return randResultDict["joke"]

print(request(userInput))
