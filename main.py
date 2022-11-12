import time
# Import the pygame module
import random

import pygame
import pygame.freetype
# import pygame_widgets
# from pygame_widgets.slider import Slider
# from pygame_widgets.textbox import TextBox

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

pygame.init()
pygame.font.init()
GAME_FONT = pygame.freetype.Font("Aldrich-Regular.ttf", 24)
INSTRUCTION_FONT = pygame.freetype.Font("Aldrich-Regular.ttf", 20)
GAME_FONT_SMALL = pygame.freetype.Font("Aldrich-Regular.ttf", 18)
HEART_IMG = pygame.image.load('heart.png')
GREY_HEART_IMG = pygame.image.load("greyheart.png")
GAME_FONT_BIG = pygame.freetype.Font("Aldrich-Regular.ttf", 50)
BUTTON_DEACTIVATED = pygame.image.load("button.png")
BUTTON_ACTIVATED = pygame.image.load("button_on.png")
SWITCH_UP = pygame.image.load("switch_up.png")
SWITCH_DOWN = pygame.image.load("switch_down.png")
SWITCH_LEFT = pygame.image.load("switch_left.png")
SWITCH_RIGHT = pygame.image.load("switch_right.png")
ALIEN_IMG = pygame.image.load("alien.png")
ASTEROID_IMG = pygame.image.load("asteroid.png")
STAR_IMG = pygame.image.load("star.png")
GUNSHOT_IMG = pygame.image.load("gunshot.png")
showing_lv_text=True
# Define constants for the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
PANEL_SIZE = 120
BUTTON_SIZE = 80
SWITCH_SIZE = 80
projspeed=3

# flavour text
STAGE_1_DESC = "I. Navigation"
STAGE_2_DESC = "II. Messenger"
STAGE_3_DESC = "III. Arrival"

