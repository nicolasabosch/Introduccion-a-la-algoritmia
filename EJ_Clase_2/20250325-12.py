
cantDinero=int(input("Ingrese la cantidad de dinero\n"))

Billetes1000 = cantDinero//1000
cantDinero%=1000

Billetes500 = cantDinero//500
cantDinero%=500

Billetes100= cantDinero//100
cantDinero%=100

Billetes50=cantDinero//50
cantDinero%=50

Billetes10=cantDinero//10
cantDinero%=10

Billetes5=cantDinero//5
cantDinero%=5

billetes1=cantDinero//1

print("son", Billetes1000, "Billetes de 1000 \n",Billetes500, "Billetes de 500:\n",Billetes100,"Billetes de 100\n", Billetes50, "Billetes de 50: \n",Billetes10, "Billetes de 10:\n",Billetes5,"Billetes de 5 \n", billetes1 ,"Billetes de 1")