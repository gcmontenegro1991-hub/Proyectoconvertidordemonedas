from colorama import Fore, Style, init

init(autoreset=True)


print(Fore.MAGENTA + Style.BRIGHT)
print("==============")
print("        💵 CONVERSOR DE MONEDA  💵")
print("=================")

print(Fore.CYAN + "/n DOLARES A PESOS COLOMBIANOS 💰")


print(Fore.WHITE + "/nIngrese los siguientes datos:")

dolares = float(input(Fore.GREEN + "Cantidad de dolares: "))

valor_dolar = float(input(Fore.GREEN + "valor del dolar:"))


pesos = dolares * valor_dolar


print(Fore.MAGENTA + "/n==========")     
print(Fore.CYAN + "         RESULTADO")
print(Fore.MAGENTA + "===========================")

print(Fore.WHITE + "Dolares:", dolares)
print(Fore.WHITE + "Tasa de cambio:", valor_dolar)

print(Fore.YELLOW + Style.BRIGHT)
print("TOTAL EN PESOS COLOMBIANOS")
print(Fore.YELLOW + "$ " +  format(pesos, ",.2f"))

print(Fore.MAGENTA + "/n=============")
print(Fore.GREEN + "  ¡GRACIAS POR UTILIZAR EL PROGRAMA!")
print(Fore.MAGENTA + "==================")



