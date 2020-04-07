import random
import time
from termcolor import colored
from simpleeval import simple_eval


class Bot:

    def __init__(self):
        self.q = ""
        self.a = ""
        
    def _think(self,s): #下划线警告不要外部改动
        return s
    
    def _format(self,s):
        return colored(s,'blue')

    def _say(self,s):
        time.sleep(Bot.wait)
        print(self._format(s))

    def run(self):
        self._say(self.q)
        self.a = input()
        self._say(self._think(self.a))


class HelloBot(Bot):

    def __init__(self):
        self.q = "Hi! What's your name?"
    
    def _think(self,s):
        return f"Hello {s}!"
        

class GreetingBot(Bot):

    def __init__(self):
        self.q = "How are you today?"

    def is_good(self,s):
        return 'good' in s.lower()
    
    def _think(self,s):
        if self.is_good(s):
            return "I'm feeling good, too."
        else:
            return "Sorry to hear that."


class ColorBot(Bot):

    def __init__(self):
        self.q = "What's your favorite color?"
        
    def _think(self,s):
        colors = ['red','green','orange','blue','brown','purple','gray']
        return f"You like {s}? That's beautiful color! I love {random.choice(colors)}."


class CalcBot(Bot):

    def __init__(self):
        self.q = "I've learned to calculate. Give me some arithmatic expression to try:"

    def _think(self,s):
        result = simple_eval(s)
        return f"Done. Result = {result}"


class Garfield:

    def __init__(self,wait=1):
        Bot.wait = wait
        self.bots = []
        
    def add(self,bot):
        self.bots.append(bot)
        
    def run(self):
        print("This is a dialog system. Let's talk.")
        print()
        
        for bot in self.bots:
            bot.run()


if __name__ == "__main__":
    g = Garfield()
    g.add(HelloBot())
    g.add(GreetingBot())
    g.add(ColorBot())
    g.add(CalcBot())
    g.run()