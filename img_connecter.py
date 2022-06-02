from PIL import Image


class ImgConnecter:
    """Класс, который соединяет картинки"""

    def connect_imgs(self, name_1: str, name_2: str) -> Image:
        """Соединяет 2 картинки размером 640x480 горизонтально
        Сохряняет в файл 'info.png'"""
        img = Image.new('RGB', (640 * 2, 480))
        img1 = Image.open(name_1)
        img2 = Image.open(name_2)
        img.paste(img1, (0, 0))
        img.paste(img2, (640, 0))

        img.save("info.png")
