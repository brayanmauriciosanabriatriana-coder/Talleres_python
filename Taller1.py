#ejercicio 1 salario 
salario = 1500000
retencion = float(salario * 0.18)
bonificacion = float(salario * 0.013)
total = salario - retencion + bonificacion
print(f"El salario es: {salario} su retencion es: {retencion} y su bonificacion es: {bonificacion} y su total {total:,}")
#ejercicio 2 cancha 
area_cancha = 135
aumento_cancha = float(area_cancha * 0.20)
total_cancha = area_cancha + aumento_cancha
print(f"el area de la cancha es de:{area_cancha} y su aumento es de: {aumento_cancha} y su total es de: {total_cancha}")
# ejercicio 3 ibague desempleo 
desempleo_ibague = 10
aumento_desempleo = float(desempleo_ibague * 0.095)
disminucion_desempleo = float(desempleo_ibague * 0.015)
total_desempleo = desempleo_ibague + aumento_desempleo - disminucion_desempleo
print("el desempleo en ibague es :",desempleo_ibague,"el aumento es de :",aumento_desempleo,"la disminicion es de :",disminucion_desempleo,"su total es:", total_desempleo)

# ejercicio 4 area terreno  
area_inicial=1000
area_reducida=float(area_inicial*0.10)
area_adicional=float(area_inicial*0.50)
area_final=area_inicial-area_reducida+area_adicional
print("el area inicial es :",area_inicial,"el area reducida es :",area_reducida,"el area adicional es :",area_adicional,"el area final es :",area_final)
# ejercicio 5  minutos 
minutos = int(input("Ingrese la cantidad de minutos: "))
horas = minutos // 60
min_restantes = minutos % 60
print(f"{minutos} minutos equivalen a {horas} horas y {min_restantes} minutos.")

# ejercicio 6 horas a minutos 
horas= int(input("ingrese una hora:"))
minutos=horas*60
print(f"{horas} horas equivalen a {minutos} minutos.")

# ejercicio 7 quintal 
quintales = float(input("Ingrese la cantidad de quintales: "))
kilogramos = quintales * 100
print(f"\n{quintales} quintal(es) equivalen a {kilogramos} kilogramos.")
#ejercicio #10
#se calcula el tiempo y la disntacia
tiempo_dia1=float(input("cuantos minutos duro el entrenamiento? ")) 
distancia_dia1=float(input("cual fue la distancia recorridea durante el entreanmiento en metros? "))

tiempo_dia2=float(input("cuantos minutos duro el entrenamiento? ")) 
distancia_dia2=float(input("cual fue la distancia recorridea durante el entreanmiento en metros? "))

tiempo_dia3=float(input("cuantos minutos duro el entrenamiento? ")) 
distancia_dia3=float(input("cual fue la distancia recorridea durante el entreanmiento en metros? "))

#se sacan los totales

total_final_tiempo = tiempo_dia1 + tiempo_dia2 + tiempo_dia3
total_final_disntacia = distancia_dia1 + distancia_dia2 + distancia_dia3

promedio=total_final_disntacia / total_final_tiempo

print(f"en la semana entrenaste {total_final_tiempo} minutos y recorriste {total_final_disntacia} metros. Tu promedio semanal fue: {promedio} m/min")



#ejercicio #11
herencia=float(input("ingrese el valor de la herencia: "))
#el enunciado tiene valores incorrectos porque al sumar los porcentajes da mas del 100%
esposa= 0.40
hijo1=0.30
hijo2=0.20
hijo3=0.40
hijo4=0.10
total_esposa= herencia * esposa
total_hijo1= herencia * hijo1
total_hijo2= herencia * hijo2
total_hijo3= herencia * hijo3
total_hijo4= herencia * hijo4
print(f"a cada cada persona le corresponde: \n esposa: {total_esposa} \n hijo 1: {total_hijo1}\n hijo 2: {total_hijo2}\n hijo 3:{total_hijo3}\n hijo 4: {total_hijo4}")



#ejercicio #13
area_total_lote=float(input("ingrese el area total del lote:  "))

area_cultivos= area_total_lote * 0.40
area_vivienda= area_total_lote * 0.25
area_zonas_verdes = area_total_lote * 0.15

#al area total del lote se le resta la suma de las areas anteriores

area_disponible= area_total_lote - (area_cultivos + area_vivienda + area_zonas_verdes)
print(f"el area disponible para cultivos es de: {area_cultivos} m² \n el area disponible para vivienda es: {area_vivienda} m² \n el area disponible para zonas verdes es de: {area_zonas_verdes} m² ")
print(f"el area disponible para otros proyectos es: {area_disponible}")


#ejercicio #14
 
taller1 = float(input("Ingrese la nota del Taller 1: "))
taller2 = float(input("Ingrese la nota del Taller 2: "))

#promedio de los talleres
nota_1 = (taller1 + taller2) / 2

evaluacion1 = float(input("Ingrese la nota de la Evaluación 1: "))
evaluacion2 = float(input("Ingrese la nota de la Evaluación 2: "))
evaluacion3 = float(input("Ingrese la nota de la Evaluación 3: "))

#promedio de evaluaciones
nota_2 = (evaluacion1 + evaluacion2 + evaluacion3) / 3

nota_3 = float(input("Ingrese la nota del trabajo final: "))

quiz1 = float(input("Ingrese la nota del Quiz 1: "))
quiz2 = float(input("Ingrese la nota del Quiz 2: "))
quiz3 = float(input("Ingrese la nota del Quiz 3: "))
quiz4 = float(input("Ingrese la nota del Quiz 4: "))

nota_4 = (quiz1 + quiz2 + quiz3 + quiz4) / 4

#se calcula el porcentaje de las notas
ponderacion_1 = nota_1 * 0.15
ponderacion_2 = nota_2 * 0.30
ponderacion_3 = nota_3 * 0.30
ponderacion_4 = nota_4 * 0.25

nota_definitiva = ponderacion_1 + ponderacion_2 + ponderacion_3 + ponderacion_4

print(f"la nota definitiva es: {nota_definitiva:.1f}")






#ejercicio #15
#asignaos el valor del pasaje
valor_pasaje= 3000
inicio_dia=int(input("ingrese el número de la registradora al iniciar el día: "))
final_dia=int(input("ingresa el número de la registradora al finalizar el día: "))
num_pasajeros_dia= final_dia  - inicio_dia

total_pasaje_dia= num_pasajeros_dia * valor_pasaje

#las 3/4 partes de la empresa corresponden al 0.75% del total del pasaje recolectado en el dia

total_pasaje_empresa= total_pasaje_dia * 0.75
total_pasaje_conductor= total_pasaje_dia - total_pasaje_empresa

print(f"el total de pasajeros del dia fue: {num_pasajeros_dia} \n el valor liquidado al conductor fue de { total_pasaje_conductor}\n el valor liquidado a la empresa fue: {total_pasaje_empresa}")