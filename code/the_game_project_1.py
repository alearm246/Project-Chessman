import pyxel
import random


class Character:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 7
        self.height = 10
        self.step = 1

    def update_random(self):
        randomNumberY = random.random() # decimal number between 0 and 1
        randomNumberX = random.random() # decimal number between 0 and 1

        if randomNumberY < .5: # 50% chance move up
            self.y -= 1
        else: # 50% chance move down
            self.y += 1

        if randomNumberX < .5: #50% chance move left
            self.x -= 1
        else: # 50% chance move right
            self.x += 1

    def update_walk(self):
        self.x = self.x+self.step
        if self.x == 50:
            self.step = self.step + -1
        elif self.x == 0:
            self.step = self.step + 1



        #self.CheckBoundary()

    def CheckBoundary(self):
            #print(self.y)
            if self.x > 145:
                self.x = 145
            if self.y > 105:
                self.y = 105
            if self.x < 0:
                self.x = 0
            if self.y < 0:
                self.y = 0

    def IsTouching(self, otherCharacter): #checks for collisions
        self_left_X = self.x
        self_top_Y = self.y
        self_bottom_Y = self.height + self.y
        self_right_X = self.width + self.x
        other_left_x = otherCharacter.x
        other_top_Y = otherCharacter.y
        other_bottom_Y = otherCharacter.height + otherCharacter.y
        other_right_X = otherCharacter.width + otherCharacter.x

        if (

          self_right_X >= other_left_x
          and self_left_X <= other_right_X
          and self_bottom_Y >= other_top_Y
          and self_top_Y <= other_bottom_Y
        ):
          return True
        else:
          return False

    def Interacting(self, otherCharacter): # checks for interactions
         if self.IsTouching(otherCharacter):
             otherCharacter.displayText = "hey what's the problem ?"


class Player(Character):
    def  __init__(self):
        Character.__init__(self)
        self.color = 12
        self.width = 16 # exact image dimensions (otherwise it gets cut off)
        self.height = 16 # exact image dimensions (otherwise it gets cut off)


    def update(self): # movesthe Character
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_S):
            self.y += 1
        if pyxel.btn(pyxel.KEY_A):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1
        #print('Enemy (update) : self.y: '+str(self.x))
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.width, self.height, 5) # displays the image
        self.CheckBoundary()



class NonPlayer(Character):
    def  __init__(self):
        Character.__init__(self)
        self.x = 32
        self.y = 32
        self.width = 32
        self.height = 32
        self.displayText = ""
    def draw(self):
        #pyxel.rect(self.x, self.y, self.x + self.width, self.y + self.height, 4)#
        if self.displayText != '':
            pyxel.text(self.x, self.y - 5, self.displayText, 6)


        pyxel.blt(self.x, self.y, 2, 0, 0, self.width, self.height, 0)
    def update(self):
        self.update_walk()
        self.CheckBoundary()
class Background():
    def __init__(self):
        self.x = 80
        self.y = 60
        self.width = 322
        self.height = 321
    def draw(self):
        pyxel.blt(self.x, self.y, 3, 0, 0, self.width, self.height, 0)


class Enemy(Character):
    def __init__(self):
        Character.__init__(self)
        self.x = 12
        self.y = 12
        self.width = 12
        self.height = 12
        self.color = 8
        #print('Enemy (__init__) : self.x: '+str(self.x))
    def update(self):
        self.update_random()
        self.CheckBoundary()

    def draw(self):
        #pyxel.blt(x, y, imageID, u, v, width, height, [colKey])
        pyxel.blt(self.x, self.y, 1, 0, 0, self.width, self.height, 5)
        #pyxel.rect(self.x, self.y, self.width, self.height, self.color)



class App:
    def __init__(self):
        self.width = 160
        self.height = 120
        self.Player = Player()
        self.Enemy = Enemy()
        self.npc = NonPlayer()
        self.Enemy2 = Enemy()
        #self.Background = Background()
        pyxel.init(self.width, self.height)

        # Load images here after initializing, but before running

        #reference: pyxel.image(imageID).load(...)
        pyxel.image(0).load(0, 0, "../assets/cat_16x16.png") # Puts the image into RAM
        pyxel.image(1).load(0, 0, "../assets/bad_face_12x12.png") # puts image into RAM
        pyxel.image(2).load(0, 0, "../assets/npc_32x32.png")
        #pyxel.image(1).load(0, 0, "../assets/random_image.png")


        #pyxel.image(2).load(0, 0, "236-2363681_lucas-gba-remastered-sprite-human-pixel-art.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.Player.update()
        self.npc.update()
        self.Enemy.update()
        self.Enemy2.update()
        self.Player.IsTouching(self.Enemy)
        self.Player.IsTouching(self.Enemy2)
        self.Player.Interacting(self.npc)

    def draw(self):
        #print("draw")
        pyxel.cls(0)
        self.Player.draw()
        self.npc.draw()
        self.Enemy.draw()
        self.Enemy2.draw()
        #self.Background.draw()

App()
