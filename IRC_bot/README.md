## IRC chatbot

Direct link to original repo: https://github.com/svimanet/chatbot

#### This software is an automated chatbot to be used with web chatrooms. Users are able to specify a server, port, password, and desired room to connect the bot to. This chatbot reads chatroom messages and processes them, producing a desired output in the chatroom.   

![alt text](https://i.imgur.com/dAwS00J.png)


## Open for hacktober contributions!       ![alt text](https://img.shields.io/github/contributors-anon/svimanet/chatbot)


#### - Create modules and add them to actuators, or just make the bot more robust!
#### - Find the contribution guidelines [here](docs/CONTRIBUTING.md)  
  

## Instructions

#### 1. Clone/copy this repository to your local machine

#### 2. Navigate inside of the newly downloaded directory

#### 3. Optional: configure config.json to settings other than default

#### 4. Build Docker image: 

```shell
docker build -t chatbot .
```
#### 5. Run chatbot:

```shell
docker run --rm -it chatbot
```

## Commands

#### - Chatbot reads commands as phrases prefixed with exclamation points (e.g., !help)
#### - Some commands require an argument following the initial phrase (e.g., !roll 5d50)
* #### **!urban word** -Searches and returns urban dictionary for provided word
* #### **!wiki word/phrase** - Searches and returns urban dictionary for provided word/phrase
* #### **!roll 5d50** - Provides randomized rolls of a 5 sided dice 50 times
* #### **!flip** - Provides randomized head or tails
* #### **!joke** - Provides a random joke
* #### **!chuck** - Provides a random Chuck Norris joke
* #### **!quote** - Provides a random quote
* #### **!horoscope sign** - Provides a daily horoscope corresponding to the provided sign
* #### **!cat** - Provides a link to a super cute cat pic
* #### **!dog** - Provides a link to a super cute dog pic
* #### **!jesus** - Provides a special message from jesus
* #### **!catfact** - Provides a random cat fact
* #### **!draw** - Provides a card randomly drawn from a deck
* #### **!help** - Displays available commands

## License
#### [The Unlicense](LICENSE)



