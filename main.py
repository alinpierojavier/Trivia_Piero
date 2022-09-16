#Importación de las librerias a usar

import time # Libreria de veces o tiempo
import random  #Libreria random
import os #Libreria para limpiar las pantallas 

###CONSTANTES DE COLORES
RED = '\033[31m'
GREEN = '\033[32m'
PURPLE = '\033[0;95m'
RESET = '\033[0m'
#COLORES CON NEGRITA
B_RED = "\033[1;31m" 
B_GREEN = "\033[1;32m"  
B_YELLOW = "\033[1;33m" 
B_BLUE = "\033[1;34m" 
B_PURPLE = "\033[1;35m"  
B_CYAN = "\033[1;36m" 

#COLORES CON SUBRAYADO
URED = "\033[4;31m" 
UGREEN = "\033[4;32m"  
UYELLOW = "\033[4;33m" 
UBLUE = "\033[4;34m"  

#COLORES CON BACKGROUND
BG_CYAN = "\033[0;106m"  # Cyan
####FIN DE CONSTANTES#####

###VARIABLES DEFINIDAS

#Inicio del puntaje: 0
puntaje = 0  
#Condicional para descubrir la palabra secreta
isFoundSecret = False  

 #Repetir trivia
iniciarTrivia = True 

 #Nro de intentos de trivia
intentos = 1 

#Guarda el puntaje que se realiza en cada intento
listaPuntajeIntentos=[] 

#os.name (define el sistema operativo), var es la palabra para limpiar pantalla 
if os.name == "posix":
	#Limpiamos
   var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"


####FUNCIONES PRINCIPALES ############
	
#-----Validación
def validacionRpta(nroPregunta=0):
    # Almacenamos la respuesta del usuario en la variable "respuesta"
    respuesta = input(UBLUE + B_BLUE + "\n tu respuesta:" + RESET + RESET + " ")
    while respuesta.lower() not in ("a", "b", "c", "d", "futbul", "musica"):
        respuesta = input("** * Debes responder a, b, c o d.** ** \n Ingresa nuevamente tu respuesta: ")
    #Esta es la palabra secreta, solo se descubre 1 vez
    if (respuesta == "musica"):
			#para usar variable global
        global isFoundSecret 
        if (isFoundSecret):
            print("Respuesta repetida!, Responde la pregunta")
        else:
            print(B_GREEN+"¡Vingo!, Obtienes 100 puntos por acertar"+RESET)
            global puntaje
            puntaje += 1000 #suma 1000 puntos si se descubre palabra
            print(B_RED+"\n******Ey! Aún tienes que responder la pregunta.******"+RESET)
            isFoundSecret = True
        respuesta = validacionRpta(nroPregunta)
    #Esta es una palabra que se menciona si responde "no" en la pregunta random es una ayuda para el jugador, (solo funciona en la pregunta 2)
    if respuesta == "futbul" and nroPregunta == 2:
        print("****-> Todo sea por disfrutar el juego, Tip: La respuesta esta en tu"+B_RED+ " MENTE"+RESET +"GO!")
        respuesta = validacionRpta()
    elif respuesta == "futbol":
        print("****-> Ey! aunque sí es talento puro, pero esta no es la pregunta con ayuda. ¡You can do it!.")
        respuesta = validacionRpta()
    return respuesta.lower()

#PARA MOSTRAR EL MENSAJE ACTUAL
def mostrarPuntajeActual(user, puntaje):
    print(B_YELLOW +
          "\n=========================================================")
    print("||", user, "tu puntaje actual es de:", puntaje, "puntos ||")
    print("=========================================================" + RESET)


#PARA IMPRIMIR LAS OPCIONES DE RESPUESTA
def printOpciones(listaOpciones):
    alternativas = ["a", "b", "c", "d"]
    for alt, opcion in zip(alternativas, listaOpciones):
        print("\t" + alt + ") " + opcion)


#####FIN DE FUNCIONES#################

#######COMIENZO DEL PROGRAMA EN CONSOLA
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(B_YELLOW + "★★★★★" + GREEN + " Bienvenido a mi trivia sobre el DEPORTE" + RESET + B_YELLOW + " ★★★★★" + RESET)

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
user = input("\nHola!, ¿Puedes decirme tu nombre?:\n ")
user = user.capitalize()  #El primer caracter se pone en mayuscula
print(f"{PURPLE} \u261E Bueno {user},el día de hoy pondremos a prueba tus conocimientos en el Deporte\n {RESET}")

