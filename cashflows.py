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

if __name__ == "__main__":
    machine = 600.0
    dep_annual = machine/3
    rev = 400.0
    cost = 100.0

    tax = .3
    r = .1

    p = (rev-cost)*(1-tax) + (dep_annual)*tax
    npv = annuity(p,r,3)-600
    print npv,p





