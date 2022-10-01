#Ejercicio Dado

from random import randint as azar
while True :
   print("1 - Tirar dado\n2 - Salir")
   opcionMenu = input(">>> ")
   if opcionMenu == "1":
      dado = azar(1, 6)
      print(dado)
   elif opcionMenu == '2':
      print("Gracias por usar el programa, hasta luego")
      break
   else: print("Opción inválida") 