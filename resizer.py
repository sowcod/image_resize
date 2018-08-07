#-*- coding: utf-8 -*-

from PIL import Image

def resize_full(image:Image, w:int, h:int):
    if image.width / image.height > w / h:
        # 横がはみ出る場合、横幅を基準にスケール設定
        scale = w / image.width
    else:
        scale = h / image.height

    new_width = int(image.width * scale)
    new_height = int(image.height * scale)
    return image.resize((new_width, new_height), resample = Image.LANCZOS)

def resize_overflow(image:Image, w:int, h:int):
    if image.width / image.height > w / h:
        # 横がはみ出る場合、縦幅を基準にスケール設定
        scale = h / image.height
    else:
        scale = w / image.width

    new_width = int(image.width * scale)
    new_height = int(image.height * scale)
    box_width = w / scale
    box_height = h / scale
    box_x = (image.width - box_width) / 2
    box_y = (image.height - box_height) / 2
    box = (int(box_x), int(box_y), int(box_x + box_width), int(box_y + box_height))
    return image.resize((w, h), resample = Image.LANCZOS, box = box)

if __name__ == '__main__':
    org_image = Image.open('org.png')

    resize_full(org_image, 50, 50).save('clip.png')
    resize_overflow(org_image, 50, 50).save('overflow.png')
