import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def Draw(vertices, edges):
    glColor(1,1,1) # Draw in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

forced = False

def Tetrahedron():
    d = math.sqrt(3)/3
    vertices = ((d, d, -d), (-d, -d, -d), (d, -d, d), (-d, d, d))

    edges = ((0,1), (0,2), (0,3), (1,2), (1,3), (2,3))
    
    surfaces = ((0,3,1), (0,2,3), (0,1,2), (1,3,2))
    
    texture = [((15/1200,675/800),(85/1200,770/800),(135/1200,670/800)), 
               ((185/1200,675/800),(245/1200,780/800),(300/1200,675/800)), 
               ((350/1200,675/800),(400/1200,780/800),(450/1200, 675/800)), 
               ((505/1200,675/800),(560/1200,780/800),(600/1200, 675/800))]
    
    #normals = ()
    
    for surface_index,surface in enumerate(surfaces):
        glBegin(GL_POLYGON)
        for vertex_index,vertex in enumerate(surface):
            glTexCoord2fv(texture[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
        glEnd()
    
    Draw(vertices, edges)
    
    
def Octohedron():
    vertices = ((1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 1, 0),(0, 0, 1), (0, 0, -1))

    edges = ((0,1), (0,3), (0,4), (0,5), (1,2), (1,4), (1,5), (2,3),(2,4), (2,5), (3,4), (3,5))
    
    surfaces = ((0,1,4),(0,5,1),(0,4,3),(0,3,5),(1,2,4),(1,5,2),(2,3,4),(2,5,3),)
    
    texture = [((15/1200,675/800),(85/1200,770/800),(135/1200,675/800)), 
               ((185/1200,675/800),(245/1200,780/800),(300/1200,675/800)), 
               ((350/1200,675/800),(400/1200,780/800),(450/1200, 675/800)),
               ((500/1200,670/800),(560/1200,785/800),(605/1200, 670/800)), 
               ((665/1200,675/800),(710/1200,780/800),(765/1200,675/800)), 
               ((820/1200,670/800),(875/1200,780/800),(930/1200,670/800)),
               ((965/1200,675/800),(1025/1200,780/800),(1070/1200,675/800)), 
               ((25/1200,510/800),(75/1200,615/800),(125/1200,510/800))]
    
    #normals = ()
    
    for surface_index,surface in enumerate(surfaces):
        glBegin(GL_POLYGON)
        for vertex_index,vertex in enumerate(surface):
            glTexCoord2fv(texture[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
        glEnd()
    
    Draw(vertices, edges)
    
    
def Icosahedron():
    phi = (1 + math.sqrt(5))/2
    k = 1/math.sqrt(1+phi**2)
    vertices = ((k, 0, phi*k), (-k, 0, phi*k),
                (phi*k, k, 0), (phi*k, -k, 0),
                (0, -phi*k, k), (0, -phi*k, -k), 
                (-phi*k, k, 0), (-phi*k, -k, 0),
                (0, phi*k, k), (0, phi*k, -k),
                (k, 0, -phi*k), (-k, 0, -phi*k))

    edges = ((0,1), (0,2), (0,3), (0,4), (0,8), (1,4), (1,6), (1,7),
             (1,8), (2,3), (2,8), (2,9), (2,10), (3,4), (3,5), (3,10),
             (4,5), (4,7), (5,7), (5,10), (5,11), (6,7), (6,8), (6,9),
             (6,11), (7,11), (8,9), (9,10), (9,11), (10,11))
    
    surfaces = ((0,4,1),(0,1,8),(0,3,4),(0,2,3),(0,8,2),(7,1,4),(2,10,3),(2,8,9),
                (2,9,10),(1,7,6),(1,6,8),(8,6,9),(3,10,5),(3,5,4),(4,5,7),(5,11,7),
                (6,7,11),(6,11,9),(9,11,10),(10,5,11))
    
    texture = [((15/1200,675/800),(85/1200,770/800),(135/1200,675/800)),
               ((185/1200,675/800),(245/1200,780/800),(300/1200,675/800)), 
               ((350/1200,675/800),(400/1200,780/800),(450/1200, 675/800)),
               ((500/1200,670/800),(560/1200,785/800),(605/1200, 670/800)), 
               ((660/1200,675/800),(710/1200,780/800),(765/1200,675/800)), 
               ((815/1200,670/800),(875/1200,780/800),(930/1200,670/800)),
               ((965/1200,675/800),(1025/1200,780/800),(1070/1200,675/800)), 
               ((20/1200,515/800),(75/1200,615/800),(125/1200,515/800)), 
               ((180/1200,495/800),(240/1200,620/800),(300/1200,495/800)),
               ((335/1200,510/800),(395/1200,625/800),(460/1200,510/800)), 
               ((495/1200,515/800),(555/1200,630/800),(625/1200,515/800)), 
               ((655/1200,515/800),(715/1200,635/800),(790/1200,515/800)),
               ((810/1200,515/800),(875/1200,635/800),(940/1200,515/800)),
               ((960/1200,520/800),(1030/1200,625/800),(1100/1200,520/800)),
               ((20/1200,340/800),(90/1200,450/800),(165/1200,340/800)),
               ((180/1200,345/800),(240/1200,450/800),(315/1200,345/800)), 
               ((325/1200,345/800),(395/1200,455/800),(465/1200,345/800)), 
               ((500/1200,345/800),(560/1200,450/800),(640/1200,345/800)),
               ((665/1200,345/800),(720/1200,450/800),(780/1200,345/800)),
               ((820/1200,345/800),(885/1200,450/800),(960/1200,345/800))]
    
    #normals = ()
    
    for surface_index,surface in enumerate(surfaces):
        glBegin(GL_POLYGON)
        for vertex_index,vertex in enumerate(surface):
            glTexCoord2fv(texture[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
        glEnd()

    Draw(vertices, edges)
    

def Dodecahedron():
    phi = (1 + math.sqrt(5))/2
    x = 1/math.sqrt(3)
    
    texture =  [((40/1200,670/800), (25/1200,700/800), (80/1200,770/800), (135/1200,700/800), (110/1200,670/800)),
                ((210/1200,660/800), (190/1200,715/800), (240/1200,770/800), (300/1200,715/800), (280/1200,660/800)),
                ((365/1200,675/800), (350/1200,720/800), (400/1200,760/800), (450/1200,720/800), (430/1200,675/800)),
                ((525/1200,680/800), (505/1200,725/800), (555/1200,770/800), (605/1200,725/800), (590/1200,680/800)),
                ((680/1200,670/800), (660/1200,725/800), (710/1200,770/800), (760/1200,725/800), (740/1200,670/800)),
                ((840/1200,670/800), (825/1200,725/800), (870/1200,760/800), (920/1200,725/800), (910/1200,670/800)),
                ((990/1200,670/800), (965/1200,725/800), (1025/1200,770/800), (1065/1200,725/800), (1040/1200,670/800)),
                ((45/1200,520/800), (30/1200,565/800), (75/1200,600/800), (125/1200,565/800), (105/1200,520/800)),
                ((205/1200,520/800), (190/1200,565/800), (240/1200,600/800), (290/1200,565/800), (275/1200,520/800)),
                ((360/1200,520/800), (345/1200,565/800), (395/1200,600/800), (450/1200,565/800), (430/1200,520/800)),
                ((515/1200,515/800), (500/1200,565/800), (555/1200,610/800), (615/1200,565/800), (605/1200,515/800)),
                ((680/1200,520/800), (665/1200,565/800), (715/1200,610/800), (775/1200,565/800), (760/1200,520/800))]

    Vertices = ((x, x, x), (x, x, -x), (x, -x, x), (x, -x, -x),
                (-x, x, x), (-x, x, -x),(-x, -x, x), (-x,-x,-x),
                (0, x/phi, x*phi), (0, x/phi, -x*phi),
                (0, -x/phi, x*phi), (0, -x/phi, -x*phi),
                (x/phi, x*phi, 0), (x/phi, -x*phi, 0),
                (-x/phi, x*phi, 0), (-x/phi, -x*phi, 0),
                (x*phi, 0, x/phi), (x*phi, 0, -x/phi),
                (-x*phi, 0, x/phi), (-x*phi, 0, -x/phi))

    Edges = ((0,8), (0,16), (8,10), (10,2), (2,16),(0,12), (12,14), (14,4), (4,8), (16,17),
             (17,1), (1,12), (10,6), (6,15), (15, 13),(13, 2), (4,18), (18,6), (18,19), (19,7), 
             (7,15), (7,11), (11,9), (9,5), (5,14), (5,19),(17,3), (13, 3), (1,9), (11,3))

    Surfaces = ((0,16,2,10,8),(14,12,0,8,4),(12,1,17,16,0),(16,17,3,13,2),(9,11,3,17,1),(10,2,13,15,6),
                (14,5,9,1,12),(18,19,5,14,4),(13,3,11,7,15),(4,8,10,6,18),(15,7,19,18,6),(11,9,5,19,7),)
    
    for surface_index,surface in enumerate(Surfaces):
        glBegin(GL_POLYGON)
        for vertex_index,vertex in enumerate(surface):
            glTexCoord2fv(texture[surface_index][vertex_index])
            
            glVertex3fv(Vertices[vertex])
        glEnd()
    
    Draw(Vertices, Edges)
    

def Cube():
    vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
                (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))

    edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4),
             (6,7), (5,1), (5,4), (5,7))

    texture = [((30/1200,660/800), (125/1200,660/800), (125/1200,755/800), (30/1200,755/800)),
               ((190/1200,670/800), (290/1200,670/800), (290/1200,760/800), (190/1200,760/800)),
               ((345/1200,665/800), (445/1200,665/800), (445/1200,765/800), (345/1200,765/800)),
               ((505/1200,670/800), (600/1200,670/800), (600/1200,765/800), (505/1200,765/800)),
               ((660/1200,670/800), (760/1200,670/800), (760/1200,760/800), (660/1200,760/800)),
               ((820/1200,655/800), (930/1200,655/800), (930/1200,760/800), (820/1200,760/800))]

    surfaces = ((1,0,3,2),(2,3,6,7),(7,6,4,5),(5,4,0,1),(5,1,2,7),(0,4,6,3))
    
    colors = ((1,0,1), (0, 1, 1), (1, 0, 1), (0,1,1))
    
    normals = [( 0,  0, -1),  # surface 0
               (-1,  0,  0),  # surface 1
               ( 0,  0,  1),  # surface 2
               ( 1,  0,  0),  # surface 3
               ( 0,  1,  0),  # surface 4
               ( 0, -1,  0)   # surface 5
              ]
    
    #glBegin(GL_QUADS)
    #for surface_index,surface in enumerate(surfaces):
    #    for vertex_index,vertex in enumerate(surface):
    #        glTexCoord2fv(texture[surface_index][vertex_index])
    #        glVertex3fv(vertices[vertex])
    #glEnd()
    for i_surface, surface in enumerate(surfaces):
        glBegin(GL_QUADS)
        glNormal3fv(normals[i_surface])
        for i_vertex, vertex in enumerate(surface):
            index = (i_surface+i_vertex) % 2
            glTexCoord2fv(texture[i_surface][i_vertex])
            glColor3fv(colors[i_vertex])
            glVertex3fv(vertices[vertex])
        glEnd()
    
    Draw(vertices, edges)

def loadTexture():
    textureSurface = pygame.image.load('numbers.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()
    
    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
    0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    return texid


pygame.init()
display = (800, 800)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

loadTexture()

run = True
angle = 0 # Rotation angle about the vertical axis
glColor(1,1,1,1)
shape = Cube

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: # Capture an escape key press to exit
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
# init model view matrix
    glLoadIdentity()
# apply view matrix
    glMultMatrixf(viewMatrix)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    glColor(1,1,1,1)
    tilt = 1 + 22 * math.cos(angle * math.pi/180) # Tilt as we rotate 
    glRotate(tilt, 1, 1, 0) # Tilt a bit to be easier to see
    angle = (angle + 1) % 360
    glRotatef(angle, 0, 0, 1) # Rotate around the box's vertical axis
    
    keys = pygame.key.get_pressed() # Get pressed keys

    options = {pygame.K_1:Tetrahedron, pygame.K_2:Cube, pygame.K_3:Octohedron,
               pygame.K_4:Dodecahedron, pygame.K_5:Icosahedron}
    
    for key,value in options.items():
        if keys[key]:
            shape = value
            
    shape()
    
    glColor4f(0.5, 0.5, 0.5, 1)
    glBegin(GL_QUADS)
    glVertex3f(-10, -10, -2)
    glVertex3f(10, -10, -2)
    glVertex3f(10, 10, -2)
    glVertex3f(-10, 10, -2)
    glEnd()
    
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(20)

pygame.quit()
