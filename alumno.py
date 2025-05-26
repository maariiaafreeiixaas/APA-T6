class Alumno:
    """
    Clase usada para el tratamiento de las notas de los alumnos. Cada uno
    incluye los atributos siguientes:

    numIden:   Número de identificación. Es un número entero que, en caso
               de no indicarse, toma el valor por defecto 'numIden=-1'.
    nombre:    Nombre completo del alumno.
    notas:     Lista de números reales con las distintas notas de cada alumno.
    """

    def __init__(self, nombre, numIden=-1, notas=[]):
        self.numIden = numIden
        self.nombre = nombre
        self.notas = [nota for nota in notas]

    def __add__(self, other):
        """
        Devuelve un nuevo objeto 'Alumno' con una lista de notas ampliada con
        el valor pasado como argumento. De este modo, añadir una nota a un
        Alumno se realiza con la orden 'alumno += nota'.
        """
        return Alumno(self.nombre, self.numIden, self.notas + [other])

    def media(self):
        """
        Devuelve la nota media del alumno.
        """
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def __repr__(self):
        """
        Devuelve la representación 'oficial' del alumno. A partir de copia
        y pega de la cadena obtenida es posible crear un nuevo Alumno idéntico.
        """
        return f'Alumno("{self.nombre}", {self.numIden!r}, {self.notas!r})'

    def __str__(self):
        """
        Devuelve la representación 'bonita' del alumno. Visualiza en tres
        columnas separas por tabulador el número de identificación, el nombre
        completo y la nota media del alumno con un decimal.
        """
        return f'{self.numIden}\t{self.nombre}\t{self.media():.1f}'

import re

def leeAlumnos(ficAlumnos):
    """
    Lee un fichero y devuelve un diccionario {nombre: Alumno}

    >>> alumnos = leeAlumnos('alumnos.txt')
    >>> for a in alumnos:
    ...     print(alumnos[a])
    ...
    171     Blanca Agirrebarrenetse 9.5
    23      Carles Balcells de Lara 4.9
    68      David Garcia Fuster     7.0
    """
    dicc = {}

    exp_id = r'\s*(?P<id>\d+)\s+'
    exp_nom = r'(?P<nom>[\w\s]+?)\s+'
    exp_notes = r'(?P<notes>[\d.\s]+)\s*'
    expresion = re.compile(exp_id + exp_nom + exp_notes)

    with open(ficAlumnos, 'rt', encoding='utf-8') as fp:
        for linea in fp:
            match = expresion.search(linea)
            if match:
                iden = int(match['id'])
                nombre = ' '.join(match['nom'].split())
                notas = [float(n) for n in match['notes'].split()]
                dicc[nombre] = Alumno(nombre, iden, notas)

    return dicc

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)