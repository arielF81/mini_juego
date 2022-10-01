import tkinter as tk
#Creo mis funciones
def verificar(dato):
   if not dato: print("Error en el nombre ingresado")
   else: return dato

def convertir(valor):
   if not valor.isdecimal(): print("Error en la cantidad de cursos ingresados")
   else: return int(valor)

def listarAlumnos():
   if not alumnos: print("No hay alumnos en la lista")
   else:
      print("Lista de alumnos: ")
      for nombre in alumnos:
         print(f"{nombre} - {alumnos[nombre]} cursos")

def agregarAlumno():
   nombre_alumno = verificar(caja_nombre.get())
   cursos = convertir(caja_cursos.get())
   if nombre_alumno != None and cursos != None:
      alumnos[nombre_alumno] = cursos
      print("Has ingresado el alumno correctamente")

#####Acá empieza el programa en sí mismo#####
alumnos = {}
#Creo mi ventana
ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Proyecto integrador")
#Agrego los elementos
boton_lista = tk.Button(text="Ver lista de alumnos", command=listarAlumnos)
boton_lista.place(x=10, y=10)
etiqueta_nombre = tk.Label(text="Nombre alumno")
etiqueta_nombre.place(x=10, y=60)
caja_nombre = tk.Entry()
caja_nombre.place(x=110, y=60, width=150)
etiqueta_cursos = tk.Label(text="Cursos")
etiqueta_cursos.place(x=10, y=100)
caja_cursos = tk.Entry()
caja_cursos.place(x=110, y=100, width=30)
boton_agregar = tk.Button(text="Agregar a la lista", command=agregarAlumno)
boton_agregar.place(x=10, y=150)
boton_cursos = tk.Button(text="Ver cantidad de cursos")
boton_cursos.place(x=120, y=150)

ventana.mainloop()