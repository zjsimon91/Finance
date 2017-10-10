__author__ = 'zjsimon'
from cashflows import *
from itertools import izip


def q1():
    l = calcYTM([100],96.2),calcYTM([0,100],91.6),calcYTM([0,0,100],86.1)
    s1,s2,s3 = l
    print "1) r1 = {0:%}".format(s1)
    print "1) r2 = {0:%}".format(s2)
    print "1) r3 = {0:%}".format(s3)

    print "2)  {0:,}".format(bondValue([300,210,400],l) - 600)
    npv = -600 + 300/(1+s1) + 210/(1+s2)**2 + 400/(1+s3)**3
    print npv

def q2():
    #1
    bondA = bondValue([100],[.05])
    bondB = bondValue([5,105],[.055]*2)
    bondC = bondValue([6,6,106],[.06]*3)

    print "Pa = {0:,}".format(bondA)
    print "Pb = {0:,}".format(bondB)
    print "Pc = {0:,}".format(bondC)

    #2
    spot1 = calculateSpot(bondA,[100],[None])
    spot2 = calculateSpot(bondB,[5,105],[spot1,None])
    spot3 = calculateSpot(bondC,[6,6,106],[spot1,spot2,None])

    print "1) r1 = {0:%}".format(spot1)
    print "1) r2 = {0:%}".format(spot2)
    print "1) r3 = {0:%}".format(spot3)

    spots =[spot1,spot2,spot3]

    #3 Longing and short - I have questions about what I'm doing here
    x3 = 100.0/106
    x2 = x3*6/105
    x1 = (x3*6 - x2*5)/100
    price = -x3*bondC + x2*bondB + x1*bondA
    print x3,x2,x1,price
    print bondValue([0,0,100],spots)

def q3():
    npv_costs = 20.0/1.05**10 + 30.0/1.05**30
    duration = ((20.0/1.05**10)*10 + (30.0/1.05**30)*30)/npv_costs
    md = duration/1.05
    delta_pv = (-npv_costs) * md * (-.0025)

    tbill_allocation = (npv_costs*md - (20*18))/(((1/1.05)*18)- (20*18))

    print "{0:20} = {1:20,}".format("NPV of Liabilities",npv_costs)
    print "{0:20} = {1:20,}".format("Duration", duration)
    print "{0:20} = {1:20,}".format("Modified Duration", md)
    print "{0:20} = {1:20,}".format("Aprox. Price Change", delta_pv)
    print "{0:20} = {1:20,}".format("tbills", tbill_allocation*18)
    print "{0:20} = {1:20,}".format("tbonds", (1-tbill_allocation)*18)

def q4():
    ds = [.5,1,1,5]
    weights = map(lambda x:x/100.0,[200,300,-900,500])
    duration = sum([k*v for k,v in zip(ds,weights)])
    
    md = duration/1.03

    delta_pv = (-100) * md * (.01)


    print "{0:20} = {1:20,}".format("Duration", duration)
    print "{0:20} = {1:20,}".format("Aprox. Price Change", delta_pv)

if __name__ == "__main__":
    #q1()
    #q2()
    #q3()
    q4()
    pass