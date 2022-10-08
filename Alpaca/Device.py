from micropython import const

# Pin definitions
UART_TxD = const(1)
UART_RxD = const(3)

I2C_ID = const(1)
I2C_SCL = const(25)
I2C_SDA = const(26)
I2C_FREQ = const(100000)


SD_SPI_ID = const(2)
SD_SCK = const(18)
SD_CS = const(5)
SD_MISO = const(19)
SD_MOSI = const(23)
SD_PATH = None

OLED_SPI_ID = const(1)
OLED_CS = const(17)
OLED_SCK = const(14)
OLED_MOSI = const(13)
# OLED_MISO = const(12)
OLED_DC = const(21)
OLED_RES = const(16)

TOUCH_A = None
TOUCH_B = None

ADC_BAT = const(36)
ADC_AUX = const(39)

IR_Rx = const(5)
IR_Tx = const(27)

WS2812_PIN = const(32)
WS2812_NUM = const(6)

BTN_UP = const(35)
BTN_DOWN = const(33)
BTN_LEFT = const(34)
BTN_RIGHT = const(15)
BTN_PUSH = const(12)
# A and B are swapped in software here to have
# the layout similar to the gameboy limit
BTN_A = const(5)
BTN_B = const(4)

PPSI262_ADDR = const(0x5B)
SGP30_ADDR = const(0x58)
LIS2DE12_ADDR = const(0x19)
