print("Sistema Financiero de apoyo al ahorrador ")
tarjeta_nombre = input("Asigna un nombre a tu tarjeta ")
tasa_interes = input("¿Qué tasa de interés maneja? (sin %)? ")
deuda_actual = input("¿Cuál es tu deuda actual con esa tarjeta? ")
pago_realizado = input("¿cuál es el pago que de este mes? ")
nuevos_cargos = input("Ingresa la suma de los gastos en el mes: ")

print("De la tarjeta ", tarjeta_nombre, " con tasa de interés de ", tasa_interes, "'%' debes: ", deuda_actual, ". Si tomamos en cuenta tu pago de $", pago_realizado, " y los gastos del mes que suman $", nuevos_cargos)

interes_mensual = int(tasa_interes)/12
deuda_recaulculada = (int(deuda_actual) - int(pago_realizado)) * (1 + int(interes_mensual))
int(nueva_deuda) = deuda_recaulculada + int(nuevos_cargos)

if nueva_deuda > pago_realizado:
    print("mayor")
else:
    print("El monto de tu pago para el mes siguiente será de $", nueva_deuda)
