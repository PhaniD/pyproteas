from pyproteas.pyproteas import PyProteas

import sys

if __name__ == '__main__':
    inp_file = sys.argv[1]
    pp = PyProteas(inp_file)
    count = pp.execute()
    print (count)
