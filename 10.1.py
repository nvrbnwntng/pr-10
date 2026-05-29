from PIL import Image

kartinka = "птичка.jpg"
novi = "птичка_cropped.jpg"

right = 90
left = 100
lower = 500
upper = 300

with Image.open(kartinka) as img:
    cropped_img = img.crop((right, left, lower, upper))
    cropped_img.save(novi)
    print(f"Изображение успешно обрезано и сохранено как '{novi}'")
    print(f"Исходный размер: {img.size}")
    print(f"Новый размер: {cropped_img.size}")
