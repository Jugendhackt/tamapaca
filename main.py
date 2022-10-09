from Alpaca import Alpaca
import gc
import time
import random

from Alpaca.SSD1351 import Display

gc.enable()
alpaca = Alpaca.Alpaca('tamagotchi')
alpaca.display.init()

class Statusbar:
    def __init__(self, alpaca: Alpaca, x: int, y: int, x_0: int = 0, y_0: int = 0):
        self.alpaca = alpaca
        self.x_0 = x_0
        self.y_0 = y_0
        self.x = x
        self.y = y
        self.redraw_counter = 20
        self.update_counter = 200
        self.battery_level = int(alpaca.battery.get_percentage() * 100)
        self.show_nick = False
        self.switch_after = 20
        self.battery_color = 0x0f0
        self.nick_color = 0x00f
        self.banner_color = 0xfff
        if alpaca.display:
            # makes sure leftovers are blanked
            alpaca.display.fill_rect(self.x_0, self.y_0, x, y, 0x000)

    def render(self, display: Display):
        self.redraw_counter += 1
        if self.redraw_counter > self.switch_after:
            self.redraw_counter = 0
            self.show_nick = not self.show_nick
            display.fill_rect(self.x_0, self.y_0, self.x, self.y, 0x000)
            bar = f"@{self.alpaca.nick}" if self.show_nick else "Jugend hackt"
            color = self.nick_color if self.show_nick else self.banner_color
            display.text(bar, 0, 0, display.rgb_to_rgb565(
                color & 0xf00,
                color & 0x0f0,
                color & 0x00f
            ))
            indicator = f"{self.battery_level}%"
            display.text(indicator, 128 - len(indicator) * 8, 0, display.rgb_to_rgb565(
                self.battery_color & 0xf00,
                self.battery_color & 0x0f0,
                self.battery_color & 0x00f
            ))

    def tick(self, alpaca: Alpaca):
        self.update_counter += 1
        if self.update_counter > 200:
            self.battery_level = int(alpaca.battery.get_percentage() * 100)
            self.battery_color = 0x0f0
            if self.battery_level < 70:
                self.battery_color = 0x00f
            if self.battery_level < 30:
                self.battery_color = 0xff0
            if self.battery_level < 10:
                self.battery_color = 0xf00
            self.update_counter = 0

    def set_nick_color(self, color: int):
        self.nick_color = color

    def set_banner_color(self, color: int):
        self.banner_color = color

    def set_battery_color(self, color: int):
        self.battery_color = color


colors = [[0, 255, 0], [0, 0, 255], [255, 0, 0], [255, 255, 0], [0, 255, 255], [255, 0, 255], [255, 255, 255]]
c = 0
zufall = 0
bd = 0
bh = 0
bs = 20

x = 0
y = 0

alpacax = 0
alpacay = 0

matex = 0
matey = 0

def draw_alpaca(alpacax,alpacay,colors):
	alpaca.display.fill_rect(alpacax+20, alpacay+25, 10, 5, colors)
	alpaca.display.fill_rect(alpacax+45, alpacay+25, 10, 5, colors)
	alpaca.display.fill_rect(alpacax+15, alpacay+30, 20, 5, colors)
	alpaca.display.fill_rect(alpacax+40, alpacay+30, 20, 5, colors)
	alpaca.display.fill_rect(alpacax+10, alpacay+35, 55, 35, colors)
	alpaca.display.fill_rect(alpacax+15, alpacay+70, 45, 5, colors)
	alpaca.display.fill_rect(alpacax+20, alpacay+75, 35, 5, colors)
	alpaca.display.fill_rect(alpacax+20, alpacay+45, 35, 5, alpaca.display.rgb_to_rgb565(252, 252, 250))
	alpaca.display.fill_rect(alpacax+15, alpacay+50, 45, 15, alpaca.display.rgb_to_rgb565(252, 252, 250))
	alpaca.display.fill_rect(alpacax+20, alpacay+65, 35, 5, alpaca.display.rgb_to_rgb565(252, 252, 250))
	alpaca.display.fill_rect(alpacax+25, alpacay+70, 25, 5, alpaca.display.rgb_to_rgb565(252, 252, 250))
	alpaca.display.fill_rect(alpacax+20, alpacay+55, 5, 5, 0x000)
	alpaca.display.fill_rect(alpacax+50, alpacay+55, 5, 5, 0x000)
	alpaca.display.fill_rect(alpacax+30, alpacay+60, 5, 10, 0x000)
	alpaca.display.fill_rect(alpacax+40, alpacay+60, 5, 10, 0x000)
	alpaca.display.fill_rect(alpacax+35, alpacay+65, 5, 5, 0x000)

