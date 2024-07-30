import pygame
import random
import os
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#Game dimensions
screen_width = 720
screen_height = 480
current_directory = os.path.join(os.getcwd(),"game/boxgame/")
print(current_directory)
# --- Classes

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.basePos = (screen_width/2 - 68, screen_height - 232)
        self.image = pygame.image.load(os.path.join(current_directory, "conceptP1.png"))
        self.rect = pygame.rect.Rect(self.basePos, (10,10))
        self.health = 3
        self.leftDodge = False
        self.rightDodge = False
        self.leftPunch = False
        self.rightPunch = False
        self.canAttack = False
        self.rythmTimer = 1
        self.rythmPos = 2        
        self.dodgeDuration = 35 #in frames
        self.dbU = False #for debug player update
        
    def update(self):
        if self.dbU == False:
            print("update player")
            self.dbU = True
            
        if player.leftDodge == True and self.rightPunch == False and self.leftPunch == False:
            self.image = pygame.image.load(os.path.join(current_directory, "leftDodgeP1.png"))
            self.rect.x = self.basePos[0] - 40
        elif player.rightDodge == True and self.rightPunch == False and self.leftPunch == False:
            self.image = pygame.image.load(os.path.join(current_directory, "rightDodgeP1.png"))
            self.rect.x = self.basePos[0] + 40
        elif self.leftPunch == True:
            #print("punch?")
            self.image = pygame.image.load(os.path.join(current_directory, "leftPunchP1.png"))
        elif self.rightPunch == True:
            #print("punch?")
            self.image = pygame.image.load(os.path.join(current_directory, "rightPunchP1.png"))        
        else:
            self.image = pygame.image.load(os.path.join(current_directory, "conceptP1.png"))
            self.rect = pygame.rect.Rect(self.basePos, self.image.get_size())
            self.rythmTimer += 1
            if self.rythmTimer % 12 == 0:
                self.rect.y += self.rythmPos
                self.rythmPos *= -1            
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.basePos = (screen_width/2 - 68, screen_height - 350)
        self.image = pygame.image.load(os.path.join(current_directory, "conceptP2.png"))
        #self.rect = pygame.rect.Rect((screen_width/2 - 68, screen_height - 292), self.image.get_size()) <--- Original
        self.rect = pygame.rect.Rect(self.basePos, self.image.get_size())
        self.health = 7
        self.leftPunch = False
        self.rightPunch = False
        self.guard = False
        self.leftHint = False
        self.rightHint = False
        self.hintDuration = 25
        self.punchDuration = 25
        self.rythmTimer = 1
        self.rythmPos = 2
        self.isStunned = False
        self.dbU = False #for debug player update
        
    def update(self):
        if self.dbU == False:
            print("update enemy")
            self.dbU = True 
            
        if self.leftHint == True:
            self.image = pygame.image.load(os.path.join(current_directory, "leftHintP2.png"))
        elif self.rightHint == True:
            self.image = pygame.image.load(os.path.join(current_directory, "rightHintP2.png"))
        elif self.leftPunch == True:
            self.image = pygame.image.load(os.path.join(current_directory, "leftPunchP2.png"))
        elif self.rightPunch == True:
            self.image = pygame.image.load(os.path.join(current_directory, "rightPunchP2.png"))
        elif self.guard == True and self.isStunned == False:
            self.image = pygame.image.load(os.path.join(current_directory, "blockP2.png"))
        elif self.isStunned == True:
            self.image = pygame.image.load(os.path.join(current_directory, "stunP2.png"))
        else:
            self.image = pygame.image.load(os.path.join(current_directory, "conceptP2.png"))
            self.rythmTimer += 1
            if self.rythmTimer % 12 == 0:
                self.rect.y += self.rythmPos
                self.rythmPos *= -1
                
                

#player health bar
class HP(pygame.sprite.Sprite):
    def __init__(self, Player):
        super().__init__()    
        self.image = pygame.image.load(os.path.join(current_directory, "playerHP3.png"))
        self.rect = pygame.rect.Rect((100, 20), self.image.get_size())
        self.health = Player.health
        self.dbU = False #for debug player update
        
    #Update shows that you can change the sprite on the fly via conditions
    def update(self):
        #if self.dbU == False:
            #print("update heart")
            #self.dbU = True 
        if self.health == 2:
            self.dbU = False
            self.image = pygame.image.load(os.path.join(current_directory, "playerHP2.png"))
        elif self.health == 1:
            self.image = pygame.image.load(os.path.join(current_directory, "playerHP1.png"))
        elif self.health == 0:
            self.image = pygame.image.load(os.path.join(current_directory, "playerHP0.png"))
        elif self.health == 3:
            self.image = pygame.image.load(os.path.join(current_directory, "playerHP3.png"))

