import random as rd


####
def canalesSinTraslape():
	canalesAleatorios = []
	canal1 = rd.randint(1,14)			#numero de canal aleatorio 1
	canal2 = rd.randint(1,14)			#numero de canal aleatorio 2
	while canal1==canal2:
		canal2 = rd.randint(1,14)
	canalesAleatorios.append(canal1)
	canalesAleatorios.append(canal2)
	print("Canales escogidos aleatoriamente: "+str(min(canalesAleatorios))+", "+str(max(canalesAleatorios)))

	#
	rangosCanales = [(2401,2423),(2406,2428),(2411,2433),(2416,2438),(2421,2443),(2426,2448),(2431,2453),(2436,2458),(2441,2463),(2446,2468),(2451,2473),(2456,2478),(2461,2483),(2473,2495)]
	a,b=rangosCanales[canal1-1]
	c,d=rangosCanales[canal2-1]
	#print(a,b)
	#print(c,d)

	#
	print("Canales sin traslape: ")
	listaNoTraslape = []
	for i in range(0,14):
		if i!=canal1-1 and i!=canal2-1:
			e,f=rangosCanales[i]
			#print(e,f)
			if not(((e>a and e<b) or (f>a and f<b)) or ((e>c and d<b) or (f>c and f<d))):
				listaNoTraslape.append(i+1)
				print(i+1)
####



##Menu principal
opcion1 = 0
while opcion1!=3:
	opcion1= int(input("*****Estimacion de tasa de datos (data rate) en base al PHY seleccionado***** \nElija la banda que desea utilizar \n1) 2.4GHz \n2) 5GHz \n3) Salir \nR: "))
	if opcion1==1:
		canalesSinTraslape()
