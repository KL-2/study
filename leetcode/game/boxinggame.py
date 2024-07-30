# import turtle
# import math

# #pygame.init()
# #pygame.mixer.init()

# # Screen set up
# window = turtle.Screen()
# window.bgcolor("beige")
# window.title("Boxing Game")

# # Images of characters
# player_boxer = "D:\code\study\leetcode\game\Boxer.gif"
# enemy_boxer = "D:\code\study\leetcode\game\Boxer.gif"
# window.addshape(player_boxer)
# window.addshape(enemy_boxer)

# # Draw ring for boxers
# border_pen = turtle.Turtle()
# border_pen.speed(0)
# border_pen.color("white")
# border_pen.width(5)
# border_pen.penup()
# border_pen.setposition(-200, -200)
# border_pen.pendown()
# border_pen.pensize(5)
# for side in range(4):
#     border_pen.fd(400)
#     border_pen.lt(90)
# border_pen.hideturtle()

# # Create the player turtle
# player = turtle.Turtle()
# player.shape(player_boxer)
# player.penup()
# player.speed(0)
# player.setposition(0, -150)
# player.setheading(90)

# playerspeed = 15
# enemyspeed = 2

# # Create the enemy
# enemy = turtle.Turtle()
# enemy.color("red")
# enemy.shape(enemy_boxer)
# enemy.penup()
# enemy.speed(3)
# enemy.setposition(-100, 100)

# # Create beginning score as zero
# score = 0

# # Move the player left, right, up, and down
# def move_left():
#     x = player.xcor()
#     x -= playerspeed
#     if x < -200:
#         x = -200
#     player.setx(x)

# def move_right():
#     x = player.xcor()
#     x += playerspeed
#     if x > 200:
#         x = 200
#     player.setx(x)
    
# def move_forward():
#     y = player.ycor()
#     y += playerspeed
#     if y > 200:
#         y = 200
#     player.sety(y)
    
# def move_backward():
#     y = player.ycor()
#     y -= playerspeed
#     if y < -200:
#         y = -200
#     player.sety(y)

# # Create keyboard bindings
# turtle.listen()
# turtle.onkey(move_left, "Left")
# turtle.onkey(move_right, "Right")
# turtle.onkey(move_forward, "Up")
# turtle.onkey(move_backward, "Down")

# # Function to check for collision
# def is_collision(t1, t2):
#     distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
#     if distance < 15:
#         return True
#     else:
#         return False

# # Draw the score
# score_pen = turtle.Turtle()
# score_pen.speed(0)
# score_pen.color("black")
# score_pen.penup()
# score_pen.setposition(-195, 175)
# scorestring = "Score: %s" % score
# score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
# score_pen.hideturtle()

# # Main game loop
# while True:
#     # Move the enemy
#     x = enemy.xcor()
#     x += enemyspeed
#     enemy.setx(x)
    
#     # Move the enemy back and down
#     if enemy.xcor() > 200 or enemy.xcor() < -200:
#         y = enemy.ycor()
#         y -= 20
#         enemyspeed *= -1
#         enemy.sety(y)
    
#     # Check for a collision between the player and the enemy
#     if is_collision(player, enemy):
#         enemy.setposition(-100, 100)
#         score += 10
#         scorestring = "Score: %s" % score
#         score_pen.clear()
#         score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

# # Uncomment this section if using pygame for sound
# # Play background music
# # song = random.randint(0, 2)
# # if song == 0:
# #     sound = pygame.mixer.Sound("Star_Song.wav")
# # elif song == 1:
# #     sound = pygame.mixer.Sound("Telecom.wav")
# # elif song == 2:
# #     sound = pygame.mixer.Sound("User_Friendly_future_mix.wav")
# # sound.play()

# # Uncomment this section if using pygame for sound
# # winsound.PlaySound("Explosion.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

# delay = input("Press enter to finish.")
import random
import time

from colorama import Fore

# Define opponents' data
opponents = [
    {"health": 100, "name": "Jermimane Suckleding III", "damage": [5, 45]},
    {"health": 135, "name": "Christian Soro", "damage": [2, 30]},
    {"health": 75, "name": "Naum Angelevoski", "damage": [10, 60]}
]

# Initialize global variables
player_health = 100
current_opponent = 0


def check_player_health():
    """Check if the player's health reaches zero."""
    global player_health

    if player_health <= 0:
        print('You lose!!')
        time.sleep(1)
        print("You lost, leaving the arena...")
        time.sleep(1.5)
        input("Press enter to leave the arena: ")
        quit()


def check_opponent_health():
    """Check if the opponent's health reaches zero and update opponent."""
    global current_opponent, player_health

    if opponents[current_opponent]["health"] <= 0:
        if current_opponent < len(opponents) - 1:
            current_opponent += 1
            player_health = 100
            select_opponent()
        else:
            print("You win the championship!!")
            input("Leave the arena: ")
            quit()


def select_opponent():
    """Select the next opponent."""
    if not current_opponent >= len(opponents):
        print("Your opponent is...")
        time.sleep(1.5)
        print(opponents[current_opponent]["name"])
        time.sleep(0.5)


def countdown():
    """Display a countdown before the fight starts."""
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Fight!")


def player_damage():
    """Calculate damage dealt by the player."""
    return random.randint(5, 45)


def opponent_damage():
    """Calculate damage dealt by the opponent."""
    damage_range = opponents[current_opponent]['damage']
    return random.randint(damage_range[0], damage_range[1])


def player_turn():
    """Handle the player's turn."""

    # if current_opponent == len(opponents) - 1:
    #     return

    global player_health

    hit = input("1. Punch\n2. Block\n: ")

    if hit == "1":
        if random.randint(0, 100) < 20:
            damage_dealt = round(player_damage() * 1.35)
            print(Fore.LIGHTBLUE_EX + '\033[1m' + "You got a critical!" + '\033[0m')
        else:
            damage_dealt = player_damage()

        opponents[current_opponent]['health'] -= damage_dealt

        if opponents[current_opponent]['health'] > 0:
            print(Fore.LIGHTRED_EX + f"{opponents[current_opponent]['health']} HP left..." + Fore.RESET)
            time.sleep(2)
            opponent_dmg = opponent_damage()
            player_health -= opponent_dmg
            print(Fore.LIGHTGREEN_EX + f"You dealt {damage_dealt} damage to the opponent!" + Fore.RESET)
            print(f"You've been hit for {opponent_dmg}!")
            print(Fore.LIGHTRED_EX + f"You have {0 if player_health < 0 else player_health} health..." + Fore.RESET)
            check_player_health()
        else:
            check_opponent_health()
    elif hit == "2":
        player_health -= random.randint(5, 20)
        print(Fore.LIGHTRED_EX + f"You have {0 if player_health < 0 else player_health} health..." + Fore.RESET)
        check_player_health()


def main():
    select_opponent()
    countdown()
    print("Your Turn!")

    while True:
        if current_opponent == len(opponents):
            break
        else:
            player_turn()

    print("You Win!!!")


if __name__ == "__main__":
    main()