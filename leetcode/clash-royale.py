import pygame
import random
import time

# 初始化Pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("文字版皇室战争")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 字体设置
font = pygame.font.SysFont("SimHei", 24)

# 单位和塔类
class Unit:
    def __init__(self, name, hp, damage, position, color):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.position = position
        self.color = color

    def attack(self, target):
        target.hp -= self.damage
        print(f"{self.name}攻击{target.name}，造成{self.damage}点伤害！")

class Tower:
    def __init__(self, name, hp, position, color):
        self.name = name
        self.hp = hp
        self.position = position
        self.color = color

class Player:
    def __init__(self, name, tower, elixir):
        self.name = name
        self.tower = tower
        self.elixir = elixir
        self.units = []

    def deploy_unit(self, unit_name, position):
        if self.elixir >= 5:
            if unit_name == "骑士":
                unit = Unit("骑士", 30, 10, position, BLUE)
            elif unit_name == "弓箭手":
                unit = Unit("弓箭手", 20, 5, position, GREEN)
            self.units.append(unit)
            self.elixir -= 5
            print(f"{self.name}部署了{unit_name}在位置{position}")
        else:
            print(f"{self.name}没有足够的圣水部署{unit_name}")

    def regenerate_elixir(self):
        self.elixir += 1
        if self.elixir > 10:
            self.elixir = 10

def display_game_state(screen, player, opponent):
    screen.fill(WHITE)

    # 绘制塔
    pygame.draw.rect(screen, player.tower.color, (player.tower.position[0], player.tower.position[1], 50, 100))
    pygame.draw.rect(screen, opponent.tower.color, (opponent.tower.position[0], opponent.tower.position[1], 50, 100))

    # 绘制塔HP
    player_tower_hp_text = font.render(f"{player.tower.name} HP: {player.tower.hp}", True, BLACK)
    screen.blit(player_tower_hp_text, (player.tower.position[0], player.tower.position[1] - 30))
    opponent_tower_hp_text = font.render(f"{opponent.tower.name} HP: {opponent.tower.hp}", True, BLACK)
    screen.blit(opponent_tower_hp_text, (opponent.tower.position[0], opponent.tower.position[1] - 30))

    # 绘制单位
    for unit in player.units:
        pygame.draw.circle(screen, unit.color, unit.position, 20)
        unit_hp_text = font.render(f"{unit.name} HP: {unit.hp}", True, BLACK)
        screen.blit(unit_hp_text, (unit.position[0] - 20, unit.position[1] - 40))

    for unit in opponent.units:
        pygame.draw.circle(screen, unit.color, unit.position, 20)
        unit_hp_text = font.render(f"{unit.name} HP: {unit.hp}", True, BLACK)
        screen.blit(unit_hp_text, (unit.position[0] - 20, unit.position[1] - 40))

    # 显示圣水
    elixir_text = font.render(f"圣水: {player.elixir}", True, BLACK)
    screen.blit(elixir_text, (10, screen_height - 30))

    pygame.display.flip()

def game_loop():
    player = Player("玩家", Tower("玩家塔", 100, (50, screen_height//2 - 50), RED), 10)
    opponent = Player("电脑", Tower("电脑塔", 100, (screen_width - 100, screen_height//2 - 50), BLACK), 10)

    running = True
    clock = pygame.time.Clock()
    round_count = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 玩家行动
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and player.elixir >= 5:
            player.deploy_unit("骑士", (100, screen_height//2))
        elif keys[pygame.K_2] and player.elixir >= 5:
            player.deploy_unit("弓箭手", (100, screen_height//2 + 50))

        # 简单的电脑AI行动
        if opponent.elixir >= 5:
            if random.choice([True, False]):
                opponent.deploy_unit("骑士", (screen_width - 150, screen_height//2))
            else:
                opponent.deploy_unit("弓箭手", (screen_width - 150, screen_height//2 + 50))

        # 单位攻击
        for unit in player.units:
            if opponent.units:
                unit.attack(opponent.units[0])
                if opponent.units[0].hp <= 0:
                    print(f"{opponent.units[0].name}被击败了！")
                    opponent.units.pop(0)
            else:
                unit.attack(opponent.tower)
                if opponent.tower.hp <= 0:
                    print(f"{opponent.tower.name}被摧毁了！")
                    running = False

        for unit in opponent.units:
            if player.units:
                unit.attack(player.units[0])
                if player.units[0].hp <= 0:
                    print(f"{player.units[0].name}被击败了！")
                    player.units.pop(0)
            else:
                unit.attack(player.tower)
                if player.tower.hp <= 0:
                    print(f"{player.tower.name}被摧毁了！")
                    running = False

        # 更新状态
        player.regenerate_elixir()
        opponent.regenerate_elixir()

        display_game_state(screen, player, opponent)
        clock.tick(30)  # 降低帧率到30
        round_count += 1

        # 每回合结束后增加等待时间
        time.sleep(1)  # 延时1秒

    if player.tower.hp > 0:
        print(f"{player.name}胜利了！")
    else:
        print(f"{opponent.name}胜利了！")

    pygame.quit()

# 开始游戏循环
game_loop()
