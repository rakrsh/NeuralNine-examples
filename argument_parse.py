#argument parsing : https://www.youtube.com/watch?v=alSgAbyC7K8&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=4

import sys
import getopt

filename = "logfile.txt"
message = "Hello"

#f:m are positional arguments
opts, args = getopt.getopt(sys.argv[1:], "f:m", ['filename', 'message'])
print(opts)
print(args)
for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)


