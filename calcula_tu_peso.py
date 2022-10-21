gravedad_en_marte = 3.72
gravedad_en_la_tierra = 9.81
gravedad_en_neptuno = 11.15

peso_en_la_tierra = float(input("Ingrese su peso"))
tu_peso_en_marte_es = (peso_en_la_tierra/gravedad_en_la_tierra)*gravedad_en_marte
tu_peso_en_neptuno_es = (peso_en_la_tierra/gravedad_en_la_tierra)*gravedad_en_neptuno
#print("{:.1f}"("Tu peso en marte es ", tu_peso_en_marte_es))
#print("Tu peso en neptuno es ", tu_peso_en_neptuno_es)
print("Tu peso en marte es {:.1f}".format(tu_peso_en_marte_es))
print("Tu peso en neptuno es {:.1f}".format(tu_peso_en_neptuno_es))
 
