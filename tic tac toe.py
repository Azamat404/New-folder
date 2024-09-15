import pygame
import random
width,height=300,300
window=pygame.display.set_mode((300,300))
pygame.display.set_caption("Tic Tac Toe")
pygame.init()
white,black=(255,255,255),(0,0,0)
FPS_clock=pygame.time.Clock()
fps=30
running=True
field=[[" "," "," "],[" "," "," " ],[" "," "," "]]
def make_random_move():
    empty_cells= [(i,j) for i in range(3) for j in range(3) if field[i][j]==" "]
    if empty_cells:
        move=random.choice(empty_cells)
        field[move[0]][move[1]]="O"
def check_winner(symbol):
    if field[0][0]==field[1][1]==field[2][2]==symbol:
        return True
    elif  field[0][2]==field[1][1]==field[2][0]==symbol:
        return True
    for I in range(3):
            if field[I][0]==field[I][1]==field[I][2]==symbol:
                return True
    for I in range(3):
            if field[0][I]==field[1][I]==field[2][I]==symbol:
                return True
    return False
def draw_tic_tac_toe():
    for row in range(3):
        for col in range(3):
            if field[row][col]=="X":
                pygame.draw.line(window, white, (col * 100 + 20, row * 100 + 20), (col * 100 + 80, row * 100 + 80), 3) 
                pygame.draw.line(window, white, (col * 100 + 80, row * 100 + 20), (col * 100 + 20, row * 100 + 80), 3)
            elif field[row][col]=="O":
                pygame.draw.circle(window, white, (col * 100 + 50, row * 100 + 50), 40, 3) 
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type== pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            row,col=pos[1]//100,pos[0]//100
            if field[row][col] == " ":
                field[row][col]= "X"
                print(field)
                make_random_move()
    window.fill(black)
    draw_tic_tac_toe()
    for i in range(1,3):
        pygame.draw.line(window, white, (i * 100, 0), (i * 100, height), 3)
        pygame.draw.line(window, white, (0, i * 100), (width, i * 100), 3)
    if check_winner("X"):
        pygame.display.set_caption("You won")
    elif check_winner("O"):
        pygame.display.set_caption("You lose")
    pygame.display.flip()
    FPS_clock.tick(fps)
    