# Es importante dar instrucciones sobre cómo jugar:
print(GREEN + "=====================================================")
print("|| INDICACIONES:                                   ||")
print("|| 1. Para contestar la pregunta debes escribir    ||")
print("||    la letra de la alternativa y presionar ENTER ||")
print("|| 2. Cada respuesta correcta se te sumará puntos  ||")
print("|| 3. Cada respuesta incorrecta se restará puntos  ||")
print("|| OJO: No hay derecho a reclamos una vez iniciado ||")
print("=====================================================" + RESET)

#Bucle de trivia si se repite
while iniciarTrivia:
    ##PREGUNTA RANDOM: Que otorga una pista en la primera pregunta, si responde sobre el futbol
    print("\nAntes de comenzar, tengo una pregunta importante que hacerte:")
    pregunta_random = input(B_BLUE +"¿Eres un fanatico del futbol?[si/no]: " + RESET)
    if (pregunta_random.lower() == "si"):
        print( GREEN +"\n¡Yo también!, te regalaré una pista de la primera pregunta porque en esta trivia amamos el deporte y quienes aman el deporte \n" + RESET + B_RED + "PISTA: Son menos de 34" + RESET)
    elif (pregunta_random.lower() == "no"):
        print(B_CYAN + "\nOh no! entonces este no será una trivia muy fácil para ti :c. \n" + RESET + B_GREEN + "TIP: Intenta escribir 'futbol' en alguna pregunta puede que haya una ayuda para ti" + RESET)
    else:
        print(RED + "\n*** Que pena! Parece que no nos estamos entendiendo, debiste escribir: si o no. Tienes 3 puntos menos por no obedecer! ¡Intentalo nuevamente!***" + RESET)
        puntaje = -3
      
    #-----Pausa o espera----------
    time.sleep(2)
    #--------Mensaje de inicio y # de intentos---------
    print( B_PURPLE + "\n Vamos a hacerlo," + user + " con tu " + RESET + B_BLUE + "intento número ", intentos, "\n" + RESET)
    time.sleep(2)
    #--Inicio de puntaje random--
    puntaje += random.randint(0, 30)
    #--Mostrar puntaje actual--
    print(B_GREEN + "=========================================")
    print("[ Inicias con:", puntaje, "Puntos     ]")
    print("=========================================" + RESET)

    print(UYELLOW + "\n★★★★★" + RESET + UGREEN + " Trivia sobre Deporte" +
          RESET + UYELLOW + " ★★★★★\n" + RESET)
    #---------PANTALLA DE CARGA CON UN LOOP FOR - DESAFIO CICLOS----
    print(B_BLUE + "Cargando la trivia.")
    for x in range(5, 0, -1):
        print(x)
        time.sleep(1)
    print(RESET + B_GREEN + "\nTrivia lista!\n" + RESET)
    
    #------------------PREGUNTA N° 1-----------------------
    valorRandom = random.randint(6, 15)
    print(f"{BG_CYAN}->PREGUNTA 1:{RESET} {URED}({valorRandom} puntos si es correcta o -{valorRandom} si es incorrecta){RESET}")
    print("1)¿Qué judador de fútbol es el mayor con los Balones de Oro?")
    #--------Funcion que imprime las opciones desde laa lista-------
                    #a     b     c    d
    printOpciones(["Leonel Messi", "Michael Platini", "Cristiano Ronaldo", "Johan Cruyff"])
    #------Validar la respuesta que está en el rango de [a,b,c,d]
    respuesta_1 = validacionRpta()
    if (respuesta_1 == "a"):
        print(B_GREEN, "Bien hecho", user,
            "! Leonel Messi es Argentino, ex jugador del Barcelona y actualmente estrella en el PSG. Tiene 7 Balones de Oro. ", RESET)
        puntaje += valorRandom
    else:
        print(B_RED, user, "Tu respuesta es incorrecta!....Vuelva intentarlo", RESET)
        puntaje -= valorRandom

    #------Mostrar puntaje actual--------
    mostrarPuntajeActual(user, puntaje)
    ##----Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ####### Pregunta 2
    valorRandom = random.randint(9, 20)
    print(f"{BG_CYAN}\n->PREGUNTA 2:{RESET} {URED}({valorRandom} puntos si es correcta o -{valorRandom} si es incorrecta){RESET}")
    print("\n2) ¿Cantante favorito de Leonel Messi?")
    #Funcion que imprime las opciones desde una lista
                    #a     b     c    d
    printOpciones(["Budbunny", "Shakira", "Coldplay", "Enrique_Iglesias"])

    #------Validación de que la respuesta se encuentre en el rango------- de [a,b,c,d]
    respuesta_2 = validacionRpta(2)
    if (respuesta_2 == "c"):
        print(B_GREEN, "Es CORRECTO", user,". En sus ratos libres, o cuando está con día libre le gusta ir al concierto de ColdPlay", RESET)
        puntaje += valorRandom
    else:
        print(B_RED, user, "Tu respuesta es incorrecta!....Vuelva intentarlo", RESET)
        puntaje -= valorRandom
    #Mostrar puntaje actual
    mostrarPuntajeActual(user, puntaje)
    ##Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ####### Pregunta 3
    valorRandom = random.randint(5, 13)
    print(f"{BG_CYAN}\n->PREGUNTA 3:{RESET} {URED}({valorRandom} puntos si es correcta o -{valorRandom} si es incorrecta){RESET}")
    print("\n3) Sí a Leonel Messi le asocia con la música¿Quién es la esposa de su mejor amigo?")
    #Funcion que imprime las opciones desde una lista
                    #a     b     c    d
    printOpciones(["Riana", "Madona", "Carol G", "Shakira"])

    ##Validación de que la respuesta se encuentre en el rango de [a,b,c,d]
    respuesta_3 = validacionRpta()
    if (respuesta_3 == "a"):
        print(B_RED, "Incorrecto!", user,'La cantante es Colombiana, quizá ya te ayudé en algo',RESET)
        puntaje -= valorRandom
    elif respuesta_3 == "b":
        print(B_RED, "Incorrecto!", user, "Su pareja es español y juega en el Barcelona",RESET)
        puntaje -= valorRandom
    elif respuesta_3 == "c":
        print(B_RED, "Incorrecto!", user, "Su equipo le llaman Culé" + RESET)
        puntaje -= valorRandom
    else:
        print(B_GREEN, "Bien hecho", user,"! Ella es Shakira y en el mundial 2010 a sido la afortunada en Cantarla",RESET)
        puntaje += valorRandom
    #Mostrar puntaje actual
    mostrarPuntajeActual(user, puntaje)
    ##Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ####### Pregunta 4
    #La puntuación de esta pregunta será dependiendo de la que se elija asi pruebo lo de usar OPERADORES MATEMATICOS (DESAFIO)
    print(f"{BG_CYAN}\n->PREGUNTA 4:{RESET} {URED}El puntaje de esta pregunta dependerá de la respuesta que elijas. Elige sabiamente.{RESET}")
    print("\n4) ¿Con qué pie juega mas Leonel Messi?")
    #Funcion que imprime las opciones desde una lista
                    #a     b     c    d
    printOpciones(["ninguna", "ambos", "zurdo", "derecha"])

    ##Validación de que la respuesta se encuentre en el rango de [a,b,c,d]
    respuesta_4 = validacionRpta()
    if (respuesta_4 == "a"):
        print(B_YELLOW, "Es incorrecto, pero tendría algo de sentido.", user, "por tu creatividad de elección te doy 5 puntos", RESET)
        puntaje += 5
    elif (respuesta_4 == "b"):
        print(B_RED, "En serio", user,"? Tu respuesta es incorrecta, pero soy buena onda, solo te restaré 5 puntos",RESET)
        puntaje -= 5
    elif (respuesta_4 == "c"):
        print(B_GREEN, "Totalmente Correcto", user,". Messi es un jugador zurdo de nacimiento, el cual viene con ese don de ser Futbolista, se ha formado en el Rosario de Argentina y posteriormente fue fichado al Barchelona con solo 12 años de edad. [Te multiplicaremos tu puntaje]",RESET)
        puntaje *= 2
    else:
        print(B_RED,"Por qué serían ambos? has fallado en tu respuesta :(, dividiremos tu puntaje a la mitad.",RESET)
        puntaje /= 2

    #Mostrar puntaje actual
    mostrarPuntajeActual(user, puntaje)
    ##Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ####### Pregunta 5
    valorRandom = random.randint(3, 10)
    print(f"{BG_CYAN}\n->PREGUNTA 5:{RESET} {URED}({valorRandom} puntos si es correcta o -{valorRandom} si es incorrecta){RESET}")
  
    print("\n5) ¿Cómo se llama la esposa de Leonel Messi?")
    #Funcion que imprime las opciones desde una lista
                    #a     b     c    d
    printOpciones(["Shakira", "Antonella Rocuss", "Daniela", "simoneta"])

    ##Validación de que la respuesta se encuentre en el rango de [a,b,c,d]
    respuesta_5 = validacionRpta()
    if (respuesta_5 == "b"):
        print(B_GREEN,"Correcto!. Antonella y Messi fueron mejores amigos de la infancia.",RESET)
        puntaje += valorRandom
    else:
        print(B_RED, "Incorrecto!", user," Además ellos fueron separandos un tiempo, años mas tarde se reencontrario y fueron novios, despues se casarony hoy en día son Esposos", RESET)
        puntaje -= valorRandom
    #Mostrar puntaje actual
    mostrarPuntajeActual(user, puntaje)
    ##Tiempo de espera para que pueda ver resultados y respuestas
    time.sleep(2)

    ###RESULTADOS
    print(UGREEN + "\nRESULTADOS: " + RESET)
    ##RULETA DE PUNTAJE FINAL - MODIFICA EL PUNTAJE POR UN JUEGO DE AZAR
    azar = input( "Ey! Antes de mostrarte tus resultados. ¿Te gustaria un juego al azar con tus puntos?[Si/No]: ")
    if (azar.lower() == "si"):
        print(B_BLUE + "¡Perfecto! Se nota que no le temes a los retos" + RESET)
        ##Vamos a darle 5 opciones  de puntajes que podria sumar o restar
        opcionesNum = []
        print("Elige cuanto quieres ganar o perder...: ")
        for i in range(1, 6, 1):
            numRandom = random.randint(20, 400)
            print(i, ")", numRandom)
            opcionesNum.append(numRandom)
        indiceNum = int(input("Elija una opcion: "))
        indiceNum -= 1
        while (indiceNum >= len(opcionesNum)):
            print("Estas fuera de Rango [1-5]")
            indiceNum = int(input("Elija una opcion: "))
            indiceNum -= 1
        numRandom = opcionesNum[indiceNum]
        time.sleep(2)
        print(B_GREEN + "**** Podrias sumar", numRandom,"puntos o podrias restarle", numRandom,"a tu puntaje ****" + RESET)
        print("Que los dioses de Trivia decian tu caso!")
        #Si el numero que elige el usuario es el mismo al del random se suma
        numeroEleccionUsuario = int(input("Elige [1 o 2]: "))
        resultado = random.randint(1, 3)
        ####FOR -LOOP DEL DESAFIO DE CICLOS.
        print("Resultado en: ")
        for x in range(3, 0, -1):
            print(x)
            time.sleep(1)
        if resultado == numeroEleccionUsuario:
            print(B_BLUE + "Genial! Tienes mucha suerte se te sumaran", numRandom, "puntos" + RESET)
            puntaje += numRandom
        else:
            print(B_RED + "Vaya suerte la tuya. Por desgracia se restaran", numRandom, "puntos" + RESET)
            puntaje -= numRandom
    elif (azar.lower() == "no"):
        print(UYELLOW + "Oh! has perdido puntos :(." + RESET)
    else:
        print(URED + "No nos estamos entendiendo :c, era escribir si o no." + RESET)

    print(UBLUE + B_BLUE + "\nObtuviste", puntaje, "puntos.", end=" ")
    ###Resultados segun pregunta random
    if (pregunta_random == "si" and puntaje <= 10):
        print("Esperaba más de un fanático del deporte.")
    elif (pregunta_random == "si" and puntaje >= 40):
        print("Realemente eres un gran fanático del deporte.")
    elif pregunta_random == "si":
        print("Bien hecho eres un fanático promedio.")

    #Resultados para los que contestaron "no" o si escribieron cualquier cosa
    if (pregunta_random != "si" and puntaje <= 10):
        print("Bueno al menos aprendiste algo nuevo sobre el futbolista.")
    elif (pregunta_random != "si" and puntaje >= 40):
        print("¿Estas seguro que no eres un fanático del fútbul?.")
    elif pregunta_random != "si":
        print("Eso no estuvo mal para no saber mucho sobre el Fútbol.")

    ##PREGUNTA SI EL USUARIO QUIERE JUGAR DE NUEVO PUNTAJE VUELVE A 0
    print(RESET + B_YELLOW + UYELLOW +
          "\n¿Deseas intentar la trivia nuevamente?" + RESET)
    repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
    listaPuntajeIntentos.append(puntaje)
    puntaje = 0
    intentos += 1
    isFoundSecret = False ##Retorna a false porque al ser nuevo intento puede escribirla de nuevo
    time.sleep(2)
    os.system(var)
    if repetir_trivia != "si": 
        print(f"{UGREEN}\nEspero {user} que lo hayas pasado bien, hasta pronto!{RESET}")
        #RESUMEN DEL JUEGO CON LOS INTENTOS, SU PUNTAJE Y SUMA DE ESTOOS
        print(B_YELLOW+UYELLOW+"RESUMEN DE JUEGO:"+RESET)
        for puntos in listaPuntajeIntentos:
          print("-> Intento",(listaPuntajeIntentos.index(puntos)+1),":",puntos,"puntos")
        print(B_BLUE,"Puntaje total:",RESET,sum(listaPuntajeIntentos),"puntos")
        iniciarTrivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
			
        print(UGREEN+"¡Gracias por jugar, hasta la otra oportunidad!" + RESET)