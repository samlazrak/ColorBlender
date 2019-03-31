from sys import platform as sys_pf

if sys_pf == "darwin":
  import matplotlib

  matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

data = np.random.rand(10, 10) * 20

# create discrete colormap
cmap = colors.ListedColormap(
  [
    (255, 255, 0),
    (368, 288, 26),
    (330, 255, 12),
    (318, 255, 127),
    (264, 260, 71),
    (255, 279, 41),
    (261, 331, 93),
    (341, 382, 23),
    (295, 278, 6),
    (371, 313, 40),
    (324, 280, 18),
    (278, 290, 29),
    (227, 66, 52),
    (340, 99, 78),
    (302, 66, 64),
    (290, 66, 179),
    (236, 71, 123),
    (227, 90, 93),
    (233, 142, 145),
    (313, 193, 75),
    (267, 89, 58),
    (343, 124, 92),
    (296, 91, 70),
    (250, 101, 81),
    (150, 0, 24),
    (263, 33, 50),
    (225, 0, 36),
    (213, 0, 151),
    (159, 5, 95),
    (150, 24, 65),
    (156, 76, 117),
    (236, 127, 47),
    (190, 23, 30),
    (266, 58, 64),
    (219, 25, 42),
    (173, 35, 53),
    (127, 0, 255),
    (240, 33, 281),
    (202, 0, 267),
    (190, 0, 382),
    (136, 5, 326),
    (127, 24, 296),
    (133, 76, 348),
    (213, 127, 278),
    (167, 23, 261),
    (243, 58, 295),
    (196, 25, 273),
    (150, 35, 284),
    (18, 10, 143),
    (131, 43, 169),
    (93, 10, 155),
    (81, 10, 270),
    (27, 15, 214),
    (18, 34, 184),
    (24, 86, 236),
    (104, 137, 166),
    (58, 33, 149),
    (134, 68, 183),
    (87, 35, 161),
    (41, 45, 172),
    (0, 49, 83),
    (113, 82, 109),
    (75, 49, 95),
    (63, 49, 210),
    (9, 54, 154),
    (0, 73, 124),
    (6, 125, 176),
    (86, 176, 106),
    (40, 72, 89),
    (116, 107, 123),
    (69, 74, 101),
    (23, 84, 112),
    (13, 152, 186),
    (126, 185, 212),
    (88, 152, 198),
    (76, 152, 313),
    (22, 157, 257),
    (13, 176, 227),
    (19, 228, 279),
    (99, 279, 209),
    (53, 175, 192),
    (129, 210, 226),
    (82, 177, 204),
    (36, 187, 215),
    (173, 255, 47),
    (286, 288, 73),
    (248, 255, 59),
    (236, 255, 174),
    (182, 260, 118),
    (173, 279, 88),
    (179, 331, 140),
    (259, 382, 70),
    (213, 278, 53),
    (289, 313, 87),
    (242, 280, 65),
    (196, 290, 76),
    (80, 46.7, 13.3),
    (193, 79.7, 39.3),
    (155, 46.7, 25.3),
    (143, 46.7, 140.3),
    (89, 51.7, 84.3),
    (80, 70.7, 54.3),
    (86, 122.7, 106.3),
    (166, 173.7, 36.3),
    (120, 69.7, 19.3),
    (196, 104.7, 53.3),
    (149, 71.7, 31.3),
    (103, 81.7, 42.3),
    (233, 116, 81),
    (346, 149, 107),
    (308, 116, 93),
    (296, 116, 208),
    (242, 121, 152),
    (233, 140, 122),
    (239, 192, 174),
    (319, 243, 104),
    (273, 139, 87),
    (349, 174, 121),
    (302, 141, 99),
    (256, 151, 110),
    (138, 51, 36),
    (251, 84, 62),
    (213, 51, 48),
    (201, 51, 163),
    (147, 56, 107),
    (138, 75, 77),
    (144, 127, 129),
    (224, 178, 59),
    (178, 74, 42),
    (254, 109, 76),
    (207, 76, 54),
    (161, 86, 65),
    (46, 71, 59),
    (159, 104, 85),
    (121, 71, 71),
    (109, 71, 186),
    (55, 76, 130),
    (46, 95, 100),
    (52, 147, 152),
    (132, 198, 82),
    (86, 94, 65),
    (162, 129, 99),
    (115, 96, 77),
    (69, 106, 88),
  ]
)


