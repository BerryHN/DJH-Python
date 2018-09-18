from optparse import OptionParser


'''
不使用usage

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
parser.add_option("-d",'--djh',dest="djhname", default=True,
                  help="test")

options, args = parser.parse_args()
print(options)
print(args)

'''

usage = "usage: python %test.py [options]"
parser = OptionParser(usage=usage)
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=True,
                  help="make lots of noise [default]")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose",
                  help="be vewwy quiet (I'm hunting wabbits)")
parser.add_option("-f", "--filename",
                  metavar="FILE", help="write output to FILE")
parser.add_option("-m", "--mode",
                  default="intermediate",
                  help="interaction mode: novice, intermediate, "
                       "or expert [default: %default]")
options, args = parser.parse_args()
print(options)
print(args)