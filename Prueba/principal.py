import funciones as s

op=0
while op!=5:
    op=s.validarMenu()
    if (op==1):
        s.asignarsueldos()
    if (op==2):
        s.clasificacion()
    if (op==3):
        s.estadisticas()
    if (op==4):
        s.reportesueldo()
    else:
        print("Finalizando programa... Desarrollado por Davier Ramos RUT 27.101.613-1")    
    