import turtle

def main():
    window = turtle.Screen()#abre una ventana
    dave = turtle.Turtle()#genermaos tortuga

    make_square(dave)#haze un cuadrado

    turtle.mainloop()#para que no se cierre la ventana

def make_square(dave):
    length = int(input('Tamano de cuadrado: '))

    for i in range(4):
        make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)

if __name__ == '__main__':
    main()
