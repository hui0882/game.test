#导入模块
import pygame
import random

#初始化pygame
pygame.init()

#定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#下一步希望可玩家自主选择各项参数部分（start)
#设定界面
WIDTH, HEIGHT = 640, 480
#设置标准方块大小
BLOCK_SIZE = 20
#设置蛇的移动速度
SNAKE_SPEED = 15
#(end)

# 创建屏幕和时钟
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇(测试)plus")
clock = pygame.time.Clock()

#绘制蛇
snake = [(5, 5), (4, 5), (3, 5)]
#绘制食物
food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1), random.randint(0, (HEIGHT // BLOCK_SIZE) - 1))
direction = (1, 0)


#定义蛇和食物的尺寸（因需实时绘制蛇和食物的位置，这个函数的定义不能与下面的绘制部分合并）
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * BLOCK_SIZE, food[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


#游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #键盘控制
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

                #蛇的移动
    head = snake[0]
    new_head = ((head[0] + direction[0]) % (WIDTH // BLOCK_SIZE), (head[1] + direction[1]) % (HEIGHT // BLOCK_SIZE))
    snake.insert(0, new_head)

    #检查是否吃到食物
    if new_head == food:
        #吃掉后随机生成食物
        food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1), random.randint(0, (HEIGHT // BLOCK_SIZE) - 1))
    else:
        snake.pop()

        #检查是否因为太饿咬了自己一口
    if len(snake) > 2:
        for segment in snake[1:]:
            if new_head == segment:
                running = False

                #清屏
    screen.fill(WHITE)

    #绘制蛇和食物
    draw_snake(snake)
    draw_food(food)

    #更新屏幕
    pygame.display.flip()

    #控制帧率（从而控制蛇的移动速度）
    clock.tick(SNAKE_SPEED)

pygame.quit()