import sys
from sdl2 import *
from OpenGL.GL import *
from OpenGL.GL import shaders

class SsSdl:
    def __init__(self, width, height):
        SDL_Init(SDL_INIT_VIDEO)

        # Use OpenGL 3.1 core
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 1)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE)

        self.window = SDL_CreateWindow(
            b"SongShader", 
            SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, width, height, 
            SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN
            )
        self.context = SDL_GL_CreateContext(self.window)

        # Use Vsync
        SDL_GL_SetSwapInterval(1)

class SsGl:
    def __init__(self, width, height):
        resize(width, height)
        compileShaders()

    def compileShaders(self):
        self.vert_program = shaders.compileShader("""
            in vec2 VPos2D; 
            void main() {
               gl_Position = vec4( VPos2D.x, VPos2D.y, 0, 1 );
            }
            """, GL_VERTEX_SHADER)
        self.frag_program = shaders.compileShader("""
            void main() {
                gl_FragColor = vec4(0.0, 0.0, 0.0, 0.0);
            }
            """, GL_FRAGMENT_SHADER)
        self.shader = shaders.compileProgram(self.vert_program, self.frag_program)

    def resize(self, width, height):
        glViewPort(0, 0, width, height)

    def redraw(self):
        glBegin(GL_QUADS)
        glVertex2f(-1, -1)
        glVertex2f( 1, -1)
        glVertex2f(-1,  1)
        glVertex2f( 1,  1)
        glEnd()


class SsApp:
    def __init__(self, width, height):
        self.sdl = SsSdl(width, height)
        self.gl = SsGl(width, height)


if __name__ == '__main__':
    print("SongShader v0.1")
    app = SsApp(640, 480)
    input()
    sys.exit(main(sys.argv))