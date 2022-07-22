def Adollar(x, y):  # conversion from american dollar to any other currency
    data = {'canadiandollar': 1.49, 'australiandollar': 1.43, 'yen': 134.19, 'rupees': 78.04, 'americandollar': 1,
            'euros': 0.9, 'ruble': 56.55, "pound": 0.82}
    for i in data:
        if i == x:
            temp = data[i]

    return y * float(temp)


def Rupees(x, y):  # conversion from rupees to any other currency
    data = {'canadiandollar': 0.017, 'australiandollar': 0.018, 'yen': 1.72, 'americandollar': 0.013, 'rupees': 1,
            'euros': 0.013, 'ruble': 0.72, "pound": 0.010}
    for i in data:
        if i == x:
            temp = data[i]

    return y * float(temp)


def Cdollar(x, y):  # conversion from canadian dollar to any other currency
    data = {"americandollar": 1.01, "australiandollar": 1.11, "yen": 103.58, "canadiandollar": 1, "euros": 0.73,
            "ruble": 41.44, "rupees": 59.81, "pound": 0.63}
    for i in data:
        if i == x:
            temp = data[i]

    return y * float(temp)


def Ausdollar(x, y):  # conversion from australian dollar to any other currency
    data = {"americandollar": 0.69, "canadiandollar": 0.90, "yen": 93.53, "australiandollar": 1, "euros": 0.66,
            "ruble": 37.42, "rupees": 54, "pound": 0.57}
    for i in data:
        if i == x:
            temp = data[i]

    return y * float(temp)


def Yen(x, y):  # conversion from yen to any other currency
    data = {"americandollar": 0.01, "canadiandollar": 0.01, "australiandollar": 0.01, "yen": 1, "euros": 0.01,
            "ruble": 0.41, "rupees": 0.58, "pound": 0.0061}
    for i in data:
        if i == x:
            temp = data[i]

    return y * float(temp)


def Euros(x, y):  # conversion from euros to any other currency
    data = {"americandollar": 1.05, "canadiandollar": 1.37, "australiandollar": 1.51, "euros": 1, "yen": 142,
            "ruble": 59.97, "rupees": 81.82, "pound": 0.86}
    for i in data:
        if i == x:
            temp = data[i]

    return y * float(temp)


def Ruble(x, y):  # conversion from ruble to any other currency
    data = {"americandollar": 0.017, "canadiandollar": 0.022, "australiandollar": 0.024, "ruble": 1, "yen": 2.29,
            "euros": 0.016, "rupees": 1.32, "pound": 0.014}
    for i in data:
        if i == x:
            temp = data[i]
    return y * float(temp)


def Pound(x, y):  # conversion from pound to any other currency
    data = {"americandollar": 1.22, "canadiandollar": 1.59, "australiandollar": 1.79, "ruble": 66, "yen": 164.98,
            "euros": 164.98, "rupees": 95.27, "pound": 1}
    for i in data:
        if i == x:
            temp = data[i]

    return y * float(temp)


def currency_conversion(currency_1, currency_2, capital):
    if currency_1 == 'americandollar':
        return Adollar(currency_2, capital)

    elif currency_1 == 'rupees':
        return Rupees(currency_2, capital)

    elif currency_1 == "canadiandollar":
        return Cdollar(currency_2, capital)

    elif currency_1 == "australiandollar":
        return Ausdollar(currency_2, capital)

    elif currency_1 == "yen":
        return Yen(currency_2, capital)

    elif currency_1 == "euros":
        return Euros(currency_2, capital)

    elif currency_1 == "ruble":
        return Ruble(currency_2, capital)

    elif currency_1 == "pound":
        return Pound(currency_2, capital)


def fixcasing(x):  # to remove spaces and make all the letters to lower case
    x = x.replace('+) ', '')  # removes the unnecessary elements in string
    x = x.replace(' ', '')
    x = x.lower()
    return x


import tkinter as tk

currencies = ['+) American Dollar', '+) Canadian dollar', '+) Australian Dollar', '+) Yen', '+) Euros', '+) Rupees',
              '+) Pound', '+) Ruble']

win = tk.Tk()
win.title('Currency Exchange :')

canvas = tk.Canvas(win, width=750, height=350, relief='raised')
canvas.pack()

menu_variable1 = tk.StringVar(win)
menu_variable1.set('Select')

menu_variable2 = tk.StringVar(win)
menu_variable2.set('Select')

heading = tk.Label(text='WELCOME TO RADIANT CURRENCY EXCHANGE', fg="red")
heading.config(font=('helvetica', 16))
canvas.create_window(370, 30, window=heading)

subheading = tk.Label(win, text='   TRANSACTION RECEIPT\nThe currencies available for exchange are:\n')
subheading.config(font=('helvetica', 14))
canvas.create_window(350, 100, window=subheading)

statement1 = tk.Label(win, text='Select the currency you want to convert :')
statement1.config(font=('helvetica', 14))
canvas.create_window(300, 150, window=statement1)

cur1 = tk.OptionMenu(win, menu_variable1, *currencies)
canvas.create_window(550, 150, window=cur1)

statement2 = tk.Label(win, text='Select the currency you wish to convert to :')
statement2.config(font=('helvetica', 14))
canvas.create_window(290, 190, window=statement2)

cur2 = tk.OptionMenu(win, menu_variable2, *currencies)
canvas.create_window(550, 190, window=cur2)

capital = tk.Label(win, text='Enter the amount :')
capital.config(font=('helvetica', 14))
canvas.create_window(330, 230, window=capital)

entry1 = tk.Entry(win)
canvas.create_window(550, 230, window=entry1)


def Conversion():
    currency_1 = menu_variable1.get()
    currency_1 = fixcasing(currency_1)

    currency_2 = menu_variable2.get()
    currency_2 = fixcasing(currency_2)

    capital = entry1.get()
    capital = float(capital)

    final = currency_conversion(currency_1, currency_2, capital)

    result = tk.Label(win, text=('The Amount Would be : {} {}'.format(str(final), currency_2)))
    result.config(font=('halvetica', 14))
    canvas.create_window(350, 320, window=result)

    # end


button1 = tk.Button(text='Convert', command=Conversion, bg='brown', fg='white', font=('helvetica', 9))
canvas.create_window(350, 280, window=button1)

win.mainloop()
