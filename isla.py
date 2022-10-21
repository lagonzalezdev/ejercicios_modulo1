print("Bienvenido a la isla, tu misión será encontrar el tesoro")
print("Puedes ir acompañado de una mascota")
companero = input("¿deseas un compañero para tu viaje? responda si o no")

if companero == "si":
    animal=input("¿ que animal desea gato o loro?")
    if animal == "loro":
        print("el loro salio volando ahora estas perdido")
    elif animal == "gato":
        print("ho no es hora de la siesta dle gato pierdes un turno ")
elif companero == "no":
    catalejo=input("quieres buscar con el catalejo?")
    if catalejo == "si":
        print("encontraste el tesoro")
        print("ganaste")
    elif catalejo == "no":
        print("camina a ciegas caes en un hueco, game over")




    
     
     
        #print("oh no, es hora de la siesta del gato, pierdes un turno")

    
        # if animal ==  gato:
              #print("oh no, es hora de la siesta del gato, pierdes un turno")
           # if animal == loro:
                    #print ("el loro salió volando, ahora estas perdido, game over")