from PIL import Image

cards = {
    "день туалета": "туалет.jpg",
    "день дедлайна": "дедлайн.jpg",
    "день рождения": "др.jpg",
    "день выгорания": "выгорание.jpg",
}

holiday = input("К какому празднику нужна открытка? ").strip().lower()

if holiday in cards:
    img = Image.open(cards[holiday])
    img.show()
    print(f"Открытка к {holiday} открыта!")
elif holiday not in cards:
    print(f"Ошибка: файл {cards[holiday]} не найден")
else:
    print(f"Извините, открытки к {holiday} нет в списке")
    print(f"Доступные праздники: {', '.join(cards.keys())}")
