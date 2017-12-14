import pandas as pd, numpy as np
import pulp
from scipy.optimize import minimize
import matplotlib.pyplot as plt,seaborn as sns
from cashflows import *

class RandomVar():
    def __init__(self, exp, stddev):
        self.exp = exp
        self.stddev = stddev

    def combine(self, var, a, b, corr):
        exp = self.exp * a + var.exp * b
        stddev = ((a ** 2 * self.stddev ** 2) + (b ** 2 * var.stddev ** 2) + (
        2 * a * b * self.stddev * var.stddev * corr)) ** .5
        return RandomVar(exp, stddev)

    def __str__(self):
        return str((self.exp, self.stddev))

    def to_dict(self):
        return {"exp":self.exp,"stddev":self.stddev}


def optimizePortfolio(cov):
    weights =[1.0/cov.shape[0] for i in range(cov.shape[0])]
    V = cov.as_matrix()

    def calculate_portfolio_var(w, V):
        w = np.matrix(w)
        return (w * V * w.T)[0, 0]

    # unconstrained portfolio (only sum(w) = 1 )
    cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1.0})
    res = minimize(calculate_portfolio_var, weights, args=V, method='SLSQP', constraints=cons)
    return res


def q1():
    abc = RandomVar(.2, .2)
    xyz = RandomVar(.15, .25)
    corr = .2

    print abc.combine(xyz, .6, .4, .2)
    print abc.combine(xyz, .9, .1, .2)


def q2():
    a = RandomVar(.11, .3)
    b = RandomVar(.145, .45)
    c = RandomVar(.09, .3)
    cols = ['a','b','c']

    vars = pd.DataFrame([each.to_dict() for each in (a,b,c)],index=cols)
    df = pd.DataFrame([[1.0, .3, .15],
                        [.3, 1.0, .45],
                        [.15, .45, 1]], index=cols,columns=cols)

    vars['weights'] = 1.0/3
    print df

    cov = df.multiply(vars['stddev'],0).multiply(vars['stddev'],1)
    p_std = cov.multiply(vars['weights'],0).multiply(vars['weights'],1).sum().sum()
    print (vars['exp']*vars['weights']).sum(),p_std**.5


def q3():
    disc = pd.DataFrame([[.5,-.25],[-.1,.05]],index=['GOOD','BAD'],columns=['A','B'])
    vars = disc.agg(['mean','std']).T
    print disc.std()
    cov = disc.cov()
    res = optimizePortfolio(cov)
    vars['weights'] = res.x

    print vars
    print round((vars['weights']*vars['mean']).sum(),4)
    print round(cov.multiply(vars['weights'],0).multiply(vars['weights'],1).sum().sum(),4)


def q4():
    abc = RandomVar(.2, .2)
    xyz = RandomVar(.15, .25)
    corr = .2
    rf = .05
    vals = []
    iters = 10000
    prev = 0
    for i in range(iters):
        a = i/float(iters)
        b = 1.0-a
        new = abc.combine(xyz,a,b,corr)
        if i > 0:
            slope = (new.exp-prev.exp)/(new.stddev-prev.stddev)
            rf_slope = (new.exp-rf)/(new.stddev)
            vals.append([new.exp,new.stddev,slope,rf_slope,a,b])

        prev = new


    df = pd.DataFrame(vals,columns=['exp','std','slope','rf','abc','xyz'])
    df['diff'] = (df['rf']-df['slope']).abs()
    d = df.sort_values('diff',ascending=1).head().iloc[0]
    #sns.regplot(x=df["std"], y=df["exp"], fit_reg=False)
    #plt.show()



if __name__ == "__main__":
    #q3()
    #q4()
    r2 = .06 + .7 * .3 * .15 * (.1 - .06)/(.15**2)
    r1 = .06 + .4 * .2 * .15 * (.1 - .06)/(.15**2)

    R1 = RandomVar(r1,.2)
    R2 = RandomVar(r2,.3)

    print R1
    print R2
    combo = R1.combine(R2,.3,.7,.5)
    print combo
    eff = (combo.exp-.06)/(.1 -.06)
    std = eff*.15
    print eff,std