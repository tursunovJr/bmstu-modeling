from math import ceil, sqrt

# Вывод результата разной природы в формате строки
def output(s):
    if type(s) == float:
        if s > 1000000:
            return '{:.8e}'.format(s)
        return '{:.8f}'.format(s)
    elif type(s) == int:
        return str(s)
    else:
        return s

def func(x, u):
    return x ** 2  + u ** 2

# Явный Эйлера
def euler(n, h, x, y):
    y_out = []
    for i in range(n):
        try:
            y += h * func(x, y)
            y_out.append(y)
            x += h
        except OverflowError:
            y_out.append('overflow')
            for _ in range(i, n-1):
                y_out.append('-----')
            break
    return y_out

# Неявный Эйлера
def implicit_euler(n, h, x, y):
    y_out = [y]
    for i in range(n):
        D = 1 - 4*h*(y + h*((x + h)**2))
        if D < 0:
            y_out.append('D < 0')
            for _ in range(i, n-2):
                y_out.append('-----')
            break
        y = (1 - sqrt(D)) / (2*h) # берем корень с минусом
        x += h
        y_out.append(y)
    return y_out
# def Picar3(x):
#     y = pow(x, 3) / 3
#     tmp = 1 + pow(x, 4) / 21
#     tmp += 2 * pow(x, 3) / (693)
#     tmp += pow(x, 12) / (19845)
#     return y*tmp


# def Picar4(x):
#     y = pow(x, 31)/109876902975
#     y += 2 * pow(x, 23) / 86266215
#     y += 2 * pow(x, 22) / 1361505915
#     y += 2 * pow(x, 19) / 3393495
#     y += pow(x, 15) / 59535
#     y += 2 * pow(x, 14) / 916839
#     y += pow(x, 13) / 56189133
#     y += 2 * pow(x, 11)/2079
#     y += 2 * pow(x, 10)/31185
#     y += 2 * pow(x, 7)/63
#     y += pow(x, 3) / 3
#     return y

# def union(n, h, x, y0):
#     y_out = [[y0, y0]]
#     for _ in range(n):
#         y_f3 = Picar3(x)
#         y_f4 = Picar4(x)
#         y_out.append([y_f3, y_f4])
#         x += h
#     return y_out
# Пикар
def picar(n, h, x, y0):
    def f1(a):
        return a ** 3 / 3
    def f2(a):
        return f1(a) + a ** 7 / 63
    def f3(a):
        return f2(a) +  (a ** 11) * (2 / 2079) + (a ** 15) / 59535
    def f4(a, f3):
        return f3 + (a ** 15)*(2 / 93555) + (a ** 19)*(2 / 3393495) + (a ** 19)*(2 / 2488563) + \
    (a ** 23)*(2 / 86266215) + (a ** 23)*(1 / 99411543) + (a ** 27)*(2 / 3341878155) + (a ** 31)*(1 / 109876902975)

    y_out = [[y0, y0, y0, y0]]
    for i in range(n-1):
        x += h
        y_f1 = f1(x)
        y_f2 = f2(x)
        y_f3 = f3(x)
        y_out.append([y_f1, y_f2, y_f3, f4(x, y_f3)])
    return y_out
        

def work():
    h = 10 ** -5 # 10**-5 это хороший шаг для численных методов
    
    x = 0
    y0 = 0
    end = 2

    n = ceil(abs(end - x)/h)+1 # количество повторений

    x_arr = [x + h*i for i in range(n)]
    y1 = euler(n, h, x, y0)
    y2 = implicit_euler(n, h, x, y0)
    y3 = picar(n, h, x, y0)

    print("|    x    |   Пикар 1     |    Пикар 2    |   Пикар 3     |    Пикар 4    |     Явный     |    Неявный    |")
    print("-"*107)
    output_step = int(n/100) # выводим только 100 значений в таблице 
    for i in range(0, n, output_step):
        print("|{:^9.5f}|{:^15.8f}|{:^15.8f}|{:^15.8f}|{:^15.8f}|{:^15s}|{:^15s}|".format(x_arr[i],y3[i][0],y3[i][1],y3[i][2],y3[i][3],output(y1[i]),output(y2[i])))


work()