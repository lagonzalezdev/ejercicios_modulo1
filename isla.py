#algoritmo isla del tesoro - lagonzalezdev
print("Bienvenido a la isla, tu misión será encontrar el tesoro")
print("Puedes ir acompañado de una mascota")
companero = input("¿deseas un compañero para tu viaje? responda si o no")
if companero == "si":
    animal=input("¿qué animal desea gato o loro?")
    if animal == "loro":
        print("el loro salió volando ahora estas perdido")
    elif animal == "gato":
        print("oh no! Es hora de la siesta del gato pierdes un turno")
    import time
    time.sleep (2)
    print ("el gato ha despertado, es hora de continuar la busqueda")
decision=input("que camino tomar, ¿derecha o izquierda?")
if decision == "derecha":
    print ("oh no! Caiste en arenas movedizas")
    print ("Game over")
elif decision == "izquierda":
    print ("Encontraste el tesoro")
    print ("Haz ganado!!")
elif companero == "no":
    catalejo=input("quieres buscar con el catalejo?")
    if catalejo == "si":
        print("encontraste el tesoro")
        print("ganaste")
    elif catalejo == "no":
        print("camina a ciegas caes en un hueco, game over")
        