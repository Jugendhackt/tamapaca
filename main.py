from Alpaca import Alpaca
import gc
import time
import random

from Alpaca.SSD1351 import Display

gc.enable()
alpaca = Alpaca.Alpaca('morgan')
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
bs = 0

x = 0
y = 0

def draw_alpaca(x,y,colors):
	alpaca.display.fill_rect(x+20, y+25, 10, 5, colors)
	alpaca.display.fill_rect(x+45, y+25, 10, 5, colors)
	alpaca.display.fill_rect(x+15, y+30, 20, 5, colors)
	alpaca.display.fill_rect(x+40, y+30, 20, 5, colors)
	alpaca.display.fill_rect(x+10, y+35, 55, 35, colors)
	alpaca.display.fill_rect(x+15, y+70, 45, 5, colors)
	alpaca.display.fill_rect(x+20, y+75, 35, 5, colors)
	alpaca.display.fill_rect(x+20, y+45, 35, 5, alpaca.display.rgb_to_rgb565(252, 252, 250))
	alpaca.display.fill_rect(x+15, y+50, 45, 15, alpaca.display.rgb_to_rgb565(252, 252, 250))
	alpaca.display.fill_rect(x+20, y+65, 35, 5, alpaca.display.rgb_to_rgb565(252, 252, 250))
	alpaca.display.fill_rect(x+25, y+70, 25, 5, alpaca.display.rgb_to_rgb565(252, 252, 250))
	alpaca.display.fill_rect(x+20, y+55, 5, 5, 0x000)
	alpaca.display.fill_rect(x+50, y+55, 5, 5, 0x000)
	alpaca.display.fill_rect(x+30, y+60, 5, 10, 0x000)
	alpaca.display.fill_rect(x+40, y+60, 5, 10, 0x000)
	alpaca.display.fill_rect(x+35, y+65, 5, 5, 0x000)



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
    		
	if alpaca.dpad.right:
		x = x+1
		
	if alpaca.dpad.left:
		x = x-1
		
	if alpaca.dpad.up:
		y = y-1
		
	if alpaca.dpad.down:
		y = y+1

        if not (zufall == 10 or zufall == 50 or zufall == 90):
                zufall = random.randint(0,1000) 
        else:
                if alpaca.a.pressed:
                        zufall = 0
        
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

        draw_alpaca(x,y,alpaca.display.rgb_to_rgb565(colors[c][0],colors[c][1], colors[c][2]))

        m = 3
        #display
        alpaca.display.fill_rect(10 * m, 15 * m, 25 * m, 20 * m, alpaca.display.rgb_to_rgb565(0, 165, 224)) #blau
        #keyboard
        alpaca.display.fill_rect(7 * m, 33 * m, 30 * m, 4 * m, alpaca.display.rgb_to_rgb565(255, 255, 0)) #gelb u
        alpaca.display.fill_rect(9 * m, 29 * m, 27 * m, 4 * m, alpaca.display.rgb_to_rgb565(255, 255, 0)) #gelb o
        #outline
        alpaca.display.fill_rect(9 * m, 15 * m, 1 * m, 14 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s3h
        alpaca.display.fill_rect(10 * m, 14 * m, 25 * m, 1 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))  #s3s
        alpaca.display.fill_rect(35 * m, 15 * m, 1 * m, 14 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s4h
        alpaca.display.fill_rect(10 * m, 28 * m, 25 * m, 1 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s2s
        alpaca.display.fill_rect(8 * m, 29 * m, 1 * m, 4 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s2h
        alpaca.display.fill_rect(7 * m, 33 * m, 1 * m, 4 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s1h
        alpaca.display.fill_rect(7 * m, 37 * m, 31 * m, 1 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s1s
        alpaca.display.fill_rect(37 * m, 33 * m, 1 * m, 4 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s6h
        alpaca.display.fill_rect(36 * m, 29 * m, 1 * m, 4 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #s5h
        #keys
        alpaca.display.fill_rect(11 * m, 30 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0)) #t1o
        alpaca.display.fill_rect(15 * m, 30 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
        alpaca.display.fill_rect(19 * m, 30 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
        alpaca.display.fill_rect(23 * m, 30 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
        alpaca.display.fill_rect(27 * m, 30 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
        alpaca.display.fill_rect(31 * m, 30 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))

        alpaca.display.fill_rect(9 * m, 34 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
        alpaca.display.fill_rect(13 * m, 34 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
        alpaca.display.fill_rect(17 * m, 34 * m, 10 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
        #alpaca.display.fill_rect(21 * m, 34 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(50, 50, 50))
        #alpaca.display.fill_rect(25 * m, 34 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(50, 50, 50))
        alpaca.display.fill_rect(29 * m, 34 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))
        alpaca.display.fill_rect(33 * m, 34 * m, 2 * m, 2 * m, alpaca.display.rgb_to_rgb565(140, 0, 0))


        if zufall == 10:
                alpaca.render_text("Ich habe Hunger!", 12, alpaca.display.rgb_to_rgb565(255, 255, 255))
                
        if zufall == 50:
                alpaca.render_text("Ich habe Durst!", 12, alpaca.display.rgb_to_rgb565(255, 255, 255))
                
        if zufall == 90:
                alpaca.render_text("Ich will Spielen!", 12, alpaca.display.rgb_to_rgb565(255, 255, 255)) 
        
        alpaca.display.show()
        time.sleep(0.05)

