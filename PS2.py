__author__ = 'zjsimon'
from cashflows import *




def q1():
    l = calcYTM([100],96.2),calcYTM([0,100],91.6),calcYTM([0,0,100],86.1)
    s1,s2,s3 = l
    print "1) r1 = {0:%}".format(s1)
    print "1) r2 = {0:%}".format(s2)
    print "1) r3 = {0:%}".format(s3)

    print "2)  {0:,}".format(bondValue([300,210,400],l) - 600)

    print l
if __name__ == "__main__":
    q1()
    pass