def find_colour(_val):
  # Colour value constants
  _colours = {
    "color1": [255, 255, 0],
    "color2": [368, 288, 26],
    "color3": [330, 255, 12],
    "color4": [318, 255, 127],
    "color5": [264, 260, 71],
    "color6": [255, 279, 41],
    "color7": [261, 331, 93],
    "color8": [341, 382, 23],
    "color9": [295, 278, 6],
    "color10": [371, 313, 40],
    "color11": [324, 280, 18],
    "color12": [278, 290, 29],
    "color13": [227, 66, 52],
    "color14": [340, 99, 78],
    "color15": [302, 66, 64],
    "color16": [290, 66, 179],
    "color17": [236, 71, 123],
    "color18": [227, 90, 93],
    "color19": [233, 142, 145],
    "color20": [313, 193, 75],
    "color21": [267, 89, 58],
    "color22": [343, 124, 92],
    "color23": [296, 91, 70],
    "color24": [250, 101, 81],
    "color25": [150, 0, 24],
    "color26": [263, 33, 50],
    "color27": [225, 0, 36],
    "color28": [213, 0, 151],
    "color29": [159, 5, 95],
    "color30": [150, 24, 65],
    "color31": [156, 76, 117],
    "color32": [236, 127, 47],
    "color33": [190, 23, 30],
    "color34": [266, 58, 64],
    "color35": [219, 25, 42],
    "color36": [173, 35, 53],
    "color37": [127, 0, 255],
    "color38": [240, 33, 281],
    "color39": [202, 0, 267],
    "color40": [190, 0, 382],
    "color41": [136, 5, 326],
    "color42": [127, 24, 296],
    "color43": [133, 76, 348],
    "color44": [213, 127, 278],
    "color45": [167, 23, 261],
    "color46": [243, 58, 295],
    "color47": [196, 25, 273],
    "color48": [150, 35, 284],
    "color49": [18, 10, 143],
    "color50": [131, 43, 169],
    "color51": [93, 10, 155],
    "color52": [81, 10, 270],
    "color53": [27, 15, 214],
    "color54": [18, 34, 184],
    "color55": [24, 86, 236],
    "color56": [104, 137, 166],
    "color57": [58, 33, 149],
    "color58": [134, 68, 183],
    "color59": [87, 35, 161],
    "color60": [41, 45, 172],
    "color61": [0, 49, 83],
    "color62": [113, 82, 109],
    "color63": [75, 49, 95],
    "color64": [63, 49, 210],
    "color65": [9, 54, 154],
    "color66": [0, 73, 124],
    "color67": [6, 125, 176],
    "color68": [86, 176, 106],
    "color69": [40, 72, 89],
    "color70": [116, 107, 123],
    "color71": [69, 74, 101],
    "color72": [23, 84, 112],
    "color73": [13, 152, 186],
    "color74": [126, 185, 212],
    "color75": [88, 152, 198],
    "color76": [76, 152, 313],
    "color77": [22, 157, 257],
    "color78": [13, 176, 227],
    "color79": [19, 228, 279],
    "color80": [99, 279, 209],
    "color81": [53, 175, 192],
    "color82": [129, 210, 226],
    "color83": [82, 177, 204],
    "color84": [36, 187, 215],
    "color85": [173, 255, 47],
    "color86": [286, 288, 73],
    "color87": [248, 255, 59],
    "color88": [236, 255, 174],
    "color89": [182, 260, 118],
    "color90": [173, 279, 88],
    "color91": [179, 331, 140],
    "color92": [259, 382, 70],
    "color93": [213, 278, 53],
    "color94": [289, 313, 87],
    "color95": [242, 280, 65],
    "color96": [196, 290, 76],
    "color97": [80, 46.7, 13.3],
    "color98": [193, 79.7, 39.3],
    "color99": [155, 46.7, 25.3],
    "color100": [143, 46.7, 140.3],
    "color101": [89, 51.7, 84.3],
    "color102": [80, 70.7, 54.3],
    "color103": [86, 122.7, 106.3],
    "color104": [166, 173.7, 36.3],
    "color105": [120, 69.7, 19.3],
    "color106": [196, 104.7, 53.3],
    "color107": [149, 71.7, 31.3],
    "color108": [103, 81.7, 42.3],
    "color109": [233, 116, 81],
    "color110": [346, 149, 107],
    "color111": [308, 116, 93],
    "color112": [296, 116, 208],
    "color113": [242, 121, 152],
    "color114": [233, 140, 122],
    "color115": [239, 192, 174],
    "color116": [319, 243, 104],
    "color117": [273, 139, 87],
    "color118": [349, 174, 121],
    "color119": [302, 141, 99],
    "color120": [256, 151, 110],
    "color121": [138, 51, 36],
    "color122": [251, 84, 62],
    "color123": [213, 51, 48],
    "color124": [201, 51, 163],
    "color125": [147, 56, 107],
    "color126": [138, 75, 77],
    "color127": [144, 127, 129],
    "color128": [224, 178, 59],
    "color129": [178, 74, 42],
    "color130": [254, 109, 76],
    "color131": [207, 76, 54],
    "color132": [161, 86, 65],
    "color133": [46, 71, 59],
    "color134": [159, 104, 85],
    "color135": [121, 71, 71],
    "color136": [109, 71, 186],
    "color137": [55, 76, 130],
    "color138": [46, 95, 100],
    "color139": [52, 147, 152],
    "color140": [132, 198, 82],
    "color141": [86, 94, 65],
    "color142": [162, 129, 99],
    "color143": [115, 96, 77],
    "color144": [69, 106, 88],
  }

  # Map the value to a colour
  _colour = [0, 0, 0]
  if _val > 30:
    _colour = _colours["red"]
  elif _val > 20:
    _colour = _colours["color"]
  elif _val > 10:
    _colour = _colours["green"]
  elif _val > 0:
    _colour = _colours["yellow"]

  return tuple(_colour)


bounds = [0, 10, 20]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines
ax.grid(which="major", axis="both", linestyle="-", color="k", linewidth=2)
ax.set_xticks(np.arange(-0.5, 10, 1))
ax.set_yticks(np.arange(-0.5, 10, 1))

plt.show()