def draw_pizza(m=1, x=0, y=0):
	#crust
	alpaca.display.fill_rect(m * 2 + x, m * 2 + y, m * 25, m * 7, alpaca.display.rgb_to_rgb565(255, 150, 0))
	#cheese
	alpaca.display.fill_rect(m * 14 + x, m * 7 + y, m * 6, m * 2, alpaca.display.rgb_to_rgb565(255, 255, 0))
	alpaca.display.fill_rect(m * 2 + x, m * 9 + y, m * 25, m * 12, alpaca.display.rgb_to_rgb565(255, 255, 0))
	alpaca.display.fill_rect(m * 6 + x, m * 21 + y, m * 17, m * 7, alpaca.display.rgb_to_rgb565(255, 255, 0))
	alpaca.display.fill_rect(m * 10 + x, m * 28 + y, m * 9, m * 6, alpaca.display.rgb_to_rgb565(255, 255, 0))
	alpaca.display.fill_rect(m * 12 + x, m * 34 + y, m * 2, m * 4, alpaca.display.rgb_to_rgb565(255, 255, 0))
	#peperoni
	alpaca.display.fill_rect(m * 17 + x, m * 9 + y, m * 3, m * 8, alpaca.display.rgb_to_rgb565(255, 0, 0))
	alpaca.display.fill_rect(m * 15 + x, m * 11 + y, m * 7, m * 4, alpaca.display.rgb_to_rgb565(255, 0, 0))
	alpaca.display.fill_rect(m * 18 + x, m * 19 + y, m * 3, m * 8, alpaca.display.rgb_to_rgb565(255, 0, 0))
	alpaca.display.fill_rect(m * 16 + x, m * 21 + y, m * 7, m * 4, alpaca.display.rgb_to_rgb565(255, 0, 0))
	alpaca.display.fill_rect(m * 4 + x, m * 12 + y, m * 3, m * 8, alpaca.display.rgb_to_rgb565(255, 0, 0))
	alpaca.display.fill_rect(m * 2 + x, m * 14 + y, m * 7, m * 4, alpaca.display.rgb_to_rgb565(255, 0, 0))
	alpaca.display.fill_rect(m * 8 + x, m * 21 + y, m * 3, m * 8, alpaca.display.rgb_to_rgb565(255, 0, 0))
	alpaca.display.fill_rect(m * 6 + x, m * 23 + y, m * 7, m * 4, alpaca.display.rgb_to_rgb565(255, 0, 0))
	#outline
	alpaca.display.fill_rect(m * 6 + x, m * 0 + y, m * 16, m * 2, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 2 + x, m * 2 + y, m * 4, m * 2, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 22 + x, m * 2 + y, m * 5, m * 2, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 0 + x, m * 4 + y, m * 2, m * 11, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 27 + x, m * 4 + y, m * 2, m * 11, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 2 + x, m * 15 + y, m * 2, m * 6, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 25 + x, m * 15 + y, m * 2, m * 6, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 4 + x, m * 21 + y, m * 2, m * 3, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 23 + x, m * 21 + y, m * 2, m * 3, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 6 + x, m * 24 + y, m * 2, m * 4, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 21 + x, m * 24 + y, m * 2, m * 4, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 8 + x, m * 28 + y, m * 2, m * 6, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 19 + x, m * 28 + y, m * 2, m * 4, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 14 + x, m * 32 + y, m * 5, m * 2, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 10 + x, m * 34 + y, m * 2, m * 4, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 14 + x, m * 34 + y, m * 2, m * 4, alpaca.display.rgb_to_rgb565(140, 0, 0))
	alpaca.display.fill_rect(m * 12 + x, m * 38 + y, m * 2, m * 2, alpaca.display.rgb_to_rgb565(140, 0, 0))


def draw_mate(matex,matey):
    alpaca.display.fill_rect(matex+20, matey+15, 30, 40, alpaca.display.rgb_to_rgb565(186, 130, 29))
    alpaca.display.fill_rect(matex+27, matey+5, 16, 10, alpaca.display.rgb_to_rgb565(209, 146, 33))
    alpaca.display.fill_rect(matex+27, matey+0, 16, 5, alpaca.display.rgb_to_rgb565(62, 25, 255))
    alpaca.display.fill_rect(matex+20, matey+25, 30, 30, alpaca.display.rgb_to_rgb565(255, 208, 19))
    
