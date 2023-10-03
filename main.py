'''
Base de datos para guardar autor y los titulos de los libros con su fecha de publicación.
Se guarda en un diccionario el autor y los libros, los libros es un diccionario que tiene
dos listas con los títulos de los libros y la fecha de publicación. Todo esto se guarda
en una lista llamada biblioteca.
'''
biblioteca = [
    {
        'autor': 'gabriel garcia marquez',
        'libros': {
            'título': ['cien años de soledad', 'el amor en los tiempos de cólera', 'memorias de mis putas tristes' ],
            'fecha': ['1967', '1967', '2004']
        }
    },
    {
        'autor': 'oscar wilde',
        'libros': {
            'título': ['el retrato de dorian gray', 'el fantasma de canterville', 'el principe feliz'],
            'fecha' : ['1890', '1887', '1888']
        }
    },
    {
        'autor': 'marguerite duras',
        'libros': {
            'título': ['el amante', 'hiroshima mon amour', 'el dolor'],
            'fecha': ['1984', '1959', '1985']
        }
    }
]

def mostrar_libros():
    '''
    Se usan dos ciclos para para acceder a la bibliota e imprimir los autores con sus libros
    '''
    
    for info_autor in biblioteca:
        # se accede al autor
        autor = info_autor['autor'].upper() 
        
        # se accede a los libros y las fechas
        libros = info_autor['libros']['título']
        fechas = info_autor['libros']['fecha']

        interfaz = '█' * 70
        divisor = '-' * 70
        
        # se imprime al autor con una decoración
        print(f'{interfaz}\n{divisor}\n{autor}\n{divisor}')

        for i in range(len(libros)):
            # ciclo para acceder a los títulos y fechas
            libro = libros[i]
            fecha = fechas[i]
            # se imprime títulos y fechas
            print(f'Libro: {libro.title()}, Publicado en : {fecha}')

    print('█' * 70) # cierre de decoración para impresión en la consola

def mostrar_libros_por_autor():
    '''
    Función que solicita el nombre del autor para imprimir sus libros y la fecha de publicación
    de cada libro
    '''
    
    # solicita el nombre del autor
    nombre_autor = input('ingrese el nombre del autor: ').lower()

    # busca el autor o una palabra clave que más se parezca con el nombre de algún autor
    # en caso que el usuario escriba mal el nombre
    for libros_autor in biblioteca:
        autor = libros_autor['autor']
        libros = libros_autor['libros']['título']
        fechas = libros_autor['libros']['fecha']

        divisor = '-' * 70
        
        if nombre_autor in autor:
            
            print(f'{divisor}\n{autor.upper()}\n{divisor}')

            for i in range(len(libros)):
                libro = libros[i]
                fecha = fechas[i]
                print(f'Libro: {libro.title()}, Publicado en: {fecha}')
            break
    # En caso de no encontrar el autor, imprime que no se encuentra en la biblioteca
    else:
        print('Autor no encontrado en la biblioteca')        

def ingresar_libro():
    '''
    Función para ingresar un nuevo autor en la biblioteca, solicita el nombre,
    el título del libro y la fecha de publicación. Primero comprueba si ya
    se encuentra el autor en la biblioteca para agregar solo los libros y la fecha
    en caso que no, lo incorpora como un nuevo autor
    en un diccionario como se establece.
    '''
    nombre = input('Ingrese el nombre del autor\n')
    libro = input('Ingrese el título del libro\n')
    fecha = input('Ingrese la fecha de publicación\n')

    for autor_existente in biblioteca:
        if autor_existente['autor'] == nombre:
            print('Se ha agregado con éxito en BiblioLab')
            autor_existente['libros']['título'].append(libro)
            autor_existente['libros']['fecha'].append(fecha)
            break
    else:
        print('Se ha agregado con éxito en BiblioLab')
        nuevo_autor = {
            'autor': nombre,
            'libros': {
                'título': [libro],
                'fecha': [fecha]
            }
        }
        biblioteca.append(nuevo_autor)

def main():
    '''
    Función principal que ejecuta el programa, llama a las demás funciones en lo requerido
    por el usuario.
    '''
    
    while True:
        print('Bienvenidos a BiblioLab')

        acceso = input('¿Desea ver nuestra biblioteca completa? (Si, No): ').lower()
        if acceso == 'si':
            mostrar_libros()
            
        buscar = input('¿Desea buscar un autor en especial? (Si o No): ').lower()
        if buscar == 'si':
            mostrar_libros_por_autor()

        agregar_nuevo_autor = input('¿Desea agregar un nuevo autor en BiblioLab? (Si o No): ').lower()
        if agregar_nuevo_autor == 'si':
            ingresar_libro()

        salir_del_programa = input('¿Desea salir del programa? (Si o No): ')

        if salir_del_programa == 'si':
            print('Gracias por usar nuestros servicios')
            break
        else:
            print('Opción no valida, por favor intentelo de nuevo')

main() # corre el programa