import requests


def listCurrency():
    url = "https://currency-exchange.p.rapidapi.com/listquotes"
    headers = {
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
        'x-rapidapi-key': "cc05c34800mshe3478569f3ce412p10039cjsn6cc35bc2595c"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def convert():
    curr1 = input("Convert from : ")
    curr2 = input("Convert to : ")
    ammount = input("ammount: ")

    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"q": ammount, "from": curr1, "to": curr2}

    headers = {
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
        'x-rapidapi-key': "cc05c34800mshe3478569f3ce412p10039cjsn6cc35bc2595c"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print("The converted amount is: {}".format(response.text))


while(True):
    print("Enter 1 to see the list of available coversion")
    print("Enter 2 to convert the currency")
    print("Enter 3 to exit the program.")
    ch = int(input("Enter your choice: "))
    if(ch == 1):
        listCurrency()
    if ch == 2:
        convert()
    if ch == 3:
        break
