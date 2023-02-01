#Importem les llibreries, primer sha de fer el pip install pygame i el random
import pygame
import random
import sys

import json

with open("variables.json", "r") as f:
    variables = json.load(f)

#Per importar algo de variables variables["monster"]["ataque"]

#Iniciem el joc, i creem una pantalla
pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("o Jogo do Ganso")

#Variables que es poden modificar a la partida pero surten d'un valor sempre igual (json)
#para modificar los valores con los que empiezas el turno
vida_jugador_partida = variables["vida_jugador"]
armadura_jugador_partida = variables["armadura_jugador"]
max_energia_jugador_partida = variables["max_energia_jugador"]
numero_cartas_partida = variables["numero_cartas"]
ataque_jugador_partida = variables["ataque_jugador"]

#FINS AQUI LA COSA ESTA BE












#Creem un bucle per utilitzar els eventos i les variables del joc
juego_en_curso = True
while juego_en_curso:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego_en_curso = False

    # Seleccionar una carta al azar
    carta_seleccionada = random.choice(cartas)

    # Verificar si el jugador tiene suficiente energía para usar la carta
    if energia_jugador >= carta_seleccionada["costo_energia"]:
        energia_jugador -= carta_seleccionada["costo_energia"]
        armadura_jugador -= carta_seleccionada["ataque"]

        # Verificar si el monstruo muere
        if armadura_jugador <= 0:
            vida_monstruo -= carta_seleccionada["ataque"]
            if vida_monstruo <= 0:
                print("Has ganado el juego!")
                juego_en_curso = False
    else:
        print("No tienes suficiente energía para usar esta carta.")

    # Recargar energía al iniciar el turno
    energia_jugador += 10

    # Actualizar la pantalla
pygame.display
#Que es vegi la informació en pantalla

# Mostrar la vida y la energía del jugador
fuente = pygame.font.Font(None, 30)
texto = fuente.render("Vida: {}   Armadura: {}   Energía: {}".format(vida_jugador, armadura_jugador, energia_jugador), True, (255, 255, 255))
ventana.blit(texto, (10, 10))

    # Mostrar la vida del monstruo enemigo
texto = fuente.render("Vida monstruo: {}".format(vida_monstruo), True, (255, 255, 255))
ventana.blit(texto, (10, 50))


#Manera de acabar el joc
if vida_jugador <= 0:
        print("Has perdido el juego!")
        juego_en_curso = False

#Alifnla del bucle principal sha de posar aixo per actualitzar
pygame.display.update()

#FINS AQUI ES REVISABLE DEL QUE ES INTERESSANT I QUE NO












#Per repartir les cartes al principi de cada torn
mano_jugador = random.sample(variables["cartas"], numero_cartas_partida)

#Per dibuixar els rectangles de les cartes
for i, carta in enumerate(mano_jugador):
    pygame.draw.rect(ventana, (255, 255, 255), (10, 100 + i * 50, 150, 40))
    texto = fuente.render("{} (Coste: {})".format(carta["nombre"], carta["energia"]), True, (0, 0, 0))
    ventana.blit(texto, (15, 105 + i * 50))
#Aixo es pot afegir directament al bucle del joc
#Comprovar si cliquem una carta
if event.type == pygame.MOUSEBUTTONDOWN:
    x, y = event.pos
    for i, carta in enumerate(mano_jugador):
        if x > 10 and x < 160 and y > 100 + i * 50 and y < 140 + i * 50:
            if energia_jugador >= carta["energia"]:
                # Restar energía
                energia_jugador -= carta["coste"]
                # Aplicar efectos de la carta (atacar o aumentar defensa)
                if "dano" in carta:
                    vida_monstruo -= carta["ataque"]
                if "defensa" in carta:
                    armadura_jugador += carta["defensa"]
                # Eliminar la carta de la mano
                mano_jugador.remove(carta)

#ESTA BE; ES PER AFEGIR CARTES DE MANERA ALEATORIA A LA MA














#Per afegir els torns
turno_actual = "jugador"

# Bucle principal del juego
while True:
    energia_jugador = max_energia_jugador_partida
    armadura_jugador = armadura_jugador_partida

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego_en_curso = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if turno_actual == "jugador":
                # Comprobar si se ha hecho click en una carta
                for i, carta in enumerate(mano_jugador):
                    if x > 10 and x < 160 and y > 100 + i * 50 and y < 140 + i * 50:
                        if energia_jugador >= carta["energia"]:
                            # Restar energía
                            energia_jugador -= carta["energia"]
                            # Aplicar efectos de la carta (atacar o aumentar defensa)
                            if "ataque" in carta:
                                vida_monstruo -= (carta["ataque"] + ataque_jugador)
                            if "defensa" in carta:
                                armadura_jugador += carta["defensa"]
                            if "bufo" in carta:
                                ataque_jugador_partida += 5
                            if "robar"
                            if "bufo_monstruo"
                            # Eliminar la carta de la mano
                            mano_jugador.remove(carta)
                # Comprobar si se ha hecho click en "Acabar turno"
                if x > 10 and x < 160 and y > 10 and y < 50:
                    turno_actual = "monstruo"
                    # Recargar energía del jugador
                    energia_jugador = max_energia
                    # Repartir cartas al principio del turno
                    mano_jugador = random.sample(cartas, numero_cartas_mano)
            elif turno_actual == "monstruo":
                # El monstruo ataca
                vida_jugador -= ataque_monstruo
                # Comprobar si el monstruo ha acabado con la armadura del jugador
                if vida_jugador <= 0 and armadura_jugador > 0:
                    armadura_jugador = 0
                # Comprobar si el jugador ha perdido
                if vida_jugador <= 0:
                    print("Has perdido!")
                    pygame.quit()
                    sys.exit()
                turno_actual = "jugador"

