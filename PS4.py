from cashflows import  *


def q2():
    a, b = findOption([150, 1.1, 0], [90, 1.1, 10])
    lu = a * 120 + b
    print "t1 upper Sp put price ",lu

    a, b = findOption([95, 1.1, 5], [50, 1.1, 50])
    ld = a * 80 + b
    print "t1 lower Sp put price ", ld

    a, b = findOption([120, 1.1, lu], [80, 1.1, ld])
    l = a * 100 + b
    print "t0  put price ", l

def q3():
    rf = 1.03
    S = 80

    #1
    u =S*1.3
    uu = u*1.3
    ud = u*.8

    d = S*.8
    dd = d*.8
    du = d*1.3
    X = 95

    print "         ",uu
    print "    ",u
    print "         ", ud
    print S
    print "         ", du
    print "    ", d
    print "         ", dd


    a, b = findOption([uu,rf,max(uu-X,0)],[ud,rf,max(ud-X,0)])
    up = a*u + b
    down = 0

    a, b = findOption([u, rf, up], [d, rf, down])
    t0 = a*S + b
    print t0

    #PUT
    a, b = findOption([uu, rf, max( X - uu, 0)], [ud, rf, max( X - ud, 0)])
    up = a * u + b

    a, b = findOption([du, rf, max(X - du, 0)], [dd, rf, max(X - dd, 0)])
    down = a*d + b

    a, b = findOption([u, rf, up], [d, rf, down])
    t0 = a * S + b

    print t0, "PUT"

    # put1 = a*up1 + b
    #
    # a, b = findOption([up1, rf, max(X-up1, 0)], [d1, rf, max(X- d1, 0)])
    # print "European put", a * S + b
    # print [up1, rf, max(X-up1, 0)], [d1, rf, max(X- d1, 0)]

def q4():
    v = 10000
    S = 50
    u = 65
    d = 40

    rf = 1.01

    print v*S*rf
    a, b = findOption([u, rf, max(S-u, 0)], [d, rf, max(S - d, 0)])
    print  a * S + b




if __name__ == "__main__":
    S = 100
    rf = 1.05
    u = S * 1.25
    uu = u * 1.25
    ud = u * .8

    d = S * .8
    dd = d * .8
    du = d * 1.25
    X = 95

    print "         ", uu
    print "    ", u
    print "         ", ud
    print S
    print "         ", du
    print "    ", d
    print "         ", dd

    a, b = findOption([uu, rf, max(uu - X, 0)], [ud, rf, max(ud - X, 0)])
    up = a * u + b
    down = 0

    a, b = findOption([u, rf, up], [d, rf, down])
    t0 = a * S + b
    print t0