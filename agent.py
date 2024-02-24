"""
Rodrigo Merino de la Parra 
A00836396

Este codigo intenta simular el comportamiento de un agente de limpieza los 
agentes se mueven de manera aleatoria por la "habitacion" donde van
limpiando celdas sucias que van encontrando en su camino. Esta simulacion
corre por un tiempo maximo o hasta que no se encuentren mas celdas sucias

Cambios en algun parametro ??? 
    1. numero de agentes
    2. tamaño de la habitacion
    3. porcentaje de celdas sucias
    4. tiempo maximo
el comportamiento y rendimiendo de los agentes cambia significativamente
aumentar el numero de agentes en teoria aumenta la eficiencia de la limpieza
sin embargo tambien podria gastarse si los agentes se encuentran limpiando
las mismas celdas. Incrementar el tamaño de la habitacion o porcentaje de 
las celdas sucias hara que la tarea sea mas dificil y para que este
completamente limpio se ocuparan mas agentes.

Este modelo puede ser util para estudiar diferentes estrategias de limpieza
automatizada y hacer cambios en el codigo para optimizar el diseño y operacion 
de nuestros "robots de limpieza"

"""


import numpy as np
import random

# parametros basicos 
M, N = 10, 10  # dimension del tablero
num_agentes = 2
porcentaje_sucio = 30
tiempo_maximo = 100

# creamos la habitacion
habitacion = np.zeros((M, N))
celdas_sucias = random.sample(range(M*N), k=int((porcentaje_sucio/100)*M*N))
for i in celdas_sucias:
    habitacion[i//N][i%N] = 1  # se marca como sucia

# inicio de agentes
agentes = [(0, 0) for _ in range(num_agentes)]

# creamos la funcion con la que se va a mover nuestro agente todas las posibles direcciones
def mover_agente(pos):
    movimientos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while True:
        dx, dy = random.choice(movimientos)
        nueva_pos = (max(0, min(M-1, pos[0] + dx)), max(0, min(N-1, pos[1] + dy)))
        if nueva_pos != pos:  # checamos que no se salga de los limites
            return nueva_pos

# simulacion
tiempo = 0
movimientos_totales = 0
while tiempo < tiempo_maximo and np.sum(habitacion) > 0:
    for i in range(num_agentes):
        x, y = agentes[i]
        if habitacion[x, y] == 1:  # si esta sucia / la limpia
            habitacion[x, y] = 0
        nueva_pos = mover_agente((x, y))
        agentes[i] = nueva_pos  # actualizamos la posicion del agnete
        movimientos_totales += 1
    tiempo += 1

# estadisticas
celdas_limpias = np.sum(habitacion == 0)
porcentaje_limpias = (celdas_limpias / (M*N)) * 100

print(f"Tiempo: {tiempo}")
print(f"% de celdas limpias: {porcentaje_limpias}%")
print(f"# de movimientos: {movimientos_totales}")
