from PIL import Image

a = Image.open("C:/Users/meng/Desktop/1989.png")
a = a.convert("RGBA")
a.putalpha(255)
a.save("C:/Users/meng/Desktop/1989.png")
