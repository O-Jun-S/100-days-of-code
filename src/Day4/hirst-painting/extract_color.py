from typing import Any, Tuple

import colorgram as cg
colors = cg.extract("spot.jpg", 30)


def color2tuple(color_obj):
    """Convert color object to tuple."""
    if not isinstance(color_obj, cg.Color):
        raise TypeError
    rgb = color_obj.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    color_tuple = (r, g, b)
    return color_tuple


color_tuple_list = []
for color in colors:
    color_t = color2tuple(color)
    color_tuple_list.append(color_t)
print(color_tuple_list)
