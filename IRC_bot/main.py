# Import libs
import socket
import ssl
import os
import json

# Import modules
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

from commands import Actuator

class Bot:
    def __init__(self):
        self.irc_socket = False
        self.actuator = Actuator()

        # Load config
        self.load_config()
        
        # Start bot
        self.server_connect()
        self.start_bot()
    
    def load_config(self):
        conf_dir = os.path.abspath(os.path.dirname(__file__))
        conf_fp = os.path.join(conf_dir, 'config.json')
        conf = {}
        try:
            if os.path.isfile(conf_fp):
                conf = json.load(open(conf_fp))
            else:
                default_fp = os.path.join(conf_dir, 'default_config.json')
                conf = json.load(open(default_fp))
                json.dump(conf, open(conf_fp, 'w+'), indent=2)
                print("Using default config. Edit config.json to change connection details")
        except Exception as e:
            print("Exiting program. Could not load config -> ", e)
            exit()
        for k, v in conf.items():
            setattr(self, k, v)


    def server_connect(self):
        """ Starts server connection to specified self.server. """
        #try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.server, int(self.port)))
        self.irc_socket = ssl.wrap_socket(sock)
        #except: # TODO find out which exception


    def sock_send(self, msg):
        """ Sends data through socket. Does not send socks. 
        :param msg: The String content to send through socket. """
        msg += '\r\n'  # New line counts as 'return/exec ..'
        self.irc_socket.send(msg.encode('utf-8'))
        print("socket_msg:", msg)


    def send_msg(self, msg, nick, pm):
        """ Sends a Private Message or a message to the channel its connected to.
        :param msg: String message to send.
        :param nick: nick of user that sent msg, and nick to respond if PM.
        :param pm: Boolean if its supposed to send privately. """
        if pm: self.irc_socket.send("PRIVMSG {0} :{1}\r\n".format(nick, msg).encode('utf-8'))
        else: self.irc_socket.send("PRIVMSG {0} :{1}\r\n".format(self.channel, msg).encode('utf-8'))


    def ping_pong(self, data):
        """ Responds PONG to server Pings. 
        :param data: raw socket data from server. """
        if "PRIVMSG" not in data and "PING" in data.split(':')[0]:
            self.sock_send("PONG {}".format(data.split(':')[1]))


    def join_channel(self, data):
        """ Joins a the specified server channel, under startup.
        :param data: Raw socket data from server. """
        if "PRIVMSG" not in data and "266" in data:
            if self.password: msg = "JOIN {} {}".format(self.channel, self.password)
            else: msg = "JOIN {}".format(self.channel)
            self.sock_send(msg)
            return True
        return False


    def check_errors(self, data):
        """ Checks for IRC errors, and one day it will handle it correctly.
        :param data: Raw socket data from server. """
        if "PRIVMSG" not in data and "ERR" in data:
            print("ERROR YALL")
            # TODO: Actual error handling


    def parse_msg(self, data):
        """ Parses messages to check for user messages, and handle them correctly.
        :param data: Raw socket data from server. """
        if "PRIVMSG" in data:
            details = data.split(":")[1]
            nick = details.split("!")[0]
            message = data.split(" :", 1)[1]

            if self.channel in details:
                result = self.actuator.command(message, nick, False)
                pm = False
            else:
                result = self.actuator.command(message, nick, True)
                pm = True
            if result: self.send_msg(result, nick, pm)


    def start_bot(self):
        """ Starts the bot and connects to channel. Then goes into actuator mode. """
        self.sock_send("USER {0} {1} {1} {2}".format(self.nick, self.hostname, self.name))
        print("USER {0} {1} {1} {2}".format(self.nick, self.hostname, self.name))
        self.sock_send("NICK {}".format(self.nick))
        joined = False
        starting = True
        while starting:
            data = self.irc_socket.recv(1024).decode('utf-8')
            print("Startup Recv = ", data)
            self.ping_pong(data)
            joined = self.join_channel(data)
            if joined: starting = False

        print("#############\nStartup success\n#############")
        self.run()


    def run(self):
        """ Keeps the bot running after startup and channel join. """
        running = True
        while running:
            data = self.irc_socket.recv(1024).decode('utf-8')
            print("Recv = ", data.replace("\r\n", ""))
            self.ping_pong(data)
            self.check_errors(data)
            self.parse_msg(data)

# Start
if __name__ == '__main__': bob = Bot()
