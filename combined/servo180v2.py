# Import libraries
import RPi.GPIO as GPIO
from sun_posv3 import Sunpos
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(40,GPIO.OUT)
servo1 = GPIO.PWM(40,50) # Note 11 is pin, 50 = 50Hz pulse
servo1.start(0)

class Servo180:

    def startingPos(self):
      servo1.ChangeDutyCycle(7)
      time.sleep(0.5)
      servo1.ChangeDutyCycle(0)


    def mover_motor(self):
      sunpos = Sunpos()
      anglesMap = {
        0: 2.8,
        1: 2.847,
        2: 2.894,
        3: 2.9410000000000003,
        4: 2.9880000000000004,
        5: 3.0350000000000006,
        6: 3.0820000000000007,
        7: 3.129000000000001,
        8: 3.176000000000001,
        9: 3.223000000000001,
        10: 3.2700000000000014,
        11: 3.3170000000000015,
        12: 3.3640000000000017,
        13: 3.411000000000002,
        14: 3.458000000000002,
        15: 3.505000000000002,
        16: 3.5520000000000023,
        17: 3.5990000000000024,
        18: 3.6460000000000026,
        19: 3.6930000000000027,
        20: 3.740000000000003,
        21: 3.787000000000003,
        22: 3.834000000000003,
        23: 3.8810000000000033,
        24: 3.9280000000000035,
        25: 3.9750000000000036,
        26: 4.022000000000004,
        27: 4.0690000000000035,
        28: 4.116000000000003,
        29: 4.163000000000003,
        30: 4.210000000000003,
        31: 4.257000000000002,
        32: 4.304000000000002,
        33: 4.351000000000002,
        34: 4.3980000000000015,
        35: 4.445000000000001,
        36: 4.492000000000001,
        37: 4.539000000000001,
        38: 4.586,
        39: 4.633,
        40: 4.68,
        41: 4.726999999999999,
        42: 4.773999999999999,
        43: 4.820999999999999,
        44: 4.8679999999999986,
        45: 4.914999999999998,
        46: 4.961999999999998,
        47: 5.008999999999998,
        48: 5.055999999999997,
        49: 5.102999999999997,
        50: 5.149999999999997,
        51: 5.1969999999999965,
        52: 5.243999999999996,
        53: 5.290999999999996,
        54: 5.337999999999996,
        55: 5.384999999999995,
        56: 5.431999999999995,
        57: 5.478999999999995,
        58: 5.5259999999999945,
        59: 5.572999999999994,
        60: 5.619999999999994,
        61: 5.666999999999994,
        62: 5.713999999999993,
        63: 5.760999999999993,
        64: 5.807999999999993,
        65: 5.854999999999992,
        66: 5.901999999999992,
        67: 5.948999999999992,
        68: 5.995999999999992,
        69: 6.042999999999991,
        70: 6.089999999999991,
        71: 6.136999999999991,
        72: 6.18399999999999,
        73: 6.23099999999999,
        74: 6.27799999999999,
        75: 6.3249999999999895,
        76: 6.371999999999989,
        77: 6.418999999999989,
        78: 6.465999999999989,
        79: 6.512999999999988,
        80: 6.559999999999988,
        81: 6.606999999999988,
        82: 6.6539999999999875,
        83: 6.700999999999987,
        84: 6.747999999999987,
        85: 6.794999999999987,
        86: 6.841999999999986,
        87: 6.888999999999986,
        88: 6.935999999999986,
        89: 6.982999999999985,
        90: 7.029999999999985,
        91: 7.076999999999985,
        92: 7.123999999999985,
        93: 7.170999999999984,
        94: 7.217999999999984,
        95: 7.264999999999984,
        96: 7.311999999999983,
        97: 7.358999999999983,
        98: 7.405999999999983,
        99: 7.4529999999999825,
        100: 7.499999999999982,
        101: 7.546999999999982,
        102: 7.593999999999982,
        103: 7.640999999999981,
        104: 7.687999999999981,
        105: 7.734999999999981,
        106: 7.7819999999999805,
        107: 7.82899999999998,
        108: 7.87599999999998,
        109: 7.92299999999998,
        110: 7.969999999999979,
        111: 8.01699999999998,
        112: 8.06399999999998,
        113: 8.110999999999981,
        114: 8.157999999999982,
        115: 8.204999999999982,
        116: 8.251999999999983,
        117: 8.298999999999984,
        118: 8.345999999999984,
        119: 8.392999999999985,
        120: 8.439999999999985,
        121: 8.486999999999986,
        122: 8.533999999999986,
        123: 8.580999999999987,
        124: 8.627999999999988,
        125: 8.674999999999988,
        126: 8.721999999999989,
        127: 8.76899999999999,
        128: 8.81599999999999,
        129: 8.86299999999999,
        130: 8.909999999999991,
        131: 8.956999999999992,
        132: 9.003999999999992,
        133: 9.050999999999993,
        134: 9.097999999999994,
        135: 9.144999999999994,
        136: 9.191999999999995,
        137: 9.238999999999995,
        138: 9.285999999999996,
        139: 9.332999999999997,
        140: 9.379999999999997,
        141: 9.426999999999998,
        142: 9.473999999999998,
        143: 9.520999999999999,
        144: 9.568,
        145: 9.615,
        146: 9.662,
        147: 9.709000000000001,
        148: 9.756000000000002,
        149: 9.803000000000003,
        150: 9.850000000000003,
        151: 9.897000000000004,
        152: 9.944000000000004,
        153: 9.991000000000005,
        154: 10.038000000000006,
        155: 10.085000000000006,
        156: 10.132000000000007,
        157: 10.179000000000007,
        158: 10.226000000000008,
        159: 10.273000000000009,
        160: 10.32000000000001,
        161: 10.36700000000001,
        162: 10.41400000000001,
        163: 10.461000000000011,
        164: 10.508000000000012,
        165: 10.555000000000012,
        166: 10.602000000000013,
        167: 10.649000000000013,
        168: 10.696000000000014,
        169: 10.743000000000015,
        170: 10.790000000000015,
        171: 10.837000000000016,
        172: 10.884000000000016,
        173: 10.931000000000017,
        174: 10.978000000000018,
        175: 11.025000000000018,
        176: 11.072000000000019,
        177: 11.11900000000002,
        178: 11.16600000000002,
        179: 11.21300000000002,
        180: 11.260000000000021,
      }
      altitud = sunpos.get_az_alt()[0]
      if(altitud < 90):
        altitud = altitud+90
      else:
        altitud = 180-altitud

      servo1.ChangeDutyCycle(anglesMap[altitud])
      time.sleep(0.5)
      servo1.ChangeDutyCycle(0)
      servo1.stop()
      GPIO.cleanup()
      return altitud
