from data.settings import *
from data.labyrinth import Labyrinth
from data.pathfinder import *

def main():
    while True:
        try:
            # This is not the fastest program, for bigger tests let the program run for a while
            options = ['default','test_1','test_2','test_3','test_4']
            for count, option in enumerate(options, start=1):
                print(count, option)
            selection = int(input('Introduzca el numero de la opcion para seleccionarla: '))

            lab = Labyrinth(options[selection-1])
            array = lab.array_generator()
            rows = len(array)
            cols = len(array[0])

            # Vertex and goal format list must not be changed in any way
            vertex_formats = [(int, tuple), (tuple, int)]
            goal_formats = [(int, tuple), (tuple, int)]

            start = (0, (0, 1, 2))
            goals = [(rows-1,(cols-3,cols-2,cols-1)),((rows-3,rows-2,rows-1),cols-1)]

            # Print labyrinth for some visual reference about the test
            for i in array:
                print(i)
            print('')

            h_graph = make_horizontal_graph(array)
            v_graph = make_vertical_graph(array)
            h_graph_with_rotation = add_edges_between_graphs(h_graph,v_graph,array,vertex_formats)
            h_graph_with_rotation.update(v_graph)
            min_moves = breadth_first_search(h_graph_with_rotation,start,goals,vertex_formats, goal_formats)
            
            # This is formated so the output is the same as the one asked for
            # if you want to see the moves uncomment the extra print line below
            if min_moves is not (-1):
                print(len(min_moves)-1)
                # print(min_moves)
            else:
                print(min_moves)
            
            
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