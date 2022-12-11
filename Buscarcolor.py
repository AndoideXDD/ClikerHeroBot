 
import PIL 
import keyboard
import pyautogui as pa
import random
import keyboard
from time import sleep
import keyboard
import pyautogui as pa 
import random
from time import sleep

empieza = False

conjuntoDeColores = []

while True:

	if keyboard.is_pressed("w") or empieza == True:

		empieza = True

		px = PIL.ImageGrab.grab().load()
		color = px[pa.position()]
		print(color)
		print(pa.position(0))

	if keyboard.is_pressed("q"): 
		break   



	if keyboard.is_pressed("n"): 
		empieza = False
