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
    for info_autor in biblioteca:
        autor = info_autor['autor'].upper() 
        
        libros = info_autor['libros']['título']
        fechas = info_autor['libros']['fecha']

        interfaz = '█' * 70
        divisor = '-' * 70
        
        print(f'{interfaz}\n{divisor}\n{autor}\n{divisor}')

        for i in range(len(libros)):
            libro = libros[i]
            fecha = fechas[i]
            print(f'Libro: {libro.title()}, Publicado en : {fecha}')

    print('█' * 70)

def mostrar_libros_por_autor():
    nombre_autor = input('ingrese el nombre del autor: ').lower()

    for libros_autor in biblioteca:
        autor = libros_autor['autor']
        libros = libros_autor['libros']['título']
        fechas = libros_autor['libros']['fecha']

        interfaz = '█' * 70
        divisor = '-' * 70
        
        if (nombre_autor == autor) == True:
            for i in range(len(libros)):
                libro = libros[i]
                fecha = fechas[i]
                print(f'{interfaz}\n{divisor}\n{autor}\n{divisor}\nLibro: {libro}, Publicado en: {fecha}')
            break
        elif (nombre_autor == autor) == False:
            continue
        else:
            print('autor no encontrado en la biblioteca')
            break

mostrar_libros_por_autor()