def fit(xvals, yvals):
    if len(xvals) != len(yvals):
        return 1

    N = len(xvals)
    sumx = sum(xvals)
    sumy = sum(yvals)
    sumx2 = sum(map(lambda x: x * x, xvals))
    sumxy = sum(map(lambda x, y: x * y, xvals, yvals))

    delta = N * sumx2 - (sumx) ** 2
    m = (N * sumxy - sumx * sumy) / delta
    b = (sumx2 * sumy - sumx * sumxy) / delta
    # b = (sumy - m * sumx) / N

    sxy2 = (1 / (N - 2)) * sum(map(lambda x, y: (y - (b + m * x)) ** 2, xvals, yvals))
    merr = (N * sxy2 / delta) ** 0.5
    berr = (sxy2 * sumx2 / delta) ** 0.5

    return [m, merr, b, berr]
