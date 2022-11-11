from xml.etree import ElementTree

colors = {
    'red': 0,
    'blue': 0,
    'green': 0
}


def add_color(color, deep):
    global colors
    value = colors[color]
    colors[color] = value + deep


def calc_colors(sub_root, deep=1):
    add_color(sub_root.attrib['color'], deep)
    for child in sub_root:
        calc_colors(child, deep + 1)


root = ElementTree.fromstringlist(input())
calc_colors(root)
print(colors['red'], colors['green'], colors['blue'])
