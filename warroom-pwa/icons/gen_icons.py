from PIL import Image, ImageDraw, ImageFont
import os

for size in [192, 512]:
    img = Image.new('RGBA', (size, size), (19, 17, 15, 255))
    draw = ImageDraw.Draw(img)
    
    # Dark gradient-ish background circle
    cx, cy = size//2, size//2
    r = int(size * 0.42)
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(26, 23, 20, 255), outline=(42, 37, 32, 255), width=max(1, size//128))
    
    # Inner accent ring
    r2 = int(size * 0.35)
    draw.ellipse([cx-r2, cy-r2, cx+r2, cy+r2], outline=(232, 115, 74, 180), width=max(2, size//64))
    
    # "戰" character approximation — just use a bold shape
    # Draw a stylized "H" for Howling
    bar_w = int(size * 0.06)
    bar_h = int(size * 0.30)
    gap = int(size * 0.14)
    top = cy - bar_h // 2
    
    # Left bar
    draw.rectangle([cx - gap - bar_w//2, top, cx - gap + bar_w//2, top + bar_h], fill=(232, 220, 200, 255))
    # Right bar
    draw.rectangle([cx + gap - bar_w//2, top, cx + gap + bar_w//2, top + bar_h], fill=(232, 220, 200, 255))
    # Cross bar
    draw.rectangle([cx - gap - bar_w//2, cy - bar_w//2, cx + gap + bar_w//2, cy + bar_w//2], fill=(232, 115, 74, 255))
    
    img.save(f'/home/claude/warroom-pwa/icons/icon-{size}.png')
    print(f'Generated {size}x{size}')

