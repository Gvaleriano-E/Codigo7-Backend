# una forma de almacenar varios valores en una misma variable
# LISTAS
colores = ['azul', 'negro', 'amarillo', 'purpura']
misc = ['eduardo', 18, False, 14.5, '2015-04-14', ['1', 2, 3]]
# imprimir la primera posicion
print(colores[1])
# imprimir la ultima posicion de la lista
print(colores[len(colores)-1])
print(colores[-1])
# imprimir desde la 0 hasta la <2
print(colores[0:2])
# imprimir desde la posicion 1
print(colores[1:])

# la forma de copiar el contenido y ya no utilizar la misma posicion de memoria para ambas variables es:
# en js se usaria colores2= [...colores]
colores2 = colores[:]
colores2[0] = "violeta"
print(colores)

nombre = "Juanito"
print(nombre[1])
# solamente se puede usar las posiciones de una variable str(STRING) para leer mas no para modificar su contenido
# nombre[1] = "e"

# metodo para agregar un nuevo elemento a una lista
colores.append('indigo')
print(colores)
# metodo para eliminar un valor solamente si existe lo eliminara, sino indicara un error
colores.remove("azul")
print(colores)
# el metodo pop ademas de eliminarlo, lo podemos almacenar en una variable
colore_eliminado = colores.pop(0)
print(colores)
print(colore_eliminado)
#otro metodo para eliminar un valor de una lista
del colores[0]
print(colores)
# metodo para resetear toda la lista y dejar en blanco
colores.clear()
print(colores)
#tupla=> coleccion de elementos ordenada no se puede modificar luego de su creacion
notas=(14,16,17,11,5,1)
print(notas[0])
print(notas[-1])
#notas[0]=20
#print(notas.length())
print(len(notas))
#cantidad de elementos de la tupla notas es 6 elementos
print("la cantdad de elementos de la tupla nota es{} elementos".format(len(notas)))
print(f"la cantidad de elementos  de la tupla nota es{len(notas)} elementos")
print("la cantidad de elementos de la tupla nota es", len(notas),"elementos")

# ver si hay elementos repetidos  enuna tupla
print(notas.count(5))

# conjunto=> coleccion de elementos desordenas , OSE que una vez que la creemos no
# no podremos  a sus posisicioens ya que se ordenaran aleatoriamente
estaciones ={"verano","otoño","primavera","Invierno"}
print(estaciones)
estaciones.add("OTOÑOVERANO")
print (estaciones)
# el metoso  in  , sirve para validae si un valor esta dentro de una coleccion 
# de datos
print("OTOÑOVERANO" in estaciones)
#esto no se puede hacer  en los conuntos
#diccionarios => coleccion de elementos que estan  indexados,
# que nosotros manejamos el nombre de sus llaves
persona ={
'id':1,
'nombre':'juancito',
"relacion":"soltero",
"fecha_nacimiento":"1992/08/04",
"hobbies":[
         {
             "nombre":"Futbol",
             "conocimiento":"Itermedio"
         },
         {
             "nombre":"Drones",
             "conocimiento":"Basico"
         }
]

}
print(persona['nombre'])
#en JS seria =>persona.hobbies[0].conocimento
print(persona["hobbies"][0]['conocimiento'])
persona['apellido']="Martinez"
# en python si la llave del diccionario no 
# existe lanzara un error y hara que el programa no continue
persona.pop("id")


libro={
    "nombre":"Harry Potter",
    "autor":"J.K. Rowling",
    "editotrial":"balablaa",
    "año":"2005",
    "idiomas":[
         {
            "nombre": "español"
        },
        {
            "nombre": "ingles"
        },
        {
            "nombre": "frances"
        },
        {
            "nombre": "aleman"
        },
    ],
    "calificacion": 5,
    "imdb": "00asd12-asd878-a4s5d4a5-a45sd4a5sd",
     "tomo":("La piedra filosofal","LA camra secreta", "El vuelo del Fenix")
}
print(libro["año"]
)
# ejercicio 1
# EJERCICIO 1
# devolver el autor del libro
print(libro["autor"])
# EJERCICIO 2
# devolver el segundo tomo
print(libro["tomos"][1])
# EJERCICIO 3
# devolver la cantidad de idiomas del libro
print(len(libro["idiomas"]))
# EJERCICIO 4
# indicar si esta o no esta el idioma ruso


