#!/usr/bin/env python3
"""Split the xTool X1 material panels into individual sample tiles.
All four material panels share one template: a 'Recommended Lasers' text
panel on the left (~0-900px) and a 2x2 photo grid on the right (~905-1960px).
The More Materials panel is a clean 5x2 grid of 10 tiles.
Outputs land in the same samples dir as .jpg files.
"""
from PIL import Image
import pathlib

S = pathlib.Path("/home/hatch/workspace/jakinscraft/assets/samples")

def crop(src, box, dst):
    im = Image.open(S / src)
    im.crop(box).save(S / dst, quality=92)
    print(f"{dst}: {Image.open(S / dst).size}")

def split_2x2(src, names):
    im = Image.open(S / src)
    w, h = im.size
    x0, xmid, x1 = 905, 1432, w
    ymid = h // 2
    boxes = [(x0, 0, xmid, ymid), (xmid, 0, x1, ymid),
             (x0, ymid, xmid, h), (xmid, ymid, x1, h)]
    for box, name in zip(boxes, names):
        im.crop(box).save(S / name, quality=92)
        print(f"{name}: {box}")

split_2x2("wood.jpg", ["wood-cat.jpg", "wood-dollhouse.jpg",
                          "wood-mountain.jpg", "wood-relief.jpg"])
split_2x2("acrylic.jpg", ["acrylic-motorcycle.jpg", "acrylic-anderson.jpg",
                             "acrylic-wedding.jpg", "acrylic-earrings.jpg"])
split_2x2("metal.jpg", ["metal-sf-plaque.jpg", "metal-zebra.jpg",
                           "metal-tags.jpg", "metal-mountain.jpg"])
split_2x2("glass.jpg", ["glass-wine.jpg", "glass-award.jpg",
                           "glass-tajmahal.jpg", "glass-cameo.jpg"])

im = Image.open(S / "more-materials.jpg")
w, h = im.size
tw, th = w // 5, h // 2
names = ["mm-leather.jpg", "mm-stone.jpg", "mm-ceramic.jpg",
         "mm-plastic.jpg", "mm-silicone.jpg", "mm-denim.jpg",
         "mm-pearl.jpg", "mm-paper.jpg", "mm-rubber.jpg",
         "mm-pcb.jpg"]
for i, name in enumerate(names):
    col, row = i % 5, i // 5
    im.crop((col * tw, row * th, (col + 1) * tw, (row + 1) * th)).save(S / name, quality=92)
    print(f"{name}: {tw}x{th}")
print("done")
