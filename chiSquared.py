def chi(fxvals, yvals, yerr):
    chiSquared = sum(map(lambda fx, y, e: ((y - fx)**2)/e**2, fxvals, yvals, yerr))
    return chiSquared
