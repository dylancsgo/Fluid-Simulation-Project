# Dylan Swanson
# FluidSim PT.2
# Starting June 2, 2024
# Reference: https://mikeash.com/pyblog/fluid-simulation-for-dummies.html
''' Revised version of my January 2024 fluid simulation program. 
    This time following the structure outlined by Mike Ash in his "Fluid
    Simulation for Dummies" paper. I followed the Coding Train coding challenge
    #132 for rendering the code.'''

from Fluid import *
pygame.init()

# Set up the window
screen = pygame.display.set_mode((N*SCALE,N*SCALE))#spacingScale = N*SCALE + spacing*(N+1)
pygame.display.set_caption("Fluid Simulator")
screen.fill((0,0,0))
pmouse_x = 0
pmouse_y = 0
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pmouse_x, pmouse_y = mouse_x, mouse_y
            mouse_x, mouse_y = pygame.mouse.get_pos()
            delta_x = mouse_x - pmouse_x
            delta_y = mouse_y - pmouse_y
            Add_Density(int(mouse_x/SCALE), int(mouse_y/SCALE), 10*SCALE)
            Add_Velocity(int(mouse_x/SCALE), int(mouse_y/SCALE), delta_x, delta_y)
   
    Step()
    Render(screen)

    pygame.display.flip()

pygame.quit()
