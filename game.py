def draw():
    xy1.move(aim1)
    head1 = xy1.copy()
    xy2.move(aim2)
    head2 = xy2.copy()

    if not inside(head1) or head1 in body2:
        print('Blue Player Wins!')
        return

    if not inside(head2) or head2 in body1:
        print('Red Player Wins')
        return

    body1.add(head1)
    body2.add(head2)
    square(xy1.x, xy1.y, 3, 'red')
    square(xy2.x, xy2.y, 3, 'blue')
    update()
    ontimer(draw, 50)
