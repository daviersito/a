import csv
import random
import os
from statistics import geometric_mean
sueldos=[]
trabajadores=["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández" ]
listas=list(zip(trabajadores,sueldos))
sueldobajo= []
sueldomedio = []
sueldoalto = []

def validarMenu():
    print("1. asignar sueldos\n"+
          "2. clasificar sueldos \n"+
          "3. ver estadisticas \n"+
          "4. reporte de sueldos\n"+
          "5.salir del programa"
          )
    while(True):
        try:
            op=int(input("    Elija su opción: "))
            if(op>=1 and op<=5):
                break
        except ValueError:
            print("Debe ser un número entero")
    return op


def asignarsueldos():
    
    trabajadores=["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández" ]
    i = 1
    while(i<=10):
        sueldos.append(random.randint(1, 3000000))
        i+=1
    print(trabajadores)
    print(sueldos)
    with open('archivo.csv', 'a+', newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)
        escritor = csv.writer(archivo)
        escritor.writerow(listas)


    
def estadisticas(sueldos):
    print(f'El numero mayor es {max(sueldos)}')
    print(f'El numero menor es {min(sueldos)}')
    sumasuel = 0
    for i in sueldos:
        sumasuel += i
    print(f'El promedio es {sumasuel/len(sueldos)}')
    print("media geometrica")
    print(geometric_mean(sueldos))
    
def clasificacion(sueldobajo, sueldomedio, sueldoalto):
    for i in sueldos:
        contbajo=0
        contmedio=0
        contalto=0
        if i < 800000:
            sueldobajo.append(i)
            contbajo+=1
        elif i > 800000 and i < 2000000:
            sueldomedio.append(i)
            contmedio+=1
        elif i > 2000000:
            sueldoalto.append(i)
            contalto+=1 
    print(f"Sueldo bajo {sueldobajo}{contbajo}")
    print(f"sueldo medio {sueldomedio} hay {contmedio}")
    print(f"sueldo alto {sueldoalto} hay {contalto}")
    return sueldobajo, sueldomedio, sueldoalto

def reportesueldo():
    print("nombre del empleado", "sueldo base", "descuento salud", "descuento afp", "sueldo liquido")
    for i in sueldos:
        for j in trabajadores:
            descuentoSalud = i * 0.07
            afp = i * 0.12
            sueldoLiquido = i - descuentoSalud - afp
        
        
            print(j,   i       ,descuentoSalud        ,afp,          sueldoLiquido )
    

