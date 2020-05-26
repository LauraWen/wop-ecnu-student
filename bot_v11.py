import random
import time
import requests
from termcolor import colored
from simpleeval import simple_eval


class Bot:

    def __init__(self):
        self.q = ""
        self.a = ""
        
    def _think(self,s): 
        return s
    
    def _format(self,s):
        return colored(s,'blue')

    def _say(self,s):
        time.sleep(Bot.wait)
        print(self._format('Bot:'),self._format(s))

    def run(self):
        self._say(self.q)
        self.a = input('User:')
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


class AirBot(Bot):
    
    def __init__(self):
        self.q = "I've learned to search the air quality. I'll show you if you can give me a city："
        
    def _think(self,s):
        
        """
        To get the air quality of one city.
        Official: http://aqicn.org/here/
        Token Adress：http://aqicn.org/data-platform/token/#/
        Param city: city
        return:
        """
        
        city = self.a
        AQICN_TOKEN = '7bd4d1430e3019c7e09c8d19d66a586c3d1b93d4'
        AIR_STATUS_DICT = {
            50: 'Good',
            100: 'Moderate',
            150: 'Unhealthy for Sensitive Groups',
            200: 'Unhealthy',
            300: 'Very Unhealthy',
            3000: 'Hazardous'
        }
        
        if not city or not city.strip():
            return
        self._say(f'Getting the air quality of {city} ...')
        try:
            url = f'http://api.waqi.info/feed/{city}/?token={AQICN_TOKEN}'
            resp = requests.get(url)
            if resp.status_code == 200:
                content_dict = resp.json()
                if content_dict.get('status') == 'ok':
                    data_dict = content_dict['data']
                    aqi = data_dict['aqi']
                    air_status = 'Hazardous'
                    for key in sorted(AIR_STATUS_DICT):
                        if key >= aqi:
                            air_status = AIR_STATUS_DICT[key]
                            break
                    aqi_info = f'{city} PM2.5：{aqi} \n{air_status}'
                    return aqi_info
                else:
                    data_dict = content_dict['data']
                    self._say(f'Failed to get the air quality:\n{data_dict}')
                    return None
        except Exception as exception:
            print(str(exception))
        return None


class CalcBot(Bot):

    def __init__(self):
        self.q = "I've also learned to calculate. Give me some arithmatic expression to try:"
        self.r = "Type 'quit', 'q', 'exit' or 'x' to exit! You can also try again:"
    
    def _think(self,s):
        try:
            result = f"Done. Result = {simple_eval(s)}"
        except:
            result = "Sorry, I can't understand."
        return result
        
    def run(self):
        self._say(self.q)
        while True:
            s = input('User:')
            if s in ['quit','q','exit','x']:
                self._say('Quiting Calculator...')
                break
            self._say(self._think(s))
            self._say(self.r)


class Garfield:

    def __init__(self,wait=1):
        Bot.wait = wait
        self.bots = []
        
    def add(self,bot):
        self.bots.append(bot)
        
    def run(self):
        print()
        print(colored("This is a dialog system. Let's talk.",'yellow'))
        print()
        
        for bot in self.bots:
            bot.run()


if __name__ == "__main__":
    g = Garfield()
    g.add(HelloBot())
    g.add(GreetingBot())
    g.add(ColorBot())
    g.add(AirBot())
    g.add(CalcBot())
    g.run()
