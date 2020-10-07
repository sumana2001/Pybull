from modules import urban_dictionary
from modules import roll
from modules import jokes
from modules import quote_day
from modules import horoscope
from modules import random_cat
from modules import random_dog
from modules import jesus
from modules import random_cat_fact
from modules import draw_card
from modules import wiki_summary
from modules import covid19
from modules import sentiment

class Actuator:
    """ Class object for handling command activations. """
    def __init__(self):
        self.perform = False
        self.nick = None
        self.pm = False
        # Define commands case switch
        self.dic = {
            "!urban": self.urban,
            "!wiki": self.wiki,
            "!roll": self.roll,
            "!flip": self.flip,
            "!joke": self.joke,
            "!chuck": self.chuck_joke,
            "!quote": self.quote,
            "!horoscope": self.horoscope,
            "!cat": self.cat,
            "!dog": self.dog,
            "!jesus": self.jesus,
            "!catfact": self.cat_fact,
            "!draw": self.draw_card,
            "!help": self.help,
            "!covidglobal": self.covidglobal,
            "!covidcountry": self.covidcountry,
            "!sentiment": self.sentiment
        }

    def command(self, msg, nick, pm):
        """ Parse and activate command from dict switch. """
        # Parse message, return if no command is given.
        command = self.message_start(msg)

        # If no command was given, no actions are performed
        if (not command): self.should_perform(False, nick)
        else: self.should_perform(True, nick)
        if (not self.perform): return False

        # Activate command
        def switcher(command, argument):
            return self.dic.get(command)(argument)
        try:
            result = switcher(command[0], (command[1]))
            return result
        except Exception as e:
            print(e)
            return "Sorry, I did not understand that command."


    def message_start(self, msg):
        """ Parses the message to determine whether or not to execute a command. """
        try:
            if (not msg.startswith("!")): return False
            msg = msg.replace("\r\n", "")
            split = msg.split(" ")
            start = split[0]

            # If no command is given, return false
            if (len(start) <= 0): return False
            # If no argument is given, return with command and no argument
            elif (len(split) <= 1): argument = False
            # Else, return with command and argument
            else: argument = msg.split(start)[1][1:]
            return (start, argument)

        # Only one word was received
        except IndexError: return False


    def should_perform(self, bool, nick):
        self.perform = bool
        self.nick = nick
        self.pm = bool

    def missing_argument(self):
        return "Did you forget an argument?"

    def urban(self, argument):
        if (argument): return urban_dictionary.urban_term(argument)
        return self.missing_argument()

    def roll(self, argument):
        if (argument): return roll.roll(argument)
        return self.missing_argument()

    def wiki(self, argument):
        if (argument): return wiki_summary.scrape(argument)
        return self.missing_argument()

    def flip(self, argument):
        return roll.coin_flip()

    def joke(self, argument):
        return jokes.random_joke()

    def chuck_joke(self, argument):
        return jokes.random_chuck_joke()

    def quote(self, argument):
        return quote_day.quote_of_the_day()

    def horoscope(self, argument):
        if (argument): return horoscope.get_horoscope(argument)
        return self.missing_argument()

    def cat(self, argument):
        return random_cat.random_cat_pic()

    def dog(self, argument):
        return random_dog.random_dog_pic()

    def jesus(self, argument):
        return jesus.jesus()

    def cat_fact(self, argument):
        return random_cat_fact.random_cat_facts()

    def draw_card(self, argument):
        return draw_card.draw_card()

    def covidglobal(self, argument):
        return covid19.get_global_covid_cases()

    def covidcountry(self, argument):
        if (argument): return covid19.get_covid_cases_by_country(argument)
        return self.missing_argument()

    def sentiment(self, argument):
        if (argument): return sentiment.get_sentiment(argument)
        return self.missing_argument()

    def help(self, argument):
        return "The available commands are: " + str(list(self.dic))[1:-1]

