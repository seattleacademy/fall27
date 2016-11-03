from sense_hat import SenseHat
sense = SenseHat()
X = [0, 255, 0]  # Green
O = [255, 255, 255]  # White

down_arrow = [
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
O, X, X, X, X, X, X, O,
O, O, X, X, X, X, O, O,
O, O, O, X, X, O, O, O
]

sense.set_pixels(down_arrow)