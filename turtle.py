import turtle
import functools
from functools import partial
from turtle import Turtle

def iterate(s):
    res = []
    
    for sym in s:
        if sym == 'G':
            res.append('GG')
        elif sym == 'F':
            res.append('F-G+F+G-F')
        else:
            res.append(sym)
    
    return ''.join(res)


def iter_n(s, n, f):
    if n == 0:
        return s
    
    return iter_n(f(s), n-1, f)

def iter_rule(s, rules):
    res = []

    for i in s:
        flag = False
        for left, right in rules:
            if i == left:
                res.append(right)
                flag = True
                break

        if not flag:
            res.append(i)
    return ''.join(res)


def t(s, n):
    length = 200 / n
    bob = turtle.Turtle()
    bob.speed(500)
    for i in s:
        if i == 'G' or i == 'F':
            bob.forward(length)

        if i == '-':
            bob.right(120)

        if i == '+':
            bob.left(120)
    
    turtle.done()


def draw(s, draw_rules):
    bob = Turtle()
    bob.speed(10000)

    for i in s:
        if i in draw_rules:
            f = draw_rules[i]
            f(bob)

    turtle.done()


serp_rules = [('F','F-G+F+G-F'), ('G','GG')]
dragon_rules = [('X','X+YF+'), ('Y','-FX-Y')]

dragon_draw_rules = {
    'F' : partial(Turtle.forward, distance=15),
    '-' : partial(Turtle.left, angle=90),
    '+' : partial(Turtle.right, angle=90)
}

tri_draw_rules = {
    'F' : partial(Turtle.forward, distance=15),
    'G': partial(Turtle.forward, distance=15),
    '-' : partial(Turtle.right, angle=120),
    '+' : partial(Turtle.left, angle=120)
}


dragon = functools.partial(iter_rule, rules=dragon_rules)

serpinski = functools.partial(iter_rule, rules=serp_rules)


s_dragon = 'FX'
s_tri = 'F-G-G'

res = iter_n(s_dragon, 10, dragon)
draw(res, dragon_draw_rules)

# print(s6)
#
# res = iter_n(s_tri, 4, serpinski)
# draw(res, tri_draw_rules)
