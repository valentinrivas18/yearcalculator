from calendar import monthrange
import datetime
import calendar

cont = "Si"

while cont == "Si":

	print("1. Dado un año indicar si es bisiesto.")
	print("2. Dado un mes, devolver la cantidad de días correspondientes.")
	print("3. Dada una fecha (día, mes, año), indicar si es válida o no.")
	print("4. Dada una fecha, indicar los días que faltan hasta fin de mes.")
	print("5. Dada una fecha, indicar los días que faltan hasta fin de año.")
	print("6. Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.")
	print("7. Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días..")

	anio = int(input('Ingrese la funcion que desea operar: '))

	if anio == 1:
		year = int(input('Ingrese el año para comprobar si es bisiesto: '))
		def bisiesto(year):
			if (year%4==0 and year%100!=0) or year%400==0:
				Sies= f"El año {year} si es bisiesto"
				return(Sies)
			else:
				Noes=f"El año {year} no es bisiesto"
				return(Noes)
		print(bisiesto(year))

	elif anio == 2:
		year1 = int(input('Porfavor ingrese el año en numeros: '))
		month = int(input('Porfavor ingrese el mes en numeros (Ejemplo: 1, 2, 3): '))
		def daysleft(year1,month):
			daysmonth = monthrange(year1,month)[1]
			return(daysmonth)
		print(f"El mes {month} tiene {daysleft(year1,month)} dias.")

	elif anio == 3:
		print("Ingrese la fecha en el formato 'dd/mm/aa' ")
		inputDate = input("Ejemplo ( 05/07/2001 ) : ")

		day,month,year = inputDate.split('/')

		isValidDate = True
		try :
		    datetime.datetime(int(year),int(month),int(day))
		except ValueError :
		    isValidDate = False

		if(isValidDate) :
		    print("La fecha que usted ingreso es valida.")
		else :
		    print("La fecha que usted ingreso NO es valida.")
	elif anio == 4:
		ano = int(input('Ingrese el año: '))
		mes = int(input('Ingrese el mes: '))
		dia = int(input('Ingrese el dia: '))
		def diasrestantes(ano,mes,dia):

			fecha_inicial = datetime.date(ano, mes, dia)

			ultimodia = int(monthrange(ano,mes)[1])

			fecha_final = datetime.date(ano, mes, ultimodia)

			total = (fecha_final - fecha_inicial)
			return(total.days)
		print(f"Quedan {diasrestantes(anio,mes,dia)} dias.")
	elif anio == 5:
		angio = int(input('Ingrese el año: '))
		mes = int(input('Ingrese el mes: '))
		dia = int(input('Ingrese el dia: '))
		def diasrestantes(angio,mes,dia):
			f1 = datetime.date(angio, mes, dia)
			f2 = datetime.date(angio, 12, 31)
			differencia = (f2 - f1)
			return(differencia.days)
		print(f"Quedan {diasrestantes(angio,mes,dia)} dias.")
	elif anio == 6:
		aniio = int(input('Ingrese el año: '))
		mes = int(input('Ingrese el mes: '))
		dia = int(input('Ingrese el dia: '))
		def diasrestantes(aniio,mes,dia):
			f1 = datetime.date(aniio, mes, dia)
			f2 = datetime.date(aniio, 1, 1)
			differencia = (f1 - f2)
			return(differencia.days)
		print(f"Han pasado {diasrestantes(aniio,mes,dia)} dias.")
	elif anio == 7:
		print('Ingrese la primera fecha porfavor: ')
		years1 = int(input('Ingrese el año: '))
		mes1 = int(input('Ingrese el mes: '))
		dia1 = int(input('Ingrese el dia: '))
		print('Ingrese la segunda fecha porfavor: ')
		years2 = int(input('Ingrese el año: '))
		mes2 = int(input('Ingrese el mes: '))
		dia2 = int(input('Ingrese el dia: '))

		f1 = datetime.date(years1, mes1, dia1)
		f2= datetime.date(years2, mes2, dia2)
		daysLeft = f2 - f1

		years = ((daysLeft.total_seconds())/(365.242*24*3600))
		yearsInt=int(years)

		months=(years-yearsInt)*12
		monthsInt=int(months)

		days=(months-monthsInt)*(365.242/12)
		daysInt=int(days)

		print(f'Han pasado {yearsInt} años, {monthsInt} meses y {daysInt} dias.')
	else:
		print('Porfavor ingrese un valor valido')
	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()