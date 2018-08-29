from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
	def enter(self):
		print("This is not a configured scene, use a subclass")
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene: #check if current scene is the ending
			next_scene_name = current_scene.enter() #enter current scene and get return value
			current_scene = self.scene_map.next_scene(next_scene_name) #use return value to update current scene

class Death(Scene):
	def enter(self):
		print("You are dead")
		exit(1)
		pass
class CentralCorridor(Scene):
	def enter(self):
		n = input("You enter the central corridor, Shoot, Dodge, or Tell Joke:")
		if n == "Shoot":
			return 'death'
		elif n == "Dodge":
			return 'death'
		elif n == "Tell Joke":
			return 'laser_weapon_armory'
		else:
			print("does not compute")
			return 'central_corridor'

class LaserWeaponArmory(Scene):
	def enter(self):
		print("You enter the laser weapon armory, you have 10 guesses for 3 digit code:")
		code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
		guess = input("[keypad]> ")
		guesses = 0
		print(f"The code is actually {code}")

		while guess != code and guesses < 10:
			print("WRONG")
			guesses += 1
			guess = input("[keypad]> ")

		if guess == code:
			print("You got the code correct")
			return 'the_bridge'
		else:
			print("you got the code wrong")
			return 'death'

class TheBridge(Scene):
	def enter(self):
		n = input("You enter the bridge, throw bomb or place bomb")
		if n == 'throw bomb':
			print("You threw the bomb and died")
			return 'death'
		elif n == 'place bomb':
			print("You place bomb and continue")
			return 'escape_pod'
		else:
			print("does not compute")
			return 'the_bridge'

class EscapePod(Scene):
	def enter(self):
		print("You enter the escape pod room")
		x = randint(1, 3) #generate random number 1, 2, or 3
		n = int(input("You choose a door from 1-3"))
		if n == x:
			print("You choose the correct door and escape")
			return 'finished'
		else:
			print("You choose the wrong door...")
			return 'death'

class Finished(Scene):
	def enter(self):
		print("You finish the game")
		return 'finished'


class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge' : TheBridge(),
		'escape_pod' : EscapePod(),
		'death' : Death(),
		'finished':Finished(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name) #return None if doesn't exist in dict
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()