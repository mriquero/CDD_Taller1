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
			if not(((e>a and e<b) or (f>a and f<b)) or ((e>c and e<d) or (f>c and f<d))):
				listaNoTraslape.append(i+1)
				print(i+1)

def canalesPara5G():
	canales = [36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161,165]
	canal1 = rd.choice(canales)
	canal2= rd.choice(canales)
	while canal1==canal2:
		canal2=rd.choice(canales)
	print("Canales escogidos para 5G:"+str(canal1)+", "+str(canal2))

def calcularSNR():
	factor = int(input(
		"Escoja el factor que contribuye al piso de ruido que usted desee:\n1) Bluetooth + hornos microonda en uso\n2) Cables o conectores defectuosos\n3) “Interferencias” por sistemas de radio\nR: "))
	app = int(input(
		"Elija la aplicaciones que desee: \n1) Conectividad de red basica\n2) Conectividad de alta velocidad\n3) voIP\nR: "))
	factorPisoRuido = [-95,-90,-93]
	aplicacion = [-80,-70,-65]
	snr = aplicacion[app-1]-factorPisoRuido[factor-1]
	return (snr,app)

def calcularColor(snr,app):
	valoresSNRRecomendados = [15,25,30]
	print("El valor SNR es: "+str(snr))
	snrRecomendado = valoresSNRRecomendados[app-1]

	if snr==snrRecomendado:
		print("El mensaje de alerta es:"+'\033[92m' + "OK"+'\033[0m')
		return snr
	elif snr== snrRecomendado-2:
		print("El mensaje de alerta es:"+'\033[93m'+"Advertencia"+'\033[0m')
		return snr
	else:
		print("El mensaje de alerta es:"+'\033[91m'+"Negacion"+'\033[0m')
		return snr

####



##Menu principal
opcion1 = 0
estandar =0
while opcion1!=3:
	opcion1= int(input("*****Estimacion de tasa de datos (data rate) en base al PHY seleccionado***** \nElija la banda que desea utilizar \n1) 2.4GHz \n2) 5GHz \n3) Salir \nR: "))
	if opcion1==1:
		canalesSinTraslape()
		while(estandar not in [1,2]):
			estandar = int(input("Elija el estandar que desea usar:\n1) 802.11b\n2) 802.11g\nR: "))
		snr,posVRecomendado = calcularSNR()
		calcularColor(snr,posVRecomendado)
	elif opcion1==2:
		canalesPara5G()
		print("El estandar a usar es: 802.11a")
		snr, posVRecomendado = calcularSNR()
		calcularColor(snr, posVRecomendado)

