from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///nombre de la base de datos")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Palabra(Base):
    _tablename_ = 'palabras'
    id = Column(Integer, primary_key=True)
    palabra = Column(String(50))
    significado = Column(String(200))

    def _repr_(self):
        return f'Palabra: {self.palabra}\nSignificado: {self.significado}'

Base.metadata.create_all(engine)

while True:
    print('Seleccione una opción:')
    print('1. Agregar nueva palabra')
    print('2. Editar palabra existente')
    print('3. Eliminar palabra existente')
    print('4. Ver listado de palabras')
    print('5. Buscar significado de palabra')
    print('6. Salir')

    opcion = input('Opcion #: ')

    try:
        opcion = int(opcion)
    except ValueError:
        print('Opción inválida. Por favor ingrese un número.')
        continue

    if opcion == 1:
        palabra = input('Ingrese la palabra: ')
        significado = input('Ingrese el significado: ')
        nueva_palabra = Palabra(palabra=palabra, significado=significado)
        session.add(nueva_palabra)
        session.commit()
        print('La palabra ha sido agregada exitosamente.')
    elif opcion == 2:
        id_palabra = input('Ingrese el ID de la palabra a editar: ')
        palabra = input('Ingrese la nueva palabra: ')
        significado = input('Ingrese el nuevo significado: ')
        palabra_editar = session.query(Palabra).filter_by(id=id_palabra).first()
        palabra_editar.palabra = palabra
        palabra_editar.significado = significado
        session.commit()
        print('La palabra ha sido editada exitosamente.')
    elif opcion == 3:
        id_palabra = input('Ingrese el ID de la palabra a eliminar: ')
        palabra_eliminar = session.query(Palabra).filter_by(id=id_palabra).first()
        session.delete(palabra_eliminar)
        session.commit()
        print('La palabra ha sido eliminada exitosamente.')
    elif opcion == 4:
        palabras = session.query(Palabra).all()
        print('Listado de palabras:')
        for palabra in palabras:
            print(palabra)
    elif opcion == 5:
        palabra = input('Ingrese la palabra a buscar: ')
        palabras = session.query(Palabra).filter(Palabra.palabra.like('%'+palabra+'%')).all()
        if len(palabras) == 0:
            print('La palabra no se encontró en el diccionario.')
        else:
            for palabra in palabras:
                print(palabra)
    elif opcion == 6:
        break
    else:
        print('Opción inválida. Por favor ingrese un número del 1 al 6.')

session.close()


