from math import fabs
a1 = 0.0134
b1 = 1
c1 = 4.35e-4
m1 = 1
a2 = 2.049
b2 = 0.563e-3
c2 = 0.528e5
m2 = 1
alpha0 = 0.05
alphaN = 0.01
l = 10
T0 = 300
R = 0.5
F0 = 50
h = 1e-3
t = 1

def get_consts():
    cc = (-alpha0*alphaN*l)/(alphaN-alpha0)
    dd = (alphaN*l)/(alphaN-alpha0)
    return cc, dd
def alpha(x):
    return cc/(x-dd)

def k(T):
    return a1 * (b1 + c1 * T ** m1)

def c(T):
    return a2 + b2 * T ** m2 - (c2 / T ** 2)

def A(T):
    return t / h * count_minus_half(k, T, t)

def D(T):
    return t / h * count_plus_half(k, T, t)

def B(x, T):
    return A(T) + D(T) + h * c(T) + h * t * 2 * alpha(x) / R

def F(x, T):
    return h * t * 2 * T0 * alpha(x) / R + T * h * c(T)

def count_plus_half(function, n, step):
    return (function(n) + function(n + step)) / 2

def count_minus_half(function, n, step):
    return (function(n) + function(n - step)) / 2

def find_koef_with_left(T):
    chalf = count_plus_half(c, T[0], t)
    khalf = count_plus_half(k, T[0], t)
    c0 = c(T[0])
    K0 = h / 8 * chalf + h / 4 * c0 + t / h * khalf + t * h / 4 * alpha(h / 2) / R + t * h / 2 * alpha(0) / R
    M0 = h / 8 * chalf - t / h * khalf + t * h / 4 * alpha(h / 2) / R
    P0 = h / 8 * chalf * (T[0] + T[1]) + h / 4 * c0 * T[0] + F0 * t + t * h / 4 * T0 / R * (3 * alpha(0) + alpha(h))
    return K0, M0, P0

def find_koef_with_right(T):
    chalf = count_minus_half(c, T[-1], t)
    khalf = count_minus_half(k, T[-1], t)
    cN = c(T[-1])
    KN = h / 8 * chalf + h / 4 * cN + t / h * khalf + t * alphaN + t * h * alpha(l - h / 2)/R/4 + t * h * alpha(l)/R/4
    MN = h / 8 * chalf - t / h * khalf + t * h * alpha(l - h / 2)/R/4
    PN = h / 8 * chalf * (T[-1] + T[-2]) + h / 4 * cN * T[-1] + t * alphaN * T0 + t * h / 2 / R * T0 * (alpha(l) + alpha(l - h / 2))
    return KN, MN, PN

def find_next (y):
    K0, M0, P0 = find_koef_with_left(y)
    KN, MN, PN = find_koef_with_right(y)
    ksi = [0, -M0 / K0]
    eta = [0, P0 / K0]
    x = h
    n = 1
    while (x + h < l):
        znam = (B(x, y[n]) - A(y[n]) * ksi[n])
        ksi.append(D(y[n]) / znam)
        eta.append((F(x, y[n]) + A(y[n]) * eta[n]) / znam)
        n += 1
        x += h
    ynext = [0] * (n + 1)
    ynext[n] = (PN - MN * eta[n]) / (KN + MN * ksi[n])
    for i in range(n - 1, -1, -1):
        ynext[i] = ksi[i + 1] * ynext[i + 1] + eta[i + 1]
    return ynext

def iterations():
    N = int(l / h + 1)
    ti = 0
    y = [T0]*N
    res = []
    res.append(y)
    ynext = [0]*N
    while 1:
        ycur = y
        while 1:
            ynext = find_next(ycur)
            maxfault = fabs((y[0] - ynext[0]) / ynext[0])
            for i in range(1, N):
                fault = fabs((y[i] - ynext[i]) / ynext[i])
                if fault > maxfault:
                    maxfault = fault
            if maxfault < 1:
                break
            ycur = ynext
        res.append(ynext)
        ti += t
        flag = 0
        for i in range(N):
            if fabs((y[i] - ynext[i]) / ynext[i]) < 1e-4:
                flag = 1
        if flag:
            break
        y = ynext
    return res, ti

def work():
    global cc, dd
    cc, dd = get_consts()
    res, ti = iterations()
    return res, ti