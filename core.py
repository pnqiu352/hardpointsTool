# core.py
import math
import re

UNIT = {
    "mm": 1.0,
    "m": 1000.0
}

def parse_point(text, unit="mm"):
    nums = re.findall(r"[-+]?\d*\.?\d+", text)
    if len(nums) != 3:
        raise ValueError("Invalid 3D point")
    return tuple(to_mm(float(n), unit) for n in nums)

def distance(p1, p2):
    return math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2    )

def to_mm(value, unit):
    return value * UNIT[unit]       

def format_hp(name, point_mm, unit="mm", dp=3):
    scale = UNIT[unit]
    x = round(point_mm[0] / scale, dp)
    y = round(point_mm[1] / scale, dp)
    z = round(point_mm[2] / scale, dp)
    return f"{name} = ({x}, {y}, {z}) {unit}"
