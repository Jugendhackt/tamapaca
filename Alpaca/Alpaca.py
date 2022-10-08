import binascii

import machine
import os

import time
from neopixel import NeoPixel

from Alpaca import Device
from Alpaca.SSD1351 import Display


class DPad:
    def __init__(self, up: int, down: int, left: int, right: int, push: int):
        Pin = machine.Pin
        Signal = machine.Signal
        self.up_signal = Signal(Pin(up, Pin.IN, pull=Pin.PULL_UP), invert=True)
        self.down_signal = Signal(Pin(down, Pin.IN, pull=Pin.PULL_UP), invert=True)
        self.left_signal = Signal(Pin(left, Pin.IN, pull=Pin.PULL_UP), invert=True)
        self.right_signal = Signal(Pin(right, Pin.IN, pull=Pin.PULL_UP), invert=True)
        self.push_signal = Signal(Pin(push, Pin.IN, pull=Pin.PULL_UP), invert=True)

    @property
    def up(self) -> bool:
        return self.up_signal.value() == 1

    @property
    def down(self) -> bool:
        return self.down_signal.value() == 1

    @property
    def left(self) -> bool:
        return self.left_signal.value() == 1

    @property
    def right(self) -> bool:
        return self.right_signal.value() == 1

    @property
    def push(self) -> bool:
        return self.push_signal.value() == 1


class Button:
    def __init__(self, pin: int):
        self.button = machine.Signal(machine.Pin(pin, machine.Pin.IN, pull=machine.Pin.PULL_UP), invert=True)

    @property
    def pressed(self) -> bool:
        return self.button.value() == 1


class Battery:
    def __init__(self, adc: int):
        self.battery = machine.ADC(machine.Pin(adc))
        self.voltage_empty = 3.55
        self.voltage_full = 4.2
        self._r1 = 453000
        self._r2 = 100000
        self._divider = (self._r2 / (self._r1 + self._r2))

    def get_percentage(self) -> int:
        out = -1
        voltage = self.get_voltage()
        if voltage > 3.775:
            out = 10.6 * voltage - 34.1
        if voltage > 3.64:
            out = 36.4 * voltage - 132
        if voltage > 3.525:
            out = 4 * voltage - 13.6
        if voltage > 3.0:
            out = 0.857 * voltage - 2.57
        else:
            out = 0.0
        out = out if out < 1.0 else 1.0
        out = out if out > 0 else 0.0
        return out

    def get_voltage(self) -> float:
        return (self.battery.read_uv() * ((self._r2 + self._r1) / self._r2)) / 1000000


class Alpaca:
    def __init__(self, nick: str = ""):
        self.i2c = machine.I2C(Device.I2C_ID, freq=Device.I2C_FREQ)
        self.sd_card = None
        self.battery = Battery(Device.ADC_BAT)
        self.display = Display(Device.OLED_SPI_ID, Device.OLED_CS, Device.OLED_DC, Device.OLED_RES)
        self.dpad = DPad(Device.BTN_UP, Device.BTN_DOWN, Device.BTN_LEFT, Device.BTN_RIGHT, Device.BTN_PUSH)
        self.a = Button(Device.BTN_A)
        self.b = Button(Device.BTN_B)
        self.neopixel = NeoPixel(machine.Pin(Device.WS2812_PIN, machine.Pin.OUT), Device.WS2812_NUM)
        self.nick = nick

    def hard_reset(self):
        self.__del__()
        machine.reset()

    def soft_reset(self):
        self.__del__()
        machine.soft_reset()

    @property
    def mac(self) -> str:
        # see documentation, in this micropython port, this is the mac address
        return binascii.hexlify(machine.unique_id()).decode("ascii")

    def render_text(self, s: str, row: int, color: int, center_x: bool = False, from_y_center: bool = False):
        x_offset = 0 if not center_x else 64 - 8 * int(len(s)/2)
        y_offset = 10 * row if not from_y_center else 64 - 10 * row
        self.display.text(s, x_offset, y_offset, self.display.rgb_to_rgb565(
            color & 0xf00, color & 0x0f0, color & 0x00f
        ))

    def __del__(self):
        if Device.SD_PATH:
            self.umount_SD()