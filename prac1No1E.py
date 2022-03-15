from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 2.0, 0.0)
    glVertex2f(-5,-5)
    glVertex2f(0,0)
    glVertex2f(1,2)
    

    glEnd()

    glutSwapBuffers()
    
glutInit(sys.argv)
glutInitWindowSize(500,500)
glutCreateWindow(b'Computer Graphics')
glutDisplayFunc(draw)
glutMainLoop()