LV_1_DESC = """1. Takeoff
Earth is facing a siege. As the best pilot the planet has to offer, you will go with the last spaceship on Earth, with a mission: To contact our allies at (^>, ><, ^<), for them to come to our aid. The general will give you further directions. Good luck, and come back alive.
You lose 1HP if the navigation instructions are incomplete at the end of the timer.
"""
LV_2_DESC = """2. Breakthrough
Congratulations on taking off. I hope you've become accustomed to the controls of this old model. Now, you will have to break through the blockade the aliens have set around Earth. Be quick, because they have been alerted to your presence. The weapons panel is on your right.
Weapon controls are on your right. Click on aliens to shoot at them. You take 1 damage for each alien with timer running out.
"""
LV_3_DESC = """3. Escape
You have gotten to the other side, but they are now searching for you. Fire at will.

"""
LV_4_DESC = """4. Asteroids
You are almost there. Navigate the asteroid belt; I have good news waiting for you on the other side.
Move your cursor over the asteroids to dodge them.
"""
LV_5_DESC = """5. Warp Drive
Here's the good news: We've checked the area and it's safe. You can enable warp drive now to get to our allies faster. You gotta be more careful with navigation, but I'm sure you can handle this. The bad news: The aliens seem to be experimenting with a qarenium-indissium alloy in their spaceship coatings.
The timer ticks faster and aliens now have 3HP.
"""
LV_6_DESC = """6. Interception
The aliens have sent a detachment of unknown size to intercept you. Deal with them before proceeding.
Use only weapons.
"""
LV_7_DESC = """7. Black Hole
You strayed off the path while evading the alien attack. You are far too close to a black hole. You know the effects of time dilation, get away now!
Time for this level has been reduced.
"""
LV_8_DESC = """8. Navigation Failure


"""
LV_9_DESC = """9. Distress Signal
Some of our allies have been attacked. You will go in a gesture of goodwill to help fight the alien invaders.

"""
LV_10_DESC = """10. Rescue
This is the rescue mission you have been called to undertake. By helping to fend off the aliens, they will be more likely to reciprocate.
Allies will help shoot some aliens. Mistakes decrease the number of allied ships by your side.
"""
LV_11_DESC = """11. Pitched Battle
The aliens have launched a full force to counter the threat your team poses. Protect your allies at all costs, as they will be crucial in your mission. Intelligence has revealed that the aliens now have rapid-fire guns, on top of missiles they previously had. These new ships are quickly approaching your location.
Aliens now have 5HP and can shoot at you. Press 1, 2, 3 or 4 on the weapons panel to activate defensive missiles.
"""
LV_12_DESC = """12. Retreat
Overwhelmed, your force retreats. Your job is to cover the retreat, to save as many allies as possible.

"""
LV_13_DESC = """13. Chase
Your force was unable to hold off the alien fleet. Enter hyperspace to flee from the aliens. This is our last chance.

"""
LV_14_DESC = """14. Minefield
We have received word of a minefield ahead in your flight path. Navigate the minefield.
Move your cursor over the mines to dodge them. Mines do 2 damage.
"""
LV_15_DESC = """15. ms. hAbu
The coast is clear. Proceed towards the destination at full speed.
There's... not much in this level. Relax.
"""
LV_16_DESC = """16. Enemy reinforcements
Apologies for the faulty information. It appears that the aliens had set up an ambush. Good on you for making it through. The bad news though, is that enemy reinforcements have arrived.

"""
LV_17_DESC = """17. Supernova
A supernova has blown you off course. Your systems seem to be working fine, from what we can tell. Just follow my instructions and you will be back on track in no time. Unfortunately, our allies are still uncontactable.
Your allies will not help in this level.
"""
LV_18_DESC = """18. Tachyon Field
.track on back were You .job Great

"""
LV_19_DESC = """19. Unknown Transmission
We lost track of you for quite a while there. It's great that you're back. There will be a tachyon field in front of you. You went forwards. Also, ignore the nonsensical transmissions. We are trying to figure out the source. Right now, just keep going towards the destination.
Ignore the nonsensical instructions.
"""
LV_20_DESC = """20. Outnumbered
Run. Your ship is no match for theirs.

"""
LV_21_DESC = """21. Rapid Fire
The aliens have developed new propulsor-powered weapons and the ship coating has been further upgraded. Still, you must press on. This is our only hope. You see the planet straight ahead.
Aliens have 7HP. Alien weapons fire twice as fast and each shot deals 2 damage.

"""
LV_22_DESC = """22. Swarm
The alien force has launched a last-ditch attempt to stop you. This is their "make it or break it" solution. Same for you, and for us. Pilot, Earth depends on you.

"""
LV_23_DESC = """23. Return
Latest intelligence report: our allies at the destination have been converted. The planet is crumbling. Come back if you still (static plays)

"""
LV_24_DESC = """24. ???
ALERT: THIS IS AN AUTOMATED MESSAGE FROM THE DEPARTMENT OF DEFENSE. WE HAVE EXPERIENCED A BREACH OF UNKNOWN MAGNITUDE. ALL AGENTS ARE TO RETURN TO BASE IMMEDIATELY. THE TACHYONIC BOMB WILL BE ACTIVATED IN 30 EARTH DAYS.
???
"""
LV_25_DESC = """25. Conversion
What do you want? Stop, stop, stop, stop, stop, sero, stop, stop, stop, stop, stop, stop, conver, stop, stop, sion, stop, stop, stop, weapon, stop, stop, stop, stop, stop, stop, stop, stop
Aliens instantly kill you.
"""

pygame.mixer.init()
CALM_MUSIC = pygame.mixer.Sound("1.mp3")
EH_MUSIC = pygame.mixer.Sound("2.mp3")
AAAA_MUSIC = pygame.mixer.Sound("3.mp3")

clock = pygame.time.Clock()
clock_tick = 0

in_level = False
level = 1
# Instructions to the player
MAX_INSTRUCTIONS = 5

