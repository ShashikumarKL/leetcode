class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie1 = Cookie("green")
cookie2 = Cookie("blue")


print(cookie1.get_color())
print(cookie2.get_color())

cookie2.set_color("yellow")
print(cookie2.get_color())