def draw_computer(x = 0, y = 0, m = 1):
    #display
    alpaca.display.fill_rect(10 * m + x, 15 * m + y, 25 * m, 20 * m, alpaca.display.rgb_to_rgb565(0, 165, 224)) #blau
    #keyboard
    alpaca.display.fill_rect(7 * m + x, 33 * m + y, 30 * m, 4 * m, alpaca.display.rgb_to_rgb565(255, 255, 0)) #gelb u
    alpaca.display.fill_rect(9 * m + x, 29 * m + y, 27 * m, 4 * m, alpaca.display.rgb_to_rgb565(255, 255, 0)) #gelb o
    #outline
    alpaca.display.fill_rect(9 * m + x, 15 * m + y, 1 * m, 14 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s3h
    alpaca.display.fill_rect(10 * m + x, 14 * m + y, 25 * m, 1 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))  #s3s
    alpaca.display.fill_rect(35 * m + x, 15 * m + y, 1 * m, 14 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s4h
    alpaca.display.fill_rect(10 * m + x, 28 * m + y, 25 * m, 1 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s2s
    alpaca.display.fill_rect(8 * m + x, 29 * m + y, 1 * m, 4 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s2h
    alpaca.display.fill_rect(7 * m + x, 33 * m + y, 1 * m, 4 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s1h
    alpaca.display.fill_rect(7 * m + x, 37 * m + y, 31 * m, 1 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s1s
    alpaca.display.fill_rect(37 * m + x, 33 * m + y, 1 * m, 4 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s6h
    alpaca.display.fill_rect(36 * m + x, 29 * m + y, 1 * m, 4 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s5h
    #keys-upper
    alpaca.display.fill_rect(11 * m + x, 30 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #t1o
    alpaca.display.fill_rect(15 * m + x, 30 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
    alpaca.display.fill_rect(19 * m + x, 30 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
    alpaca.display.fill_rect(23 * m + x, 30 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
    alpaca.display.fill_rect(27 * m + x, 30 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
    alpaca.display.fill_rect(31 * m + x, 30 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
    #keys-lower
    alpaca.display.fill_rect(9 * m + x, 34 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
    alpaca.display.fill_rect(13 * m + x, 34 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
    alpaca.display.fill_rect(29 * m + x, 34 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
    alpaca.display.fill_rect(17 * m + x, 34 * m + y, 10 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
    alpaca.display.fill_rect(33 * m + x, 34 * m + y, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))


push= False

statusbar = Statusbar(alpaca, 128, 8)

alpaca.display.fill(alpaca.display.rgb_to_rgb565(252, 252, 250))


while True:
    if alpaca.dpad.push:
        if push == False:
            c = c+1
        push = True
        if c == len(colors):
            c = 0
    else: 
        push= False

        
        alpaca.display.fill_rect(0, 8, 128, 128 - 8, 0x000)

        statusbar.render(alpaca.display)

        statusbar.tick(alpaca)
        # alpaca.render_text(f"alpaca", 2, alpaca.display.rgb_to_rgb565(252, 186, 3))
        # alpaca.render_text(f"UP: {('YES' if alpaca.dpad.up else 'NO')}", 3, (0x0f0 if alpaca.dpad.up else 0x00f))
        # alpaca.render_text(f"DOWN: {('YES' if alpaca.dpad.down else 'NO')}", 4, (0x0f0 if alpaca.dpad.down else 0x00f))
        # alpaca.render_text(f"LEFT: {('YES' if alpaca.dpad.left else 'NO')}", 5, (0x0f0 if alpaca.dpad.left else 0x00f))
        # alpaca.render_text(f"RIGHT: {('YES' if alpaca.dpad.right else 'NO')}", 6, (0x0f0 if alpaca.dpad.right else 0x00f))
        # alpaca.render_text(f"SELECT: {('YES' if alpaca.dpad.push else 'NO')}", 7, (0x0f0 if alpaca.dpad.push else 0x00f))
        # alpaca.render_text(f"A: {('YES' if alpaca.a.pressed else 'NO')}", 8, (0x0f0 if alpaca.a.pressed else 0x00f))
        # alpaca.render_text(f"B: {('YES' if alpaca.b.pressed else 'NO')}", 9, (0x0f0 if alpaca.b.pressed else 0x00f))

        # alpaca.render_text("MAC Address", 10, 0xfff)
        # alpaca.render_text(f"{alpaca.mac}", 11, 0xfff)

        alpaca.display.fill_rect(x+20, y+25, 10, 5, alpaca.display.rgb_to_rgb565(colors[c][0],colors[c][1], colors[c][2]))
        alpaca.display.fill_rect(x+45, y+25, 10, 5, alpaca.display.rgb_to_rgb565(colors[c][0],colors[c][1], colors[c][2]))
        alpaca.display.fill_rect(x+15, y+30, 20, 5, alpaca.display.rgb_to_rgb565(colors[c][0],colors[c][1], colors[c][2]))
        alpaca.display.fill_rect(x+40, y+30, 20, 5, alpaca.display.rgb_to_rgb565(colors[c][0],colors[c][1], colors[c][2]))
        alpaca.display.fill_rect(x+10, y+35, 55, 35, alpaca.display.rgb_to_rgb565(colors[c][0],colors[c][1], colors[c][2]))
        alpaca.display.fill_rect(x+15, y+70, 45, 5, alpaca.display.rgb_to_rgb565(colors[c][0],colors[c][1], colors[c][2]))
        alpaca.display.fill_rect(x+20, y+75, 35, 5, alpaca.display.rgb_to_rgb565(colors[c][0],colors[c][1], colors[c][2]))
        alpaca.display.fill_rect(x+20, y+45, 35, 5, alpaca.display.rgb_to_rgb565(252, 252, 250))
        alpaca.display.fill_rect(x+15, y+50, 45, 15, alpaca.display.rgb_to_rgb565(252, 252, 250))
        alpaca.display.fill_rect(x+20, y+65, 35, 5, alpaca.display.rgb_to_rgb565(252, 252, 250))
        alpaca.display.fill_rect(x+25, y+70, 25, 5, alpaca.display.rgb_to_rgb565(252, 252, 250))
        alpaca.display.fill_rect(x+20, y+55, 5, 5, 0x000)
        alpaca.display.fill_rect(x+50, y+55, 5, 5, 0x000)
        alpaca.display.fill_rect(x+30, y+60, 5, 10, 0x000)
        alpaca.display.fill_rect(x+40, y+60, 5, 10, 0x000)
        alpaca.display.fill_rect(x+35, y+65, 5, 5, 0x000)

        alpaca.display.fill_rect(0, 20, 47, 8, 0x000)
        alpaca.render_text("Hunger", 2, alpaca.display.rgb_to_rgb565(255, 255, 255))
        alpaca.display.fill_rect(2, 30, bh+1, 5, alpaca.display.rgb_to_rgb565(255, 255, 255))
        
        alpaca.display.fill_rect(0, 40, 40, 8, 0x000)
        alpaca.render_text("Durst", 4, alpaca.display.rgb_to_rgb565(255, 255, 255))
        alpaca.display.fill_rect(2, 50, bd+1, 5, alpaca.display.rgb_to_rgb565(255, 255, 255))
        
        alpaca.display.fill_rect(0, 60, 39, 8, 0x000)
        alpaca.render_text("Spass", 6, alpaca.display.rgb_to_rgb565(255, 255, 255))
        alpaca.display.fill_rect(2, 70, bs+1, 5, alpaca.display.rgb_to_rgb565(255, 255, 255))

        zufall = random.randint(0,100)

		if (zufall == 10 and bh < 20):
			bh = bh+1
		if bh == 20:
			alpaca.render_text("Ich habe Hunger!", 12, alpaca.display.rgb_to_rgb565(255, 255, 255))
		elif bd == 20:
			alpaca.render_text("Ich habe Durst!", 12, alpaca.display.rgb_to_rgb565(255, 255, 255))
		elif bs == 0:
			alpaca.render_text("Ich will Spielen!", 12, alpaca.display.rgb_to_rgb565(255, 255, 255))

		if (zufall == 50 and bd < 20):
			bd = bd+1

		if (zufall == 90 and bs > 0):
			bs = bs-1


		if alpaca.dpad.right:
			x = x+1

		if alpaca.dpad.left:
			x = x-1

		if alpaca.dpad.up:
			y = y-1

		if alpaca.dpad.down:
			y = y+1

		if alpaca.a.pressed:
			draw_pizza(50, 90)

		if alpaca.b.pressed:
			draw_computer(90, 90)

        alpaca.display.show()
        print("updated")
        time.sleep(0.05)

