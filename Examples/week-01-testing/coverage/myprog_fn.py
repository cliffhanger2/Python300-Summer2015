import sys

a = 0; b = 1

def foo( x ):
    if x:
        print "in branch"
        if x + 1:
            print "+ 1"
    print "out of branch"

if __name__ == '__main__':
    arg = int( sys.argv[1] )
    foo( arg )
