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

split_2x2("x1-wood.jpg", ["x1-wood-cat.jpg", "x1-wood-dollhouse.jpg",
                          "x1-wood-mountain.jpg", "x1-wood-relief.jpg"])
split_2x2("x1-acrylic.jpg", ["x1-acrylic-motorcycle.jpg", "x1-acrylic-anderson.jpg",
                             "x1-acrylic-wedding.jpg", "x1-acrylic-earrings.jpg"])
split_2x2("x1-metal.jpg", ["x1-metal-sf-plaque.jpg", "x1-metal-zebra.jpg",
                           "x1-metal-tags.jpg", "x1-metal-mountain.jpg"])
split_2x2("x1-glass.jpg", ["x1-glass-wine.jpg", "x1-glass-award.jpg",
                           "x1-glass-tajmahal.jpg", "x1-glass-cameo.jpg"])

im = Image.open(S / "x1-more-materials.jpg")
w, h = im.size
tw, th = w // 5, h // 2
names = ["x1-mm-leather.jpg", "x1-mm-stone.jpg", "x1-mm-ceramic.jpg",
         "x1-mm-plastic.jpg", "x1-mm-silicone.jpg", "x1-mm-denim.jpg",
         "x1-mm-pearl.jpg", "x1-mm-paper.jpg", "x1-mm-rubber.jpg",
         "x1-mm-pcb.jpg"]
for i, name in enumerate(names):
    col, row = i % 5, i // 5
    im.crop((col * tw, row * th, (col + 1) * tw, (row + 1) * th)).save(S / name, quality=92)
    print(f"{name}: {tw}x{th}")
print("done")
