import turtle as tt
import pygame as pg
import time
import random
from format_module import *


# tạo âm thanh thư viện pygame
pg.mixer.init()
pg.mixer.music.load(r'D:\IT\python\SPHP2\musics\background.mp3')
sound_coin = pg.mixer.Sound(r'D:\IT\python\SPHP2\musics\coin.mp3')
sound_win = pg.mixer.Sound(r'D:\IT\python\SPHP2\musics\victory.mp3')
sound_lose = pg.mixer.Sound(r'D:\IT\python\SPHP2\musics\lose.mp3')
sound_beam = pg.mixer.Sound(r'D:\IT\python\SPHP2\musics\beam.mp3')

# tạo màn hình
bg = tt.Screen()
bg.setup(1000,600)
bg.title('Zgame')
bg.bgcolor('red')
bg.bgpic(r'D:\IT\python\SPHP2\imgs\background.png')

#tao khối nhân vật
bg.addshape(r'D:\IT\python\SPHP2\imgs\blue.gif')
bg.addshape(r'D:\IT\python\SPHP2\imgs\red.gif')
bg.addshape(r'D:\IT\python\SPHP2\imgs\monster.gif')

#tạo 2 điểm và định vị trên màn hình
blue =  tt.Turtle()
blue.shape(r'D:\IT\python\SPHP2\imgs\blue.gif')
blue.penup()
blue.goto(200,0)

red =  tt.Turtle()
red.shape(r'D:\IT\python\SPHP2\imgs\red.gif')
red.penup()
red.goto(-200,0)

#tạo văn bản xuất hiện trên màn hình khi game bắt đầu
tt_text = tt.Turtle()
tt_text.penup()
tt_text.hideturtle()
tt_text.goto(0,100)
tt_text.write('Enter R to choose Red / B to choose Blue', align= 'center', font= ('Arial',20,'bold'))

#tạo và hiển thị các quả bóng ngẫu nhiên
balls = []
def create_random_score():
    for _ in range(7):
        ball = tt.Turtle()
        ball.hideturtle()
        ball.penup()
        ball.goto(random.randint(-480,480), random.randint(-280, 280))
        ball.shape('circle')
        ball.shapesize(2)
        ball.color(random.choice(['red', 'blue', 'green', 'yellow', 'orange']))
        ball.showturtle()
        balls.append(ball)
    update_score()

# điều khiển người chơi
tt_player = tt.Turtle() #tạo người chơi
tt_player.hideturtle() #ẩn người chơi
tt_player.penup()  #không để lại đường kẻ

def choose_red():
    blue.hideturtle() # ẩn
    red.hideturtle() # ẩn
    tt_player.shape(r'D:\IT\python\SPHP2\imgs\red.gif') 
    tt_player.showturtle() #hiện người chơi
    tt_text.clear()# xóa thông báo bắt đầu
    
    create_random_score() #tạo bóng ngẫu nhiên
    pg.mixer.music.play(-1) #phát nhạc nền
    generate_monster(5) # tạo monster
        
def choose_blue(): # tương tự choose_red
    blue.hideturtle()
    red.hideturtle()
    tt_player.shape(r'D:\IT\python\SPHP2\imgs\blue.gif')
    tt_player.showturtle()
    tt_text.clear()
    create_random_score()
    pg.mixer.music.play(-1)
    generate_monster(5)
    
def get_x_coordinate():#lấy tọa độ x người chơi
    return tt_player.xcor()
def get_y_coordinate():#lấy tọa độ y người chơi
    return tt_player.ycor()
def left():# di chuyển bằng cách thay đổi tọa độ 
    tt_player.goto(get_x_coordinate() - 10, get_y_coordinate())
    is_touch_ball() #chạm bóng
    is_touch_edge() # chạm cạnh
def right(): #tương tự left
    tt_player.goto(get_x_coordinate() + 10, get_y_coordinate())
    is_touch_ball()
    is_touch_edge()
def up():#tương tự left
    tt_player.goto(get_x_coordinate(), get_y_coordinate() + 10)
    is_touch_ball()
    is_touch_edge()
def down():#tương tự left
    tt_player.goto(get_x_coordinate(), get_y_coordinate() - 10)
    is_touch_ball()
    is_touch_edge()
#điểm số và kiếm tra va chạm
score = -1
def update_score(): #cập nhật điểm
    global score
    score += 1 #tăng điểm
    tt_text.clear()
    tt_text.goto(-400, 250)
    tt_text.write(f'Score: {score}', align= 'center', font= ('Arial',20,'bold'))

def is_touch_ball(): #kiểm tra người chơi có chạm bóng hay không
    for ball in balls:#lặp qua tất cả các quả bóng
        if ball.distance(tt_player) < 20: # nếu khoảng cách tới bóng nhỏ hơn 20
            sound_coin.play() #phát âm thanh
            ball.hideturtle() # ẩn bóng
            balls.remove(ball)# xóa khỏi danh sách bóng
            update_score() #cập nhật điếm
            if len(balls) == 0: # nếu ko còn quả bóng nào
                sound_win.play() #phát âm  thanh win
                tt_text.goto(0,0) # di chuyển chuột tới 0,0
                tt_text.write('You win', align= 'center', font= ('Arial',40,'bold')) # hiện chữ win
             
def is_touch_edge(): #kiểm tra người chơi có chạm cạnh không
    if abs(tt_player.xcor()) > 480 or abs(tt_player.ycor()) > 280: # nếu x hoặc y vượt
        sound_lose.play() # phát âm thanh thua
        tt_text.goto(0,0) # chữ xuất hiện ở 0,0
        bg.clear() #xóa nền để thấy rõ thông báo
        tt_text.write('You loose', align= 'center', font= ('Arial',40,'bold')) #hiện thua

#
monsters = []

def generate_monster(monster_quantity):# Tạo và khởi tạo số lượng monster được chỉ định
    for _ in range(monster_quantity): #lặp từng monster
        monster = tt.Turtle()
        monster.penup()
        monster.hideturtle()
        monster.speed(random.randint(1,4)) #tốc độ ngẫu nhiên
        monster.shape(r'D:\IT\python\SPHP2\imgs\monster.gif') # đặt hình monster
        monster.goto(random.randint(-480,480), random.randint(-240,240)) #vị trí ban đầu ngẫu nhiên
        monster.showturtle() #hiện monster
        
        monsters.append(monster)
    move_monster() #di chuyển
def move_monster(): #hàm di chuyển
    time.sleep(3) # chờ 3 giây
    while True: 
        for monster in monsters:
            monster.goto(random.randint(-480,480), random.randint(-240,240))
            
def is_touch_monster(): # kiểm tra va chạm của người
    for monster in monsters:
        if monster.distance(tt_player) < 20:
            sound_lose.play()
            tt_text.goto(0,0)
            bg.clear()
            tt_text.write('You loose', align= 'center', font= ('Arial',40,'bold')) 
    bg.ontimer(is_touch_monster, 100)
is_touch_monster() 
#
bg.onkey(choose_red,'r')
bg.onkey(choose_blue,'b')
bg.onkey(up,'Up')
bg.onkey(down,'Down')
bg.onkey(left,'Left')
bg.onkey(right,'Right')
# bg.onkey(beam,'Space')

bg.listen()

tt.done()

