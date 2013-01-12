#!/usr/bin/env python
'''
__Life.py__ = "Welcome to the game we call life. You wake up, you go to work, and you do it all again untill eventually the 9-to-5 grind drains all the life out of you.
                Press the left and right arrow keys to move.
                Press the space bar to quit life."

__author__ = "Kevin Skompinski"
__email__ = "kevinsko@buffalo.edu"
__copyright__ = "Copyright 2012, Spring '12, DMS110: Programming for Digital Art"

__python version__ = "2.7.2"
__last updated__ = "May 2, 2012"

'''
#-----import modules-----
import sys, pygame

#-----global variables-----
run = 1
end = False

#-----initialize pygame-----
pygame.init()
pygame.mixer.init()

#-----classes-----
#classes and function definitions
class Character:
    """Main Character"""
    
    #-----function definitions-----
    def __init__(self):
        """All initial setup/start values of the Character"""
        
        self.sprites = []

        self.sprites.append(pygame.image.load("rs.png")) #0
        
        self.sprites.append(pygame.image.load("r1.png"))
        self.sprites.append(pygame.image.load("r2.png"))
        self.sprites.append(pygame.image.load("r3.png"))
        self.sprites.append(pygame.image.load("r4.png"))
        self.sprites.append(pygame.image.load("r5.png"))
        self.sprites.append(pygame.image.load("r6.png"))
        self.sprites.append(pygame.image.load("r7.png"))
        self.sprites.append(pygame.image.load("r8.png"))

        self.sprites.append(pygame.image.load("l1.png"))
        self.sprites.append(pygame.image.load("l2.png"))
        self.sprites.append(pygame.image.load("l3.png"))
        self.sprites.append(pygame.image.load("l4.png"))
        self.sprites.append(pygame.image.load("l5.png"))
        self.sprites.append(pygame.image.load("l6.png"))
        self.sprites.append(pygame.image.load("l7.png"))
        self.sprites.append(pygame.image.load("l8.png"))
        
        self.sprites.append(pygame.image.load("ss.png"))

        self.shadow = pygame.image.load("shadow.png")
        self.srect = self.shadow.get_rect(center=(500,500))

        self.black = pygame.image.load("black.png")
        self.brect = self.black.get_rect()

        self.step = pygame.mixer.Sound("411__tictacshutup__thump-3-1.wav")
        self.step.set_volume(0.5)

        
        self.curframe = 0 #the index position that corresponds to the current frame 
        self.rect = self.sprites[0].get_rect(center=(500,450)) 

        self.left = False
        self.right = False
        self.end = False
        self.blackimg = False
        self.timer = False
        self.gunPlayed = False
        self.moveSpeed = 0 #speed for character to move

        self.yawn = pygame.mixer.Sound("68458__robinhood76__00925-yawn-gape-2.wav")
        self.yawn.play()

        self.gun = pygame.mixer.Sound("shotgun.wav")
        
    def updateGraphic(self):
        """Flips through the loaded images of the sprite"""
        global end

        if self.left == True:
            if self.curframe == 0:
                self.curframe = 9
            elif self.curframe == 9:
                self.curframe = 10
                self.step.play()
            elif self.curframe == 10:
                self.curframe = 11
            elif self.curframe == 11:
                self.curframe = 12
            elif self.curframe == 12:
                self.curframe = 13
            elif self.curframe == 13:
                self.step.play()
                self.curframe = 14
            elif self.curframe == 14:
                self.curframe = 15
            elif self.curframe == 15:
                self.curframe = 16
            else:
                self.curframe = 9
                
        if self.right == True:
            if self.curframe == 0:
                self.curframe = 1
            elif self.curframe == 1:
                self.curframe = 2
                self.step.play()
            elif self.curframe == 2:
                self.curframe = 3
            elif self.curframe == 3:
                self.curframe = 4
            elif self.curframe == 4:
                self.curframe = 5
            elif self.curframe == 5:
                self.curframe = 6
                self.step.play()
            elif self.curframe == 6:
                self.curframe = 7
            elif self.curframe == 7:
                self.curframe = 8
            else:
                self.curframe = 1

        if self.end == True:
            if self.gunPlayed != True:
                self.gun.play()
            self.curframe = 17
            self.blackimg = True
            self.gunPlayed = True
            end = True
    
    def updateAnimation(self):
        """Updates the animated movement"""
        if self.left: 
            self.rect.left -= self.moveSpeed
            
        if self.right: 
            self.rect.right += self.moveSpeed
    
    def resetAnimation(self):
        """Resets the current index position of the list of animated images back to 0 when the character is not moving"""
        global end
        if self.left == False and self.right == False and end == False: #always at index position 0 unless the character is moving        
            self.curframe = 0          
    
    def moveLeft(self):
        """Movement controlled by left arrow key"""
        self.left = True
    
    def moveRight(self):
        """Movement controlled by right arrow key""" 
        self.right = True
    
    def stopLeft(self):
        """Stops diagonal movement when keyup from arrow is released"""
        self.left = False
    
    def stopRight(self):
        """Stops diagonal movement when keyup from arrow is released"""
        self.right = False

    def startEnd(self):
        self.end = True
    
    def draw(self,screen):
        """Updates the draw blit used in frame flips"""

        if self.end == True:
            screen.blit(self.shadow, self.srect)
            screen.blit(self.sprites[17], self.rect) #draws the image in the list self.sprites at the current index position [self.curframe] on the rectangle self.rect

        else:
            screen.blit(self.shadow, self.srect)
            screen.blit(self.sprites[self.curframe], self.rect) #draws the image in the list self.sprites at the current index position [self.curframe] on the rectangle self.rect

    def drawGun(self,screen):
        screen.blit(self.shadow, self.srect)
        screen.blit(self.sprites[17], self.rect)
            
    def drawBlack(self,screen):
        screen.blit(self.shadow, self.srect)
        screen.blit(self.sprites[17], self.rect)

        screen.blit(self.black, self.brect)


