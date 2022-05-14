import turtle


def oldinga():
    tosh.pencolor(ranglar[rang])
    tosh.forward(100)


def chapga():
    tosh.left(45)


def onga():
    tosh.right(45)


def ochirish():
    global orqaRang
    tosh.pencolor(ranglar[orqaRang])
    tosh.back(100)


def qalin():
    global size
    size += 1
    tosh.pensize(size)


def kichraytirish():
    global size
    size -= 1
    if size > 0:
        tosh.pensize(size)
    else:
        size = 1
        tosh.pensize(size)


def color():
    global rang
    if rang > 5:
        rang = 0
    else:
        rang += 1
    tosh.pencolor(ranglar[rang])


def uzish():
    global qoyish
    if qoyish == 1:
        tosh.penup()
        qoyish = 0
    elif qoyish == 0:
        tosh.pendown()
        qoyish = 1


def orqafon():
    global orqaRang
    if orqaRang > 5:
        orqaRang = 0
    else:
        orqaRang += 1
    wn.bgcolor(ranglar[orqaRang])


def clear():
    tosh.clear()


def malumot(tekst, x, y):
    tanish = turtle.Turtle()
    tanish.hideturtle()
    tanish.penup()
    tanish.goto(x, y)
    tanish.write(tekst, font=10)


def main():
    global tosh
    global size
    global rang
    global orqaRang
    global ranglar
    global qoyish
    global wn

    qoyish = 1

    ranglar = ['green', 'red', 'pink', 'blue', 'yellow', 'white', 'black']

    rang = 0

    orqaRang = 0

    size = 1

    wn = turtle.Screen()
    wn.setup(900, 600)
    wn.title('salom ketmonjonlar')
    wn.bgcolor('orange')

    tosh = turtle.Turtle()
    tosh.pensize(size)

    malumot('oldinga yurish -> w', 450, 350)
    malumot('orqaga yurish yurish -> s', 450, 325)
    malumot('o\'nga -> d', 450, 300)
    malumot('chapga -> a', 450, 275)
    malumot('sakrash -> probel', 450, 250)
    malumot('yozuvni rangini o\'zgartirish -> f', 450, 225)
    malumot('ma\'lumotni tozalash -> c', 450, 200)
    malumot('orqa fonni o\'zgartirish -> b', 450, 175)

    wn.onkey(oldinga, 'w')
    wn.onkey(chapga, 'a')
    wn.onkey(onga, 'd')
    wn.onkey(ochirish, 's')
    wn.onkey(qalin, 'q')
    wn.onkey(kichraytirish, 'e')
    wn.onkey(color, 'f')
    wn.onkey(uzish, 'space')
    wn.onkey(orqafon, 'b')
    wn.onkey(clear, 'c')

    wn.listen()
    wn.mainloop()


main()
