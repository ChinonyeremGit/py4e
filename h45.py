# TODO: create the map of actions and then the engine to play the game
# TODO: rescuing the kindgom , i'll create dseries of classes for player to choose what's best
from sys import exit
from textwrap import dedent

# class (object):
#     def enter(self):


class engine(object):
    def __init__(self, map):
        self.map = map

    def play(self):
        current_scene = self.map.opening_scene()
        last_scene = self.map.next_scene('end')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.map.next_scene(next_scene_name)


            current_scene.enter()

class Intro():

    def enter(self):
        print(dedent('''
              The community of umuokoro is in dire danger, a pure in heart
              person is required to emmbark on a jouney to the river of the
              four gods to get a new jar of redemption to protect the
              king and the village from dangers.
              The person is to accept to embark on the journey, use flutes
              to engage things in the forest, eggs for gifts and must forgive
              those who brought the agony to the kingdom
              '''))
        action = input('\n do you wish to continue? \n yes or quit\n>')
        if action.lower() == 'yes':
            return 'journey'
        elif action.lower() == 'quit':
            print('You quit the play, haha')
            exit(1)
        else:
            print('Does not commute')
            return 'intro'


class Journey():

    def enter(self):
        print(dedent('''
              You agreed to save the kingdom, the chiefpriest fortifies you,
              gives you a flute, eggs, and ties a ribbon on your forehead as
              a symbol of authority for you to enter the land of the spirit.
              Two days into the journey, the thought of abandonig the journey
              came up.'''))
        action = input(dedent('''abandon journey, flee to another village for
                       safety, continue \n > '''))

        if action.lower() == "abandon journey":
            print('You lose, bye')
            exit(1)
        elif action.lower() == 'flee to another village for safety':
            print('you lose dear coward, bye')
            exit(1)
        elif action.lower() == 'continue':
            print("Ride on hero")
            return 'spirit'

class Spirit():

    def enter(self):
        print(dedent('''
              You meet a spirit guard and it ask you to turn back as human beings
              are not allowed into the land of the gods. You explained why it's
              necessary for you to enter but the spirit didn't leave. '''))

        action = input('sing with the flute, fight with it, sleep\n > ')

        if action.lower() == 'sing with the flute':
            print(dedent('''You sing a nice song and shortly the spirit dissapears
                  allowing you to proceed with the journey'''))
            return 'snake'
        elif action.lower() == 'fight with it':
            print(dedent('''You go to fight the spirit but can't touch the spirit.
                  it strikes ))you and you fall and die, end of game, \n you lose
                  '''))
            exit(1)
        elif action.lower() == 'sleep':
            print('You sleep and lose, game over')
            exit(1)
        else:
            print('Does not commute')
            return 'spirit'

class Snake():

    def enter(self):
        print(dedent('''You decide to rest along the way and sundenly a snake approaches
             you. You see it on time and decides to take an immidiate action'''))

        action = input('Hit the snake, blow the flute, run \n>')

        if action.lower() == 'hit the snake':
            print('Before you hit the snake, it bit you and the game ends, \n bye.')
            exit(1)
        elif action.lower() == 'blow the flute':
            print('You blow the game and the snake disappears, continue')
            return 'old_woman'
        elif action.lower() == 'run':
            print('You ran and something hit you. you fall and the snake bit you.')
            exit(1)
        else:
            print('chose right')
            return 'snake'

class Old_Woman():

    def enter(self):
        print(dedent('''On the way, an old woman appeared asking you to offer a
              sacrifice before you could continue your journey'''))

        action = input(dedent('''Blow the flute, run, offer an egg \n > '''))
        if action.lower() == 'Blow the flute':
            print('You blow the flute but the old woman refused to leave, retry')
            return 'king'
        elif action.lower() == 'run':
            print('You and fall and the spirit came again')
            return 'spirit'
        elif action.lower() == 'offer an egg':
            print('You offer her an egg and she lets you go, continue')
        else:
            print('Does not commute')
            return 'old_woman'

class King():

    def enter(self):
        print(dedent('''You reach the river and look around for the broken jar but
              you couldn't see it. The late king appeared, narrates the story of how
              he broke the jar because he never liked you. He begs for your
              forgiveness so he could finally rest as he has been waiting for this
              day. He apologises'''))

        action = input(dedent('forgive the king, cry and leave, slap the king\n> '''))

        if action.lower() == 'forgive the king':
            print('You forgive the king and he dissapears, the jaw appears and you take it.')
            return 'end'
        elif action.lower() == 'cry and leave':
            print(dedent('''You leave the king and he continues to wail. On your way,
                  you thought to return and save the kingdom'''))
            return 'journey'

class End():

    def enter(self):
        print(dedent('''You took the jaw and the kingdom was almost destroyed. You raised
              the jaw and the kingdom was saved, YOU WIN'''))


class Map(object):

    scenes = {
          'intro': Intro(),
          'journey': Journey(),
          'spirit': Spirit(),
          'snake': Snake(),
          'old_woman': Old_Woman(),
          'king': King(),
          'end': End()}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val


a_map = Map('intro') # sets start_scene to intro here
a_game = engine(a_map) # connects the map to the engine to proceed the game
a_game.play() # calls the play method