# Crossed out alien boxes
num_alien_boxes = 0
alien_possible_boxes = random.sample(range(20), num_alien_boxes)
ALHP = 1

# player health
p_hp = 15

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# rect with alpha
def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


# Define a panel object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'panel'
class Panel(pygame.sprite.Sprite):
    def __init__(self, num):
        super(Panel, self).__init__()
        self.surf = pygame.Surface((PANEL_SIZE, PANEL_SIZE))
        self.surf.fill((169, 169, 169, 128))
        self.rect = self.surf.get_rect()
        self.rectCenter = pygame.Rect(5, 5, 110, 110)

        self.textSurf, rect = GAME_FONT.render(str(num), (169, 169, 169))


# alien weapon, stars, asteroid
class Falling:
    x = 0
    y = 0
    speed = 0
    imgs = {"Asteroid": ASTEROID_IMG, "Star": STAR_IMG, "Gunshot": GUNSHOT_IMG}

    def __init__(self, start, end, x, type, speed):
        self.y = start
        self.end = end
        self.x = x
        self.type = type
        self.speed = speed
        self.surf = self.imgs[self.type]
        self.location = self.x, self.y
        self.rect = self.surf.get_rect()

    def draw(self, screen):
        self.img = self.imgs[self.type]
        screen.blit(self.img, (self.x, self.y - self.img.get_height()))

    def handle_event(self, screen, e):
        if SCREEN_HEIGHT - 2 * 120 < self.y < SCREEN_HEIGHT - 120:
            if self.type in ("Asteroid", "Gunshot", "Mine") and e.type == KEYDOWN:
                if (
                        e.key == pygame.K_1 and 6 * 120 < self.x < 7 * 120) or (
                        e.key == pygame.K_2 and 7 * 120 < self.x < 8 * 120) or (
                        e.key == pygame.K_3 and 8 * 120 < self.x < 9 * 120) or (
                        e.key == pygame.K_4 and 9 * 120 < self.x < 10 * 120):
                    return "Delete"
        elif SCREEN_HEIGHT - 120 < self.y:
            if self.type in ("Asteroid", "Gunshot", "Mine"):
                return "Missed"
        self.location = self.x, self.y
        self.rect.move_ip(self.location[0], self.location[1])
        if self.surf.get_rect().collidepoint(pygame.mouse.get_pos()) and self.type == "Star":
            return "Delete"
        return False

    def next(self):
        self.y += self.speed


class Switch(pygame.sprite.Sprite):
    activated = False
    activatedImg = None
    deactivatedImg = None
    rect = None
    pos = 0
    location = (0, 0)
    handled = False

    def __init__(self, pos):
        super(Switch, self).__init__()
        self.pos = pos
        self.surf = self.deactivatedImg.convert_alpha()
        self.rect = self.surf.get_rect()
        # self.rect = self.rect.move(self.location[0], self.location[1])

    def updateLocation(self, loc):
        self.location = loc
        self.rect.move_ip(self.location[0], self.location[1])

    def activate(self):
        self.activated = True
        self.surf = self.activatedImg.convert_alpha()

    def deactivate(self):
        self.activated = False
        self.surf = self.deactivatedImg.convert_alpha()

    def toggle(self):
        if self.activated:
            self.activated = False
            self.surf = self.deactivatedImg.convert_alpha()
        else:
            self.activated = True
            self.surf = self.activatedImg.convert_alpha()


class ToggleClass(pygame.sprite.Sprite):
    pass


class InstantButton(Switch):
    size = BUTTON_SIZE

    def __init__(self, pos):
        self.activatedImg = BUTTON_ACTIVATED.convert_alpha()
        self.deactivatedImg = BUTTON_DEACTIVATED.convert_alpha()
        super(InstantButton, self).__init__(pos)


