class SuperHero:  
    def __init__(self, shape, color, speed):
        self.shape = shape
        self.color = color
        self.speed = speed
    def move (self, distance):
       # f-string {}
       print(f"hình {self.shape} màu {self.color} đang di chuyển {distance} tốc độ {self.speed}")
    def movebykey (self, key):
        direction = {
            'w' : 'lên trên',
            's' : 'xuống dưới',
            'a' : 'sang trái',
            'd' : 'sang phải'
        }
        if key in direction:
            print(f"hình {self.shape} màu {self.color} đang di chuyển {direction[key]} tốc độ {self.speed}")
        else:
            print("không hợp lệ trong w,a,s,d")
if __name__ == "__main__":
    hero = SuperHero('hình tròn', "đỏ", 10)
    hero.move(15)
    hero.movebykey('w')
    hero.movebykey('x')