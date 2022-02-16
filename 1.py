import random

def check_horizontal(box):
    for i in range(3): 
        for y in range(3):
            if box[i][0][y]==box[i][1][y]==box[i][2][y]==True:
                return True
            
def check_vertical(box):
    for i in range(3):
        for y in range(3):
            if box[0][i][y]==box[1][i][y]==box[2][i][y]==True:
                return True
        
def check_diagonal(box):
    for i in range(3):
        if (box[0][0][i]==True)and(box[1][1][i]==True)and(box[2][2][i]==True):
            return True
        elif (box[0][2][i]==True)and(box[1][1][i]==True)and(box[2][0][i]==True):
            return True 

        
def check_horizontal_cl(box):
    for i in range(3):
        if (box[i][0][0]==box[i][1][1]==box[i][2][2]==True)or(box[i][0][2]==box[i][1][1]==box[i][2][0]==True):
            return True

def check_vertical_cl(box):
    for i in range(3):
        if box[0][i][0]==box[1][i][1]==box[2][i][2]==True:
            return True
        elif box[0][i][2]==box[1][i][1]==box[2][i][0]==True:
            return True
            
def check_diagonal_cl(box):
    if  (box[0][0][0]==True)and(box[1][1][1]==True)and(box[2][2][2]==True):
        return True
    elif (box[0][0][2]==True)and(box[1][1][1]==True)and(box[2][2][0]==True):
        return True
    elif (box[0][2][0]==True)and(box[1][1][1]==True)and(box[2][0][2]==True):
        return True
    elif(box[0][2][2]==True)and(box[1][1][1]==True)and(box[2][0][0]==True):
        return True

                


times=0

for i in range(100):
    kouti1=[False]*3
    kouti2=[False]*3
    kouti3=[False]*3
    kouti4=[False]*3
    kouti5=[False]*3
    kouti6=[False]*3
    kouti7=[False]*3
    kouti8=[False]*3
    kouti9=[False]*3

    grami1=[kouti1,kouti2,kouti3]
    grami2=[kouti4,kouti5,kouti6]
    grami3=[kouti7,kouti8,kouti9]

    game_ends=False
    box=[grami1,grami2,grami3]

    while game_ends==False:
        random_cyrcle=random.randrange(3)
        random_grami=random.randrange(3)
        random_kouti=random.randrange(3)
        if not box[random_grami][random_kouti][random_cyrcle]==False:
            times+=1
            box[random_grami][random_kouti][random_cyrcle]==True

            if not game_ends:
                game_ends=check_horizontal(box)
            if not game_ends:
                game_ends=check_vertical(box)
            if not game_ends:
                game_ends=check_diagonal(box)
            if not game_ends:
                game_ends=check_horizontal_cl(box)
            if not game_ends:
                game_ends=check_vertical_cl(box)
            if not game_ends:
                game_ends=check_diagonal_cl(box)
                
        



print ("avg of ending game ",times/100)











