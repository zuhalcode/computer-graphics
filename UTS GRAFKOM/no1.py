from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import math

# Bresenham's algorithm
def drawCircle(x, y, r):
    glBegin(GL_POINTS)
    for i in range(0, 360):
        theta = 2.0 * 3.1415926 * i / 360
        glVertex2f(x + r * math.cos(theta), y + r * math.sin(theta))
    glEnd()

def setPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 200.0, 0.0, 200.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    drawCircle(100, 100, 50)
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Lab")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()

