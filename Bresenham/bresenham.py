from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# bresenham line drawing algorithm
def bresenham(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    dx = x2 - x1
    dy = y2 - y1
    d2 = 2 * (dx - dy)
    if m < 1 and m > 0:
        d1 = 2 * dy
        p = d1 - dx
        for x in range(x1, x2):
            p = p - d2 if(p >= 0) else p + d1
            y1 = y1 + 1 if(p >= 0) else y1
            glVertex2i(x, y1)
    elif(m > 1):
        d1 = 2 * dx
        p = d1 - dy
        for y in range(y1, y2):
            p = p + d2 if(p >= 0) else p - d1
            x1 = x1 + 1 if(p >= 0) else x1 
            glVertex2i(x1, y)

def display():
    # Membersihkan window
    glClear(GL_COLOR_BUFFER_BIT)
    # Menentukan Warna
    glColor3f(1.0, 1.0, 1.0)
    # Spesifikasikan diameter dari pixel yang akan digammbar
    glPointSize(7.0)
    # Memilih mode point
    glBegin(GL_POINTS)
    # Membuat titik
    bresenham(5,20,30,40)
    glEnd()
    glFlush()

def main():
    # Inisialisasi glut
    glutInit(sys.argv)
    # Inisialisasi tipe display glut
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # Inisialisasi ukuran layar
    glutInitWindowSize(500, 500)
    # Inisialisasi posisi window
    glutInitWindowPosition(100, 100)
    # inisialisasi pembuatan window
    glutCreateWindow(b"Bresenham's line algorithm")
    # Membersihkan layar dan memberikan warna background
    glClearColor(0.0, 0.0, 0.0, 0.0)
    # Set origin dari grid dan ukurannya 50 x 50
    gluOrtho2D(0, 50, 0, 50)
    # Memanggil fungsi display
    glutDisplayFunc(display)
    glutMainLoop()

main()
