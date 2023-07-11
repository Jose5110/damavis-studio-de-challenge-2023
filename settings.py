# Initial laberynth settings
free_space_char = '.'
blocked_space_char = '#'
block_width = 3
block_height = 1


default = { 'width' : 12,
            'height' : 9,
            'blocked_coordinates' : [(1,5),(3,0),(8,9)]}

custom = {'width' : 0,
          'height' : 0,
          'block_coordinates' : []}

test_1 = {'width' : 9,
          'height' : 5,
          'blocked_coordinates' : [(1,0),(1,4),(2,4),(3,1),(3,7),(4,1),(4,7)]}

test_2 = {'width' : 9,
          'height' : 5,
          'blocked_coordinates' : [(1,0),(1,4),(1,7),(2,4),(3,1),(3,7),(4,1),(4,7)]}

test_3 = {'width' : 3,
          'height' : 3,
          'blocked_coordinates' : []}

test_4 = {'width' : 10,
          'height' : 10,
          'blocked_coordinates' : [(1,1),(1,6),(2,1),(6,1),(7,1),(7,5),(8,6)]}

config = {'default':default, 'custom':custom, 'test_1':test_1, 'test_2':test_2, 'test_3':test_3, 'test_4':test_4}