#BUCLE DEL JOC PRINCIPAL, SHA DANAR POSANT TOTS ELS EVENTOS AQUI, ACABAR DE MODIFICAR LO DE TREURE LA VIDA ALS MONSTRES, AFAGIR BE LO DELS TORNS I LO DELS MONSTRES









 #Per posar musica he de fer aquest scrip
'''
 import pygame

pygame.init()
pygame.mixer.init()

# Carga la música
pygame.mixer.music.load("music.mp3")

# Reproduce la música en un bucle
pygame.mixer.music.play(-1)

# El resto del código aquí

# Termina Pygame
pygame.quit()
 '''
 
 
 
 
 
 
 
 
 
#Molt interessant pero per afegirho cap al late, quan en si el joc funcioni, poder es pot posar opcions de volum, mida de la campanya, o escullir quin jugador vols ser, etc etc 
#MOLT INTERESSANT PER VEURE LA ESTRUCTURA SENCERA DUN BUCLE
#Per generar un menu i poder interaccionar amb ell
'''
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

# Define los colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# Define las opciones del menú principal
main_menu_options = ["Jugar", "Opciones", "Salir"]

# Define las opciones del menú de opciones
options_menu_options = ["Volumen", "Resolución", "Volver"]

# Indica qué menú se está mostrando actualmente
current_menu = "main"

# Configura la fuente y el tamaño de los títulos de los menús
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Obtiene la posición del ratón
            mouse_pos = pygame.mouse.get_pos()
            # Verifica si se hizo clic en alguna opción
            if current_menu == "main":
                for i, option in enumerate(main_menu_options):
                    text = font.render(option, True, white)
                    text_rect = text.get_rect()
                    text_rect.center = (200, 100 + i * 50)
                    if text_rect.collidepoint(mouse_pos):
                        # Si se hizo clic en la opción "Opciones", cambia al menú de opciones
                        if option == "Opciones":
                            current_menu = "options"
                        # Si se hizo clic en la opción "Salir", termina el juego
                        elif option == "Salir":
                            running = False
            elif current_menu == "options":
                for i, option in enumerate(options_menu_options):
                    text = font.render(option, True, white)
                    text_rect = text.get_rect()
                    text_rect.center = (200, 100 + i * 50)
                    if text_rect.collidepoint(mouse_pos):
                        # Si se hizo clic en la opción "Volver", regresa al menú principal
                        if option == "Volver":
                            current_menu = "main"

    # Limpia la pantalla
    screen.fill(black)

    # Dibuja las opciones del menú actual
    if current_menu == "main":
        for i, option in enumerate(main_menu_options):
            text = font.render(option, True, white)
            screen.blit(text, (200, 100 + i * 50))
    elif current_menu == "options":
        for i, option in enumerate(options_menu_options):
            text = font.render(option, True, white)
            screen.blit(text, (200, 100 + i * 50))

    # Actualiza la pantalla
    pygame.display.update()

# Termina Pygame
pygame.quit()
'''









#EASY PERO SHA DEVEURE ON ES POSA EXACTAMENT
#Para esojer un monstruo aleatorio
'''
#primer va lo de llegir el archiu json pero ja esta posat
# Obtenemos una lista de monstruos del archivo
monsters = variables["monsters"]

# Seleccionamos un monstruo al azar de la lista
monster = random.choice(monsters)

# Obtenemos la información del monstruo seleccionado
monster_name = monster["name"]
monster_health = monster["health"]
monster_attack = monster["attack"]
'''









#Cosas sobre els eventos
'''

#Es crea una funció evento personalitzat per diferents coses
# Define un evento personalizado para cambiar de nivel
LEVEL_CHANGE_EVENT = pygame.USEREVENT + 1

# Define un evento personalizado para jugar un sonido de efecto
SOUND_EFFECT_EVENT = pygame.USEREVENT + 2

#Despres dintre el bucle principal del joc, processa els eventos
running = True

# Bucle principal del juego
while running:
    # Procesa los eventos en la cola de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                # Genera un evento personalizado para jugar un sonido de efecto
                pygame.event.post(pygame.event.Event(SOUND_EFFECT_EVENT))
        elif event.type == LEVEL_CHANGE_EVENT:
            # Procesa el evento personalizado para cambiar de nivel
            print("Cambiando de nivel...")
        elif event.type == SOUND_EFFECT_EVENT:
            # Procesa el evento personalizado para jugar un sonido de efecto
            print("Reproduciendo sonido de efecto...")
            '''