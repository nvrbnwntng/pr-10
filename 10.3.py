from PIL import Image, ImageDraw, ImageFont

cards = {
    "день туалета": "туалет.jpg",
    "день дедлайна": "дедлайн.jpg",
    "день рождения": "др.jpg",
    "день выгорания": "выгорание.jpg",
}

holiday = input("Праздник: ").lower()
if holiday not in cards: exit("Нет такой открытки")

name = input("Имя: ")
img = Image.open(cards[holiday])
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("arialbd.ttf", 40)

text = f"{name}, поздравляю!"

x = img.width // 2
y = img.height - 75

draw.text((x, y), text, font=font, fill=(255,0,0), anchor="mm")

img.save(f"{name}_открытка.png")
img.show()
