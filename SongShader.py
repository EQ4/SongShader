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
        SDL_Init(SDL_INIT_VIDEO)

        # Use OpenGL 3.1 core
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 1)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE)

        self.window = SDL_CreateWindow(
            b"SongShader", 
            SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, 
            SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN
            )
        self.context = SDL_GL_CreateContext(self.window)

        # Use Vsync
        SDL_GL_SetSwapInterval(1)



class SsApp:
    def __init__(self):
        self.sdl = SsSdl()
        self.gl = SsGl()


if __name__ == '__main__':
    print("SongShader v0.1")
    app = SsApp()
    input()
    sys.exit(main(sys.argv))