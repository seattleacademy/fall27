from sense_hat import SenseHat
sense = SenseHat()
X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

up_arrow = [
O, O, O, X, X, O, O, O,
O, O, X, X, X, X, O, O,
O, X, X, X, X, X, X, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O
]

sense.set_pixels(up_arrow)