
import cv2
import numpy as np

def extract_candles_from_image(image_file):
    # ⚠️ Placeholder: এখানে OpenCV দিয়ে candlestick detect করতে হবে
    # এখন কিছু ডামি candle data রিটার্ন করতেছি
    return [
        {'color': 'green', 'height': 40, 'wick': 10},
        {'color': 'red', 'height': 30, 'wick': 12},
        {'color': 'green', 'height': 45, 'wick': 5},
        {'color': 'green', 'height': 50, 'wick': 3},
        {'color': 'red', 'height': 28, 'wick': 7},
    ]
