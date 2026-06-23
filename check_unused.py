import os, re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

used = re.findall(r'src="([^"]+)"', html)
used_images = [os.path.basename(u) for u in used if 'images/' in u]

all_images = os.listdir('images')

unused = set(all_images) - set(used_images)

with open('unused.txt', 'w', encoding='utf-8') as f:
    for img in sorted(unused):
        f.write(img + "\n")
        
print("Unused files mapped")