class Background:
    
    #-----function definitions-----
    def __init__(self):
        """All initial setup/start values of the background"""

        self.foreground1 = pygame.image.load("foreground1.png")
        self.foreground2 = pygame.image.load("foreground2.png")
        self.foreground3 = pygame.image.load("foreground3.png")

        self.midground1 = pygame.image.load("midground1.png")
        self.midground2 = pygame.image.load("midground2.png")
        self.midground3 = pygame.image.load("midground3.png")

        self.frect1 = self.foreground1.get_rect(center=(3900,350))
        self.frect2 = self.foreground2.get_rect(center=(3900,350))
        self.frect3 = self.foreground3.get_rect(center=(3900,350))

        self.mrect1 = self.midground1.get_rect(center=(3000,350))
        self.mrect2 = self.midground2.get_rect(center=(3000,350))
        self.mrect3 = self.midground3.get_rect(center=(3000,350))

        self.news = pygame.mixer.Sound("Weazel News Latest Report.wav")
        self.music = pygame.mixer.Sound("TombstoneSmileRemix-Final.wav")
        self.office = pygame.mixer.Sound("Just a moment  Office Space.wav")
        self.typing = pygame.mixer.Sound("7968__cfork__computer-keyboard-hacking.wav")
        self.phone = pygame.mixer.Sound("24929__acclivity__phoneringing.wav")
        self.wind = pygame.mixer.Sound("22331__black-boe__wind.wav")
        self.clang = pygame.mixer.Sound("clang.wav")
        self.music2 = pygame.mixer.Sound("KillTheTarget.wav")
        self.static = pygame.mixer.Sound("23503__percy-duke__radio-static.wav")

        self.left = False
        self.right = False
        self.moveSpeed = 5 #speed for background to move

        self.x = 0

    def events(self):
        global run
        global end
        if run == 1:
            if self.x == 30:
                self.news.play(0, 0, 10000)
        
            if self.x == 250:
                self.news.fadeout(10000)

            if self.x == 300:
                self.music.play(-1, 0, 5000)

            if self.x == 1250:
                self.music.fadeout(5000)
                self.office.play(-1, 0, 10000)
                self.typing.play(-1, 0, 10000)
                self.phone.play(-1, 0, 10000)

            if self.x == 1390:
                self.clang.play(0,0,100)
                self.office.fadeout(8000)
                self.typing.fadeout(8000)
                self.phone.fadeout(8000)
                pygame.time.wait(8000)
                run = run + 1
                self.wind.play(0,0,0)
                self.x = 0

        if run == 2:
            if self.x == 30:
                self.news.set_volume(0.3)
                self.news.play(0, 0, 10000)
                self.static.set_volume(0.5)
                self.static.play(-1, 0, 10000)
        
            if self.x == 250:
                self.news.fadeout(10000)
                self.static.fadeout(10000)

            if self.x == 300:
                self.music.set_volume(0.25)
                self.music2.play(-1, 0, 5000)

            if self.x == 1250:
                self.music2.fadeout(5000)
                self.office.play(-1, 0, 10000)
                self.typing.play(-1, 0, 10000)
                self.phone.play(-1, 0, 10000)

            if self.x == 1390:
                self.clang.play(0,0,100)
                self.office.fadeout(8000)
                self.typing.fadeout(8000)
                self.phone.fadeout(8000)
                pygame.time.wait(8000)
                run = run + 1
                self.x = 0

        if run >= 3:
            if self.x == 30:
                self.wind.play(-1,0,0)
        
            if self.x == 1250:
                self.music.fadeout(5000)
                self.office.play(-1, 0, 10000)
                self.typing.play(-1, 0, 10000)
                self.phone.play(-1, 0, 10000)

            if self.x == 1390:
                self.clang.play(0,0,100)
                self.office.fadeout(8000)
                self.typing.fadeout(8000)
                self.phone.fadeout(8000)
                self.wind.fadeout(8000)
                pygame.time.wait(8000)
                self.frect3 = self.foreground3.get_rect(center=(3900,350))
                self.mrect3 = self.midground3.get_rect(center=(3000,350))
                run = run + 1
                self.x = 0

        if end == True:
            self.news.stop()
            self.music.stop()
            self.music2.stop()
            self.office.stop()
            self.typing.stop()
            self.phone.stop()

    
    def updateAnimation(self):
        """Updates the animated movement"""
        global run
        if run == 1:
            
            if self.left and self.x >=0: 
                self.frect1.left += self.moveSpeed
                self.mrect1.left += self.moveSpeed*0.5               
                self.x = self.x-1
                
            if self.right and self.x <1400: 
                self.frect1.right -= self.moveSpeed
                self.mrect1.right -= self.moveSpeed*0.5   
                self.x = self.x+1

        if run == 2:
            if self.left and self.x >=0: 
                self.frect2.left += self.moveSpeed
                self.mrect2.left += self.moveSpeed*0.5               
                self.x = self.x-1
                
            if self.right and self.x <1400: 
                self.frect2.right -= self.moveSpeed
                self.mrect2.right -= self.moveSpeed*0.5   
                self.x = self.x+1

        if run >= 3:
            if self.left and self.x >=0: 
                self.frect3.left += self.moveSpeed
                self.mrect3.left += self.moveSpeed*0.5               
                self.x = self.x-1
                
            if self.right and self.x <1400: 
                self.frect3.right -= self.moveSpeed
                self.mrect3.right -= self.moveSpeed*0.5   
                self.x = self.x+1
                
    def moveLeft(self):
        """Movement controlled by left arrow key"""
        self.left = True
        
    def moveRight(self):
        """Movement controlled by right arrow key""" 
        self.right = True
    
    def stopLeft(self):
        self.left = False
    
    def stopRight(self):
        self.right = False
    
    def draw(self,screen):
        """Updates the draw blit used in frame flips"""
        global run
        if run == 1:
            screen.blit(self.midground1, self.mrect1) #draws the foreground
            screen.blit(self.foreground1, self.frect1) #draws the midground

        if run == 2:
            screen.blit(self.midground2, self.mrect2) #draws the foreground
            screen.blit(self.foreground2, self.frect2) #draws the midground

        if run >= 3:
            screen.blit(self.midground3, self.mrect3) #draws the foreground
            screen.blit(self.foreground3, self.frect3) #draws the midground

               