class HoldButton(InstantButton, ToggleClass):
    def __init__(self, pos):
        super(HoldButton, self).__init__(pos)


class SwitchUpDown(Switch, ToggleClass):
    size = SWITCH_SIZE

    def __init__(self, pos):
        self.activatedImg = SWITCH_DOWN.convert_alpha()
        self.deactivatedImg = SWITCH_UP.convert_alpha()
        super(SwitchUpDown, self).__init__(pos)


class SwitchLeftRight(Switch, ToggleClass):
    size = SWITCH_SIZE

    def __init__(self, pos):
        self.activatedImg = SWITCH_RIGHT.convert_alpha()
        self.deactivatedImg = SWITCH_LEFT.convert_alpha()
        super(SwitchLeftRight, self).__init__(pos)


class Alien(pygame.sprite.Sprite):
    global projspeed
    health = 1
    firing = False
    rect = None
    pos = 0
    location = (0, 0)

    def __init__(self, pos, health=1):
        super(Alien, self).__init__()
        self.pos = pos
        self.health = health
        self.surf = ALIEN_IMG.convert_alpha()
        self.rect = self.surf.get_rect()
        # self.rect = self.rect.move(self.location[0], self.location[1])

    def updateLocation(self, loc):
        self.location = loc
        self.rect.move_ip(self.location[0], self.location[1])

    def draw(self, pos):
        if self.health <= 0:
            return
        screen.blit(ALIEN_IMG, ((pos % 4 + 6) * PANEL_SIZE + 21, SCREEN_HEIGHT - (7 - pos // 4) * PANEL_SIZE + 15))
        textSurfAlienHP, rect = GAME_FONT_BIG.render(str(self.health), (255, 255, 255))
        screen.blit(textSurfAlienHP,
                    ((pos % 4 + 6) * PANEL_SIZE + 50, SCREEN_HEIGHT - (7 - pos // 4) * PANEL_SIZE + 40))
        if self.location == (0, 0):
            self.updateLocation(((pos % 4 + 6) * PANEL_SIZE + 50, SCREEN_HEIGHT - (7 - pos // 4) * PANEL_SIZE + 40))
        # text4surf, rect = GAME_FONT_BIG.render("4", (208, 125, 216))
        # screen.blit(text4surf, (9 * PANEL_SIZE + 50, SCREEN_HEIGHT - 2 * PANEL_SIZE + 40))

    def takeDamage(self, amt=1):
        self.health -= amt
        if self.location == (0, 0):
            self.updateLocation(self.location)
        self.draw(self.pos)

    def fire(self):
        if self.location != (0, 0):
            falling_objects.append(
                Falling(self.location[1] + 60, SCREEN_HEIGHT - 120, self.location[0] - 16, "Gunshot", projspeed))

def makeInstruction(switches, num):
    ins = []
    for i in range(num):
        rswitch = random.choice(switches)
        msg = ""
        if type(rswitch) == InstantButton:
            msg = f"Activate {rswitch.pos}"
        elif type(rswitch) == HoldButton:
            msg = f"Press {rswitch.pos}"
        elif type(rswitch) == SwitchUpDown:
            msg = f"Flick {rswitch.pos}"
        elif type(rswitch) == SwitchLeftRight:
            msg = f"Flick {rswitch.pos}"

        # elif type(rswitch) == SliderHori:
        #     msg = f"Move {rswitch.pos} to {random.randint(0, 2)}"
        ins.append("- " + msg)
    return ins


def spawn_alien(health=1):
    has_aliens_pos = [al.pos for al in has_aliens if al is not None]
    can_spawn = [item for item in alien_possible_boxes if item not in has_aliens_pos]
    if can_spawn == []:
        return
    pos = random.choice(can_spawn)
    has_aliens[pos] = Alien(pos, health)

# Instantiate switches.
switches = []
for i in range(2):
    n = random.randint(1,3)
    if n == 1:
        switches.append(InstantButton(i + 1))
    if n == 2:
        switches.append(HoldButton(i + 1))
    if n == 3:
        switches.append(SwitchUpDown(i + 1))
    if n == 4:
        switches.append(SwitchLeftRight(i + 1))

instructions = makeInstruction(switches, 2)

# Instantiate panels.
panels = []
for i in range(1, 37):
    panels.append(Panel(i))

# Variable to keep the main loop running
running = True
loop = True
seconds_passed = 0
showing_lv_text = True

# Falling objects
falling_objects = []
has_aliens = [None] * 20

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            elif in_level:
                for fo in falling_objects:
                    result = fo.handle_event(screen, event)
                    if result == "Delete":
                        falling_objects.remove(fo)
                    elif result == "Missed":
                        falling_objects.remove(fo)
                        p_hp -= 1
                        for i in range(15):
                            if i < p_hp:
                                screen.blit(HEART_IMG, (PANEL_SIZE * 6 + i * 32, 8))
                            else:
                                screen.blit(GREY_HEART_IMG, (PANEL_SIZE * 6 + i * 32, 8))

        elif event.type == QUIT:
            running = False
        elif in_level:
            if event.type == MOUSEBUTTONDOWN:
                for s in switches:
                    if s.rect.collidepoint(pygame.mouse.get_pos()):
                        s.toggle()
                        instructions.pop(0)
                for al in has_aliens:
                    if al is None:
                        continue
                    if al.rect.collidepoint(pygame.mouse.get_pos()):
                        al.takeDamage(1)

                # if slider.slider.on_slider(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                #     slider.slider.handle_event(screen, pygame.mouse.get_pos()[0])
            if event.type == MOUSEBUTTONUP:
                for s in switches:
                    if not issubclass(type(s), ToggleClass) and s.rect.collidepoint(pygame.mouse.get_pos()):
                        s.toggle()
            for fo in falling_objects:
                fo.handle_event(screen, event)

        # Check for QUIT event. If QUIT, then set running to false.
    # clock tick
    dt = clock.tick()
    clock_tick += dt

    if loop:
        # Fill the screen with black
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('1asteroid.jpg'), (0, 0))
    # level
    projspeed+=0.2
    if level == 1:
        num_alien_boxes = 0
        CALM_MUSIC.play()
        #in_level = False
        #showing_lv_text=True
    if level == 5:
        ALHP = 3
    if level >= 6:
        MAX_INSTRUCTIONS = 4
    if level == 11:
        CALM_MUSIC.stop()
        EH_MUSIC.play()
    if level >= 11:
        projspeed += 0.2
        ALHP = 5
        MAX_INSTRUCTIONS = 3
    if level >= 16:
        MAX_INSTRUCTIONS=2
    if level < 20:
        num_alien_boxes = min(20, 1 + level)
    if level == 21:
        EH_MUSIC.stop()
        AAAA_MUSIC.play()
    if level == 26:
        pass
        # TODO: win screen
    elif level >= 21:
        projspeed += 0.4
        ALHP = 7
        MAX_INSTRUCTIONS = 1

    if clock_tick > 1000:
        if in_level:
            if random.randint(1, 2) == 1:
                spawn_alien(health=ALHP)
        if in_level:
            for al in has_aliens:
                if al is not None:
                    if random.randint(1, 3) == 1:
                        al.fire()
        seconds_passed += 1
        clock_tick = 0

    if len(instructions) == 0:
        level += 1
        alien_possible_boxes = random.sample(range(20), min(20, num_alien_boxes))
        has_aliens = [None] * 20
        falling_objects = []
        switches = []
        for i in range(min(36, level*2)):
            n = random.randint(1, 3)
            if n == 1:
                switches.append(InstantButton(i + 1))
            if n == 2:
                switches.append(HoldButton(i + 1))
            if n == 3:
                switches.append(SwitchUpDown(i + 1))
            if n == 4:
                switches.append(SwitchLeftRight(i + 1))

        instructions = makeInstruction(switches, level*7//3)
        in_level = False
        seconds_passed = 0

    # Draw instructions
    draw_rect_alpha(screen, (128, 128, 128, 200), (0, 0, PANEL_SIZE * 6, SCREEN_HEIGHT - 6 * PANEL_SIZE))
    draw_rect_alpha(screen, (0, 0, 0, 128), (8, 8, PANEL_SIZE * 6 - 16, SCREEN_HEIGHT - 6 * PANEL_SIZE - 16))
    for i in range(min(len(instructions), MAX_INSTRUCTIONS)):
        textSurf, rect = INSTRUCTION_FONT.render(instructions[i], (240, 240, 240))
        screen.blit(textSurf, (20, 25 * i + 20))

    if len(instructions) > MAX_INSTRUCTIONS:
        textSurfMore, rect = GAME_FONT_SMALL.render(f"... and {len(instructions) - 5} more", (210, 210, 210))
        screen.blit(textSurfMore, (20, 145))

    # Draw the panels on the screen
    for i in range(36):
        x = PANEL_SIZE * (i % 6)
        y = SCREEN_HEIGHT - 6 * PANEL_SIZE + PANEL_SIZE * (i // 6)
        screen.blit(panels[i].surf, (x, y))
        draw_rect_alpha(panels[i].surf, (39, 39, 39, 128), panels[i].rectCenter)
        screen.blit(panels[i].textSurf, (x + 10, y + 10))

    # Draw switches
    if in_level:
        for s in switches:
            # if s.rect is not None and s.rect.collidepoint(pygame.mouse.get_pos()):
            #    print(f"{s} activated on {pygame.mouse.get_pos()}")
            #    s.toggle()
            #    handled = pygame.mouse.get_pressed()[0]

            i = s.pos - 1
            x = PANEL_SIZE * (i % 6)
            y = SCREEN_HEIGHT - 6 * PANEL_SIZE + PANEL_SIZE * (i // 6)
            screen.blit(s.surf, (x + (PANEL_SIZE - s.size) // 2, y + (PANEL_SIZE - s.size) // 2))
            if s.location == (0, 0):
                s.updateLocation((x + (PANEL_SIZE - s.size) // 2, y + (PANEL_SIZE - s.size) // 2))

    # draw slider
    # slider = SliderHori(13, 124124, 2)
    # slider.slider.draw(screen)

    # draw health
    if in_level:
        for i in range(15):
            if i < p_hp:
                screen.blit(HEART_IMG, (PANEL_SIZE * 6 + i * 32, 8))
            else:
                screen.blit(GREY_HEART_IMG, (PANEL_SIZE * 6 + i * 32, 8))
        # draw alien boxes
        draw_rect_alpha(screen, (50, 50, 50, 200),
                        (6 * PANEL_SIZE, SCREEN_HEIGHT - 7 * PANEL_SIZE - 6, 4 * PANEL_SIZE, 6 * PANEL_SIZE + 6))

        for i in range(20):
            if i not in alien_possible_boxes:
                draw_rect_alpha(screen, (35, 35, 35, 128),
                                (
                                (i % 4 + 6) * PANEL_SIZE + 6, SCREEN_HEIGHT - (7 - i // 4) * PANEL_SIZE, PANEL_SIZE - 6,
                                PANEL_SIZE - 6))
                pygame.draw.line(screen, (255, 53, 53, 128),
                                 ((i % 4 + 6) * PANEL_SIZE + 6 + 15, SCREEN_HEIGHT - (7 - i // 4) * PANEL_SIZE + 15),
                                 ((i % 4 + 7) * PANEL_SIZE - 15, SCREEN_HEIGHT - (6 - i // 4) * PANEL_SIZE - 6 - 15), 7)
                pygame.draw.line(screen, (255, 53, 53, 128),
                                 ((i % 4 + 7) * PANEL_SIZE - 15, SCREEN_HEIGHT - (7 - i // 4) * PANEL_SIZE + 15),
                                 (
                                 (i % 4 + 6) * PANEL_SIZE + 6 + 15, SCREEN_HEIGHT - (6 - i // 4) * PANEL_SIZE - 6 - 15),
                                 7)
            else:
                draw_rect_alpha(screen, (0, 0, 0, 128),
                                (
                                (i % 4 + 6) * PANEL_SIZE + 6, SCREEN_HEIGHT - (7 - i // 4) * PANEL_SIZE, PANEL_SIZE - 6,
                                PANEL_SIZE - 6))
        # draw aliens
        # for i in range(20):
        # if i in has_aliens:
        for al in has_aliens[:]:
            if al is None:
                continue
            if al.health <= 0:
                has_aliens[al.pos] = None
            al.draw(al.pos)
            # screen.blit(ALIEN_IMG, ((i % 4 + 6) * PANEL_SIZE + 21, SCREEN_HEIGHT - (7 - i // 4) * PANEL_SIZE + 15))

        # draw falling objects
        for fo in falling_objects:
            fo.next()
            fo.draw(screen)
        # draw number boxes
        for i in range(4):
            draw_rect_alpha(screen, (60, 10, 10, 128),
                            ((i + 6) * PANEL_SIZE + 6, SCREEN_HEIGHT - 2 * PANEL_SIZE, PANEL_SIZE - 6,
                             PANEL_SIZE - 6))
        text1surf, rect = GAME_FONT_BIG.render("1", (97, 215, 97))
        screen.blit(text1surf, (6 * PANEL_SIZE + 50, SCREEN_HEIGHT - 2 * PANEL_SIZE + 40))
        text2surf, rect = GAME_FONT_BIG.render("2", (126, 176, 225))
        screen.blit(text2surf, (7 * PANEL_SIZE + 50, SCREEN_HEIGHT - 2 * PANEL_SIZE + 40))
        text3surf, rect = GAME_FONT_BIG.render("3", (198, 198, 117))
        screen.blit(text3surf, (8 * PANEL_SIZE + 50, SCREEN_HEIGHT - 2 * PANEL_SIZE + 40))
        text4surf, rect = GAME_FONT_BIG.render("4", (208, 125, 216))
        screen.blit(text4surf, (9 * PANEL_SIZE + 50, SCREEN_HEIGHT - 2 * PANEL_SIZE + 40))

    # show level text
    if not in_level:

        lvt = ""
        exec("lvt=LV_" + str(level) + "_DESC")
        draw_rect_alpha(screen, (124, 67, 29),
                        (300, 200, 600, 500))
        draw_rect_alpha(screen, (145, 85, 45),
                        (340, 240, 520, 420))
        lvt = lvt.split("\n")
        pygame.draw.rect(screen,(0,0,0),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT))
        txt1, txt2 = lvt[0], lvt[1]+"\n"+lvt[2]
        #124 chars
        tx2=txt2.split(" ")
        txt2=""
        leng=0
        for i in tx2:
            leng+=len(i)+1
            if leng<=124:
                txt2+=i+" "
            else:
                leng=len(i)+1
                txt2+="\n"+i+" "
        txt1surf, rect = GAME_FONT_BIG.render(txt1, (200, 200, 200))
        screen.blit(txt1surf, (20, 50))
        for i in range(len(txt2.split("\n"))):
            txt2surf, rect = GAME_FONT_SMALL.render(txt2.split("\n")[i], (200, 200, 200))
            screen.blit(txt2surf, (20, 120+40*i))
        showing_lv_text = True

    #if in_level:
     #   showing_lv_text = False
    # Update the display
    pygame.display.flip()

    if showing_lv_text:
        if seconds_passed>3:
            showing_lv_text = False
            in_level=True
            seconds_passed=0
