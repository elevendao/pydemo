import os

def myfunc(self, args):
    self.args=args
    print "sss"
    print "bbb"

def main():
    print "what the hell"
    realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)

    file_path = os.path.split(realpath)
    print file_path

    print realpath
    print dirname
    myfunc(

if __name__ == "__main__":
    main()