class Overlay:
    """Overlay Image"""
    
    #-----function definitions-----
    def __init__(self):

        self.overlay = pygame.image.load("overlay.png")
        self.rect = self.overlay.get_rect()
    
    def draw(self,screen):
        """Updates the draw blit used in frame flips"""
        screen.blit(self.overlay, self.rect)


#-----global variables-----
mainClock = pygame.time.Clock()
width, height = 1000,700

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Life') #GUI window title
pygame.key.set_repeat(10,10) #sets a key repeat so can hold down the arrow keys and the character will move 

player = Character() #make an instance of the player
world = Background() #make an instance of the background
overlay = Overlay() #make an instance of the overlay image

background1 = pygame.image.load("sky1.png") #load in background image 1
background2 = pygame.image.load("sky2.png") #load in background image 2
background3 = pygame.image.load("sky3.png") #load in background image 3

#-----main body-----
loop = True
black = False
done = False

while loop:
    #-----events-----
    #check for events (user input from keyboard and/or mouse)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            loop = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and event.key == pygame.K_LEFT:
                player.stopLeft()
                world.stopLeft()
                player.stopRight()
                world.stopRight()

            elif event.key == pygame.K_RIGHT:                
                player.moveRight() #calls the Character class moveRight() function for the player instance
                world.moveRight()
                
            elif event.key == pygame.K_LEFT:                
                player.moveLeft() #calls the Character class moveLeft() function for the player instance
                world.moveLeft()
         
            elif event.key == pygame.K_SPACE:
                player.startEnd()
                
                      
        #using keyup events to stop flag triggers of movement in diagonal direction
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.stopLeft()
                world.stopLeft()
            if event.key == pygame.K_RIGHT:
                player.stopRight()
                world.stopRight()

        #-----updates-----
    #automatic updates as coded not using key events
    #stops movement if reach ends of screen
    player.updateGraphic() #cycles through the image files of character in list

    player.updateAnimation() #calls the Character class updateAnimation() function for the player instance
    
    world.updateAnimation() #updates the background

    player.resetAnimation() #resets the aimation if player is not moving

    world.events() #location based events and sound effects in the background class
    
    #-----view updates-----
    #(re)drawing the objects on the screen after animations are updated         
    screen.fill((0,0,0))   

    global end
    global run
    if run == 1:
        screen.blit(background1, (0,0)) #draws the background on the screen

    if run == 2:
        screen.blit(background2, (0,0)) #draws the background on the screen

    if run >= 3:
        screen.blit(background3, (0,0)) #draws the background on the screen
    
    world.draw(screen)

    if end == False:
        player.draw(screen)

    if end == True:
        player.draw(screen)
        if black == True:
            player.drawBlack(screen)
            done = True
        black = True
        
    overlay.draw(screen)

    #show the objects on the screen
    if done == False:
        pygame.display.flip()

    else:
        pygame.time.wait(1000)
        pygame.display.flip()

    mainClock.tick(20)

#-----CREDITS-----
"All ambient sounds and sound effects frovided by The FreeSound Project."
"Weazel News report taken from Grand Theft Auto IV by Rockstar Games."
"Smile Song (The Living Tombstone remix) originally from My Little Pony; Friendship is Magic."
"Office sound effects are from Office Space."
