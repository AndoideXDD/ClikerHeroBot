import keyboard
import pyautogui as pa 
import random
from time import sleep



contador_de_cliks_del_raton = 0

contador_de_cliks_del_raton_por_cada_100_cliks = 0

contador_de_cliks_del_raton_por_cada_1000_cliks = 0

ultimo_contador_lo_digo_en_serio = 4

empieza = False
 
#controla el volver a escenarios anteriores


       
while True:

	# If para hacer auto click 

	if keyboard.is_pressed(" ") or empieza == True:

		#Mata y recoje el oro y los monstruos
		
		pa.click(x = random.randint(765,1230), y = random.randint(449,587))
		contador_de_cliks_del_raton = contador_de_cliks_del_raton +1

		#Deja de ejecutar
		if keyboard.is_pressed("q"): 
			break
		if keyboard.is_pressed("m"):
			contador_de_cliks_del_raton = 0
			empieza = False
			continue

		if contador_de_cliks_del_raton < 5 or contador_de_cliks_del_raton > 95:

			 
			#Deja de ejecutar
			if keyboard.is_pressed("q"): 
				break
			if keyboard.is_pressed("m"):
				contador_de_cliks_del_raton = 0
				empieza = False
				continue
			#Mejora a los heroes
			pa.click(x=152, y=random.randint(273,518))

		if contador_de_cliks_del_raton == 100:
			#Deja de ejecutar
			if keyboard.is_pressed("q"): 
				break
			if keyboard.is_pressed("m"):
				contador_de_cliks_del_raton = 0
				empieza = False
				continue
			
			contador_de_cliks_del_raton = 0

			#Baja un poco la scroll bar

			pa.click(x=663, y=712)

			#Prueba a ver si hay otro scenario

			pa.click(1066,66)

			#Quitan anuncios estos dos clicks

			pa.click(x=1255, y=59)
			pa.click(x=1040, y=144)
			contador_de_cliks_del_raton_por_cada_100_cliks = contador_de_cliks_del_raton_por_cada_100_cliks + 1

		

			

		if contador_de_cliks_del_raton_por_cada_100_cliks == 10:

			contador_de_cliks_del_raton_por_cada_1000_cliks = contador_de_cliks_del_raton_por_cada_1000_cliks +1

			contador_de_cliks_del_raton_por_cada_100_cliks  = 0

			#sube la scroll bar 

			for x in range(100):
				pa.click(x=658, y=222)
				#Deja de ejecutar
				if keyboard.is_pressed("q"): 
					break
				if keyboard.is_pressed("m"):
					contador_de_cliks_del_raton = 0
					empieza = False
					continue

			#baja la scroll bar 

			for x in range(4+ultimo_contador_lo_digo_en_serio):
				pa.click(x=657, y=700)
				#Deja de ejecutar
				if keyboard.is_pressed("q"): 
					break
				if keyboard.is_pressed("m"):
					contador_de_cliks_del_raton = 0
					empieza = False
					continue
			#clika para mejorar a los heroes las habilidades 

			for x in range(20):

				pa.click(x = random.randint(266,514), y = random.randint(299, 372))
				#Deja de ejecutar
				if keyboard.is_pressed("q"): 
					break
				if keyboard.is_pressed("m"):
					contador_de_cliks_del_raton = 0
					empieza = False
					continue

			pa.click(x=853, y=72)


			#baja la scroll bar 

			for x in range(100):

				#Deja de ejecutar
				if keyboard.is_pressed("q"): 
					break
				if keyboard.is_pressed("m"):
					contador_de_cliks_del_raton = 0
					empieza = False
					continue

				pa.click(x=657, y=700)

		#Siempre y cuando este esta variable permitira que no tengas que pulsar espacio todo el rato

		empieza = True

		# Este sirve para mejorar todas las habilidades de los heroes en general

		if contador_de_cliks_del_raton_por_cada_1000_cliks == 2:
			ultimo_contador_lo_digo_en_serio = ultimo_contador_lo_digo_en_serio + 1
			contador_de_cliks_del_raton_por_cada_1000_cliks = 0

			sleep(60)
			#sube la scroll bar 

			for x in range(100):
				pa.click(x=658, y=222)

				#Deja de ejecutar
				if keyboard.is_pressed("q"): 
					break
				if keyboard.is_pressed("m"):
					contador_de_cliks_del_raton = 0
					empieza = False
					continue
			#baja la scroll bar 
			# aparte el ultimo_contador_lo_digo_en_serio sirve para que pasado muchos cliks deje de mejorar a los personajes demasiado costosos
			for x in range(ultimo_contador_lo_digo_en_serio):

				#Deja de ejecutar
				if keyboard.is_pressed("q"): 
					break
				if keyboard.is_pressed("m"):
					contador_de_cliks_del_raton = 0
					empieza = False
					continue

				pa.click(x=657, y=700)

			for n in range(10):
				if keyboard.is_pressed("q"): 
						break
				if keyboard.is_pressed("m"):
					contador_de_cliks_del_raton = 0
					empieza = False
					continue
				for x in range(20):

					
					#Deja de ejecutar
					if keyboard.is_pressed("q"): 
						break
					if keyboard.is_pressed("m"):
						contador_de_cliks_del_raton = 0
						empieza = False
						continue

					#Mejora a los heroes

					pa.click(x=164, y=282)
					pa.click(x = random.randint(266,514), y = random.randint(299, 372))

				#baja la scroll bar 

				for t in range(4):
					pa.click(x=657, y=700)

			pa.click(x=719, y=203)
			pa.click(x=721, y=262)
			pa.click(x=721, y=316)

	#Deja de ejecutar
	if keyboard.is_pressed("q"): 
		break
	if keyboard.is_pressed("m"):
		contador_de_cliks_del_raton = 0
		empieza = False
		continue