#Enemy health bar           
class HPE(pygame.sprite.Sprite): 
    def __init__(self,Enemy):
        super().__init__()    
        self.image = pygame.image.load(os.path.join(current_directory, "enemyHP7.png"))
        self.rect = pygame.rect.Rect((420, 20), self.image.get_size())
        self.health = Enemy.health
        self.dbU = False #for debug player update
    
    #Update shows that you can change the sprite on the fly via conditions
    def update(self):
       # if self.dbU == False:
            #print("update enemy heart")
            #self.dbU = True 
        if self.health == 6:
            self.dbU = False
            self.image = pygame.image.load(os.path.join(current_directory, "enemyHP6.png"))
        elif self.health == 5:
            self.image = pygame.image.load(os.path.join(current_directory, "enemyHP5.png"))
        elif self.health == 4:
            self.image = pygame.image.load(os.path.join(current_directory, "enemyHP4.png"))
        elif self.health == 3:
            self.image = pygame.image.load(os.path.join(current_directory, "enemyHP3.png"))
        elif self.health == 2:
            self.image = pygame.image.load(os.path.join(current_directory, "enemyHP2.png"))
        elif self.health == 1:
            self.image = pygame.image.load(os.path.join(current_directory, "enemyHP1.png"))
        elif self.health == 0:
            self.image = pygame.image.load(os.path.join(current_directory, "enemyHP0.png"))
        elif self.health == 7:
            self.image = pygame.image.load(os.path.join(current_directory, "enemyHP7.png"))             
                     
            

    
 
# --- Create the window
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen = pygame.display.set_mode([screen_width, screen_height])

# Set Background
background = pygame.image.load(os.path.join(current_directory, "gsC.jpg"))

# Set Music
pygame.mixer.pre_init(44100, 16, 2, 5000)
sound1 = pygame.mixer.Sound(os.path.join(current_directory,"theme.wav"))
sound1.set_volume(0.1)
channel1 = sound1.play(-1)

hit = pygame.mixer.Sound(os.path.join(current_directory,"hit.wav"))
hit2 = pygame.mixer.Sound(os.path.join(current_directory,"hit2.wav"))
hint = pygame.mixer.Sound(os.path.join(current_directory,"hint.wav"))
hint.set_volume(0.4)
block = pygame.mixer.Sound(os.path.join(current_directory,"block.wav"))
block.set_volume(0.3)
win = pygame.mixer.Sound(os.path.join(current_directory,"win.wav"))
gameover = pygame.mixer.Sound(os.path.join(current_directory,"gameover.wav"))
    
 
# --- Sprite list
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# Create player and enemy
player = Player()
enemy = Enemy()
playerHP = HP(player)
enemyHP = HPE(enemy)

all_sprites_list.add(playerHP)
all_sprites_list.add(enemyHP)
all_sprites_list.add(enemy)
all_sprites_list.add(player)

#Setting Hearts
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

noLivesTimer = 0
dodgeTimer = 0
hintTimer = 0
punchTimer = 0
canLoseHP = True
canLoseHPTimer = 0
stunTimer = 0
attackTimer = 0
gameOverTimer = 0
 
