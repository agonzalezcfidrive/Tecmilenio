print("Sistema Financiero de apoyo al ahorrador ")
tarjeta_nombre = input("Asigna un nombre a tu tarjeta ")
tasa_interes = float(input("¿Qué tasa de interés maneja? (sin %)? "))
deuda_actual = float(input("¿Cuál es tu deuda actual con esa tarjeta? "))
pago_realizado = float(input("¿cuál es el pago que de este mes? "))
nuevos_cargos = float(input("Ingresa la suma de los gastos en el mes: "))

print("De la tarjeta ", tarjeta_nombre, " con tasa de interés de ", tasa_interes, "'%' debes: ", deuda_actual, ". Si tomamos en cuenta tu pago de $", pago_realizado, " y los gastos del mes que suman $", nuevos_cargos)

interes_mensual = tasa_interes/12
deuda_recaulculada = (deuda_actual - pago_realizado) * (1 + interes_mensual)
nueva_deuda = deuda_recaulculada + nuevos_cargos

if nueva_deuda > pago_realizado:
    print("Como la deuda es mayor que el pago anterior: $", deuda_recaulculada, " deberás pagar lo mismo que este mes: $",pago_realizado)
else:
    print("El monto de tu pago para el mes siguiente será de $", nueva_deuda)
    Print("Recomendaría al menos pagar: $", deuda_actual*interes_mensual, " para que tu ")
