import sys

with open(sys.args[1]) as file_in:
    with open(sys.args[2], "w") as file_out:
        file_out.write(file_in.read().replace('"metadata": {\n    "collapsed": true\n   },\n', '"metadata": {},\n'))