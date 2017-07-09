import re
import sys, getopt

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input=", "output=", "str1=", "str2=", "str3="])

        search = []
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print '''
                This program is used for search up to 3 str
                -i: for input file
                -o: for output file
                --str1=: for the first str
                --str2=: for the second str
                --str3=: for the thred str
                '''
                sys.exit(1)
            elif opt in ("-i", "--input="):
                inFileName = arg
            elif opt in ("-o", "--output="):
                outFileName = arg
            elif opt in ("--str1="):
                search.append(arg)
            elif opt in ("--str2="):
                search.append(arg)
            elif opt in ("--str3="):
                search.append(arg)

        f = open(inFileName, 'r')
        f_b = open(outFileName, 'w+')

        temp = f.readlines()

        for line in temp:
            for sec in search:
                if re.match(sec, line) is not None:
                    f_b.write(line)

        f.close()
        f_b.close()
    except getopt.GetoptError:
        print("getopt error! Please use -h to see the help.");
        sys.exit(1);



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Please use -h to see the help."
    else:
        main()
