from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-6, 6, -6, 6, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)

    glVertex2f(-5, -5)
    glVertex2f(5, -5)
    glVertex2f(0, 5)
    glVertex2f(-5, -5)

    glEnd()
    glutSwapBuffers()


glutInit(sys.argv)
glutInitWindowSize(500, 500)
glutInitWindowPosition(700,100)
glutCreateWindow("UTS PRAKTEK GRAFIKA KOMPUTER")
glutDisplayFunc(draw)
glutMainLoop()