eventScreen = 0
seconds = 60
milliseconds = 0

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    key = pygame.key.get_pressed()
 
        #elif event.type == pygame.MOUSEBUTTONDOWN:
            #print("mouse button")
            #enemy.health -= 1
            #enemyHP.health = enemy.health
            #player.health -= 1
            #playerHP.health = player.health            
            #event with button
        
    #Eventscreen
    #Start Screen
    if eventScreen == 0:
        screen.fill(BLACK)
        font = pygame.font.SysFont(os.path.join(current_directory,"emulogic"), 20)
        text = font.render("Press enter to start game", True, WHITE)
        center_x = (screen_width // 2) - (text.get_width() // 2)
        center_y = (screen_height // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])
        
        pygame.display.flip()        
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            eventScreen = 1                   
              
    
    #Game Screen
    if eventScreen == 1:
        #CONTROLS: LEFT dodge left; RIGHT dodge right; UP attack
        key = pygame.key.get_pressed()
        if (player.rightDodge and player.leftDodge) == False:
            if key[pygame.K_LEFT]:
                player.leftDodge = True
                player.rightDodge = False
                dodgeTimer = 1
                print("leftDodge!")
            elif key[pygame.K_RIGHT]:
                player.rightDodge = True
                player.leftDodge = False
                dodgeTimer = 1
                print("rightDodge!")
            elif key[pygame.K_UP]:
                punch = random.randint(1,2)
                if punch == 1:
                    player.leftPunch = True
                else:
                    player.rightPunch = True
    
    
        # --- Game logic
        
        #Attack Timer to put the player in resting position
        if player.leftPunch or player.rightPunch:
            attackTimer += 1
            if attackTimer % 12 == 0:
                player.leftPunch = False
                player.rightPunch = False
        
        #HP timer, prevents loss of hp for half a second (30 frames)
        if canLoseHP == False:
            canLoseHPTimer += 1
            if canLoseHPTimer % 30 == 0:
                canLoseHP = True
            
        #resets player health
        if player.health <= 0:
            noLivesTimer += 1 #start counter when lives are 0
            if noLivesTimer % 60 == 0: #after one second has passed, reset lives
                player.health = 3
                playerHP.health = player.health    
        
        #disables the dodge after dodge duration timer       
        if player.leftDodge or player.rightDodge:
            dodgeTimer += 1
            if dodgeTimer % player.dodgeDuration == 0:
                player.leftDodge = False
                player.rightDodge = False
        
        #randomly throws a hint to the player
        if (enemy.rightHint and enemy.leftHint and enemy.rightPunch and enemy.leftPunch and enemy.isStunned) == False:   
            if random.randint(1,150) == 50:
                #print("Hinted!")
                hintLR = random.randint(1,2)
                if hintLR == 1:
                    #print("leftHint?")
                    enemy.leftHint = True
                    channel2 = hint.play(0)
                else:
                    #print("rightHint?")
                    enemy.rightHint = True
                    channel2 = hint.play(0)
        
        #registers if player attack is to be blocked or attack lands          
        if player.canAttack == False:
            if player.leftPunch or player.rightPunch:
                enemy.guard = True
                channel2 = block.play(0)           
            else:
                enemy.guard = False
        else:
            if player.leftPunch or player.rightPunch:
                enemy.isStunned = True
                enemy.health -= 1
                enemyHP.health = enemy.health 
                enemy.rightPunch = False
                enemy.leftPunch = False
                player.canAttack = False
                channel2 = hit.play(0)
                
                
        #disable enemy stun
        if enemy.isStunned:
            stunTimer += 1
            if stunTimer % 12 == 0:
                enemy.isStunned = False
                
        
        #punches the direction of hint
        if enemy.rightHint or enemy.leftHint:           
            hintTimer += 1
            if hintTimer % enemy.hintDuration == 0:
                if enemy.leftHint:
                    enemy.leftHint = False
                    enemy.leftPunch = True
                else:
                    enemy.rightHint = False
                    enemy.rightPunch = True
        
        #registers dodge and damage            
        if enemy.leftPunch or enemy.rightPunch:
            if enemy.leftPunch:
                if player.rightDodge:
                    player.canAttack = True
                else:
                    if canLoseHP:
                        player.health -= 1
                        playerHP.health = player.health
                        canLoseHP = False
                        channel2 = hit.play(0)
   
                    player.canAttack = False
            elif enemy.rightPunch:
                if player.leftDodge:
                    player.canAttack = True
                else:
                    if canLoseHP:
                        player.health -= 1
                        playerHP.health = player.health
                        canLoseHP = False
                        channel2 = hit.play(0)
                        
                    player.canAttack = False 
            punchTimer += 1
            if punchTimer % enemy.punchDuration == 0:
                enemy.leftPunch = False
                enemy.rightPunch = False
            
        #shows win/lose screen
        if enemy.health == 0:
            channel2 = win.play(0)
            eventScreen = 2
            
        elif player.health == 0 or seconds == 0:
            channel2 = gameover.play(0)
            eventScreen = 3
        
                    
        
        #######Pseudocode#######
        #if enemyLeftPunch == true:
            #if leftDodge:
                #playerCanAttack = true
            #else:
                #playerHP -= 1
                #playerCanAttack = false
        #elif enemyRightPunch == true:
            #if rightDodge:
                #playerCanAttack = true
                #playerCanAttack = false
            #else:
                #playerHP -= 1
        #else:
            #playerCanAttack = false
     
        # Call the update() method on all the sprites
        all_sprites_list.update() 
        
        # --- Draw a frame
     
        # Clear the screen
        screen.blit(background, (0,0))
        
        # Draws the timer
        font = pygame.font.SysFont("emulogic", 40)
        text = font.render(str(seconds), True, BLACK)
        center_x = (screen_width // 2) - (text.get_width() // 2)    
        screen.blit(text, [center_x, 15])
     
        # Draw all the sprites
        all_sprites_list.draw(screen)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()  
        
        if milliseconds > 60:
            seconds -= 1
            milliseconds -= 60
        
        milliseconds +=1
    
    if eventScreen == 2:
        gameOverTimer += 1
        if gameOverTimer % 160 == 0:
            player.health = 3
            playerHP.health = player.health
            enemy.health = 7
            enemyHP.health = enemy.health
            seconds = 60      
            eventScreen = 0
            
        screen.fill(BLACK)
        font = pygame.font.SysFont("emulogic", 40)
        text = font.render("You win", True, WHITE)
        center_x = (screen_width // 2) - (text.get_width() // 2)
        center_y = (screen_height // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])
        
        pygame.display.flip()
        
    if eventScreen == 3:
        gameOverTimer += 1
        if gameOverTimer % 160 == 0:
            player.health = 3
            playerHP.health = player.health
            enemy.health = 7
            enemyHP.health = enemy.health
            seconds = 60      
            eventScreen = 0
        screen.fill(BLACK)
        font = pygame.font.SysFont("emulogic", 40)
        text = font.render("You lose", True, WHITE)
        center_x = (screen_width // 2) - (text.get_width() // 2)
        center_y = (screen_height // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])
        
        pygame.display.flip()
        


 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()