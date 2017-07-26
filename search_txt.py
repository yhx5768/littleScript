import re
import sys, getopt

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:s:", ["help", "input=", "output=", "str="])

        for opt, arg in opts:
            # print "%s is %s" %(opt, arg)
            if opt in ("-h", "--help"):
                print '''
                This program is used for search mulit strs to a new txt file.
                --input=: for input file
                --output=: for output file
                --str=: for the strs, sparated by ','
                '''
                sys.exit(1)
            elif opt in ("-i", "--input"):
                inFileName = arg
            elif opt in ("-o", "--output"):
                outFileName = arg
            elif opt in ("-s", "--str"):
                Str = arg

        search(inFileName=inFileName, outFileName=outFileName, Str=Str)

    except getopt.GetoptError:
        print("getopt error! Please use -h to see the help.");
        sys.exit(1);

def search(inFileName, outFileName, Str):
    f = open(inFileName, 'r')
    f_b = open(outFileName, 'w+')

    temp = f.readlines()

    search = Str.split(',')

    for line in temp:
        for sec in search:
            if re.match(sec, line) is not None:
                f_b.write(line)

    f.close()
    f_b.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Please use -h to see the help."
    else:
        main()
