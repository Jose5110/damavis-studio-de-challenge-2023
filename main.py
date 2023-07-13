from data.settings import *
from data.labyrinth import Labyrinth

def main():
    while True:
        try:
            options = ['default','test_1','test_2','test_3','test_4']
            for count, option in enumerate(options, start=1):
                print(count, option)
            selection = int(input('Introduzca el numero de la opcion para seleccionarla: '))

            lab = Labyrinth(options[selection-1])
            array = lab.array_generator()
            for i in array:
                print(i)
            print('')

            validation = input('Do you want to try again (y/n - > any key ): ')
            if validation == 'y':
                    continue
            else:
                    break
                    
        except ValueError:
            print('Introduzca un numero entero dentro del rango de opciones: ')
            continue

if __name__ == '__main__':
    main()