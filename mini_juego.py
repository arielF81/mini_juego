
import random
#Genero mi lista de números
mis_numeros = []
while len(mis_numeros) < 6:
   numero = input("Ingresá 6 números de 0-15: ")
   if numero.isdecimal():
      numero = int(numero)
      if numero > 15: print("Número fuera de rango (0-15)")
      elif numero not in mis_numeros: mis_numeros.append(numero)
      else: print("Este número ya lo elegiste")
   else: print("Entrada inválida")
print("Tus números elegidos son:", mis_numeros)
#Sorteo
sorteo = []
while len(sorteo) < 6:
   numero_azar = random.randint(0,15)
   if numero_azar not in sorteo: sorteo.append(numero_azar)
print("Los números sorteados fueron:", sorteo)
#Ganadores
ganadores = []
for num in mis_numeros:
   if num in sorteo:
      print("Este lo acertaste:", num)
      ganadores.append(num)
print(f"Acertaste {len(ganadores)} números, que fueron los siguientes: {ganadores}") 

