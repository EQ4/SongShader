import sys
from sdl2 import *
from OpenGL.GL import *

class SsGl:
    def __init__(self):
        glOrtho(-1.0, 1.0, 1.0, 1.0, -1.0, 1.0)

    def resize(self, width, height):
        glViewPort(0, 0, width, height)

    def redraw(self):
        glBegin(GL_QUADS)
        glVertex3f(-1, -1, 0)
        glVertex3f( 1, -1, 0)
        glVertex3f(-1,  1, 0)
        glVertex3f( 1,  1, 0)
        glEnd()


class SsSdl:
    def __init__(self):
        SDL_Init(SDL_INIT_EVERYTHING)
        SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
        self.screen = SDL_SetVideoMode(800, 600, 32, SDL_OPENGL)
        SDL_WM_SetCaption("SongShader")

class SsApp:
    def __init__(self):
        self.gl = SsGl()
        self.sdl = SsSdl()


if __name__ == '__main__':
    print("SongShader v0.1")
    app = SsApp()
    input()
    sys.exit(main(sys.argv))