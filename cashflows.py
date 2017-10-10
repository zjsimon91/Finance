def perpetuity(p,r):
    """
        :param p: payment
        :param r: discount rate
        :return: Present Value of annuity
    """
    return p/r

def eaf(r,k):
    return ((1+r)/k)**k - 1

def annuity(p,r,n):
    """
        :param p: payment
        :param r: discount rate
        :param n: payment periods
        :return: Present Value of annuity
    """
    return p * ((1 - (1+r)**-n )/r)

def growthPerpetuity(p,r,g):
    """
        :param p: first payment
        :param r: discount rate
        :param g: growth rate of payments
        :return: Present Value of growth perpetuity
    """
    return (p/(r-g))

def growthAnnuity(p,r,g,n):
    """
    perpetuity - perpetuity starting n payment periods later
    :param p: first payment
    :param r: discount rate
    :param g: growth rate of payments
    :param n: number of periods
    :return: Present Value of growth annuity
    """
    perp = growthPerpetuity(p,r,g)
    return perp * (1-((1+g)/(1+r))**n)


#Fixed income
def calcYTM(flows,pv,beg=-1,end=100):
    r = 0
    pv_flows = pv - sum([flows[i]/(1+r)**(i+1) for i in range(len(flows))])
    while abs(pv_flows) > .01:
        if pv_flows < 0:
            newr = (r+end)/2.0
            beg = r
            r = newr
        else:
            newr = (r+beg)/2.0
            end = r
            r = newr

        pv_flows = pv - sum([flows[i]/(1+r)**(i+1) for i in range(len(flows))])

    return r

def bondValue(flows,rates):
    pv_flows =  sum([flows[i]/(1+rates[i])**(i+1) for i in range(len(flows))])
    return pv_flows

def calculateSpot(Value,flows,rates):
    rate_at = rates.index(None)
    flowValue = sum([flows[i]/(1+rates[i])**(i+1) for i in range(len(flows)) if i != rate_at] )
    pvMissing = Value - flowValue
    return (flows[rate_at]/pvMissing)**(1.0/(rate_at+1)) -1


if __name__ == "__main__":
    pass




