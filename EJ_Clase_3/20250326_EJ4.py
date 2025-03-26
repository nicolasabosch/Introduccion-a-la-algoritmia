horas=int(input("que hora es?: "))
minutos=int(input("que minuto es?: "))

fullTime=input("El formato horario es completo o parcial?")

if fullTime=="parcial":
    fullTime=False
else:
    fullTime=True


if fullTime==False:
    if horas<=12 and horas >=0:
        esPM=input("Es AM o PM")
        if esPM=="AM":
            esPM=False
        else:
            esPM=True
        print("El formato de las horas esta bien.")
        
    if horas>12:
        print("Formato horario mal ingresado.")
        
    if minutos>60:
        print("El formato de los minutos esta mal")
    
    else:
        print("El formato de los minutos esta bien")
        
else:
    if horas<24 and horas>=0:
        print("El formato de las horas esta bien")
        
    