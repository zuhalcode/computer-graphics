import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def cylinder(radius, height, num_slices):
    r = radius
    h = height
    n = float(num_slices)
    circle_pts = []

    for i in range(int(n) + 1):
        # menentukan sudut
        angle = 2 * math.pi * (i/n)

        # menentukan titik
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)

    # menggambar lingkaran bagian belakang
    glBegin(GL_TRIANGLE_FAN) 
    glColor(1, 1, 1)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
    glEnd()

    # menggambar lingkaran bagian depan
    glBegin(GL_TRIANGLE_FAN) 
    glColor(1, 1, 1)
    # menggambar titik pusat
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = -h/2.0
        glVertex(x, y, z)
    glEnd()

    # menggambar selimut 
    glBegin(GL_TRIANGLE_STRIP) 
    glColor(1, 1, 0)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
        glVertex(x, y, -z)
    glEnd()


def main():
    # inisialisasi pygame
    pygame.init()
    (width, height) = (800, 600)
    # mengatur resolusi display layar
    screen = pygame.display.set_mode((width, height), OPENGL | DOUBLEBUF)
    # kecepatan rotasi
    rotation = 0.0
    # mengatur posisi awal
    x = 0.0
    y = 0.0
    z = -60

    while True:
        # menambah kecepatan rotasi
        rotation += 1

        # membersihkan background dengan warna hitam
        glClear(GL_COLOR_BUFFER_BIT)
        glClear(GL_DEPTH_BUFFER_BIT)

        # mengaktifkan memory depth buffer
        glEnable(GL_DEPTH_TEST)

        # mengatur proyeksi matriks
        glMatrixMode(GL_PROJECTION)

        # mereset matriks proyeksi 
        glLoadIdentity()

        # menyiapkan perspektif matriks proyeksi 
        gluPerspective(45, float(width)/height, 1, 100)

        # mengatur posisi kamera
        glTranslatef(x,y,z)

        # mengatur ke mode matriks modelview
        glMatrixMode(GL_MODELVIEW)
        
        # mereset matriks proyeksi 
        glLoadIdentity()

        # apabila ditekan tombol x, maka program akan berhenti.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            # apabila ditekan arah panah atas bergerak ke atas
            if event.key == pygame.K_UP:
                y += .5
            # apabila ditekan arah panah bawah bergerak ke bawah
            if event.key == pygame.K_DOWN:
                y -= .5
            # apabila ditekan arah panah kiri bergerak ke kiri
            if event.key == pygame.K_LEFT:
                x -= .5
            # apabila ditekan arah panah kanan bergerak ke kanan
            if event.key == pygame.K_RIGHT:
                x += .5
        
        # mengatur rotasi kamera
        glRotate(rotation, 0, 1, 0)

        # menggambar objek
        cylinder(5, 20, 50)

        # menampilkan gambar
        pygame.display.flip()
        
        # menunggu 1s sebelum looping lagi
        pygame.time.Clock().tick(100)
main()