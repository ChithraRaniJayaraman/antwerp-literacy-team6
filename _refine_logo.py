from PIL import Image, ImageDraw, ImageOps

base_path = "logo for reading literacy.jpeg"
new_photo_path = "reading photo.jpg"
out_path = "antwerpen-literacy-team-logo-final.png"

base = Image.open(base_path).convert("RGBA")
new_photo = Image.open(new_photo_path).convert("RGBA")

# Keep original artwork untouched; only add one extra photo section in the right face.
layer = Image.new("RGBA", base.size, (0, 0, 0, 0))

# Extra section positioned within right-side face, without cropping key original areas.
x1, y1, x2, y2 = 792, 560, 955, 785
w, h = x2 - x1, y2 - y1

fitted = ImageOps.fit(new_photo, (w, h), method=Image.Resampling.LANCZOS)
mask = Image.new("L", (w, h), 0)
draw_mask = ImageDraw.Draw(mask)
draw_mask.rounded_rectangle((0, 0, w, h), radius=16, fill=255)
layer.paste(fitted, (x1, y1), mask)

# Clean border so the new section matches existing collage style.
d = ImageDraw.Draw(layer)
d.rounded_rectangle((x1, y1, x2, y2), radius=16, outline=(255, 255, 255, 240), width=6)

final = Image.alpha_composite(base, layer)
final.convert("RGB").save(out_path, "PNG")
print(f"Saved: {out_path}")
