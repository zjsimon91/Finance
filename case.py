from cashflows import *

if __name__=="__main__":
    r = RandomVar(.0131,.0414)
    for i in range(11):
        x = RandomVar(.0131,.0414)
        r = r.combine(x,1,1,0)

    print r
    print .0414*12**.5
    print (.0131+1)**12 - 1