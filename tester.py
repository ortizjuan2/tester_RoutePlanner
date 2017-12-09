# tester file
from student_code import shortest_path
from helpers import load_map, show_map
from optparse import OptionParser
from time import clock


if __name__=='__main__':
    parser = OptionParser()
    parser.add_option('-f', '--file', dest='map_filename',
                        help='Map file name in pickle format.')
    parser.add_option('-s', '--start', 
                        dest='start', help='Starting node.')
    parser.add_option('-g', '--goal',
                        dest='goal', help='Goal node.')
    
    (options, arg) = parser.parse_args()
    # check for options
    if not options.start or not options.goal or not options.map_filename:
        parser.error("you must specify options, please type -h for details.")
    #
    start = int(options.start)
    goal = int(options.goal)
    map_filename = options.map_filename
    # load map
    M = load_map(map_filename)
    start_t = clock()
    path = shortest_path(M, start, goal)
    end_t = clock()
    print('Best path found {}'.format(path))
    print('Lapsed time: {0:2.4f} secs'.format(end_t - start_t))