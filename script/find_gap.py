#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
寻找缺口的脚本，有一定失败几率
"""
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


def get_position(image):
    image = image.resize((280, 158))  # 修改为页面上的尺寸页面上的尺寸
    image = image.convert('L')
    yuzhi = 150
    yuzhi2 = 40
    ll = 10
    for i in range(55, image.size[0] - 20):  # 260   range(55, 264)
        for j in range(0, image.size[1] - 20):  # 160   range(0, 140)
            flag = True
            # 如果两列像素附近的色差大于40且像素点灰度大于150，说明有可能是缺口的地方
            # 如果两列像素附近色差小于40说明不是缺口的地方
            for l in range(0, ll):  # range(0, 10)
                # print((i, j), (i + 1, j + l))
                # print(image.getpixel((i, j)), image.getpixel((i + 1, j + l)))
                pixel = image.getpixel((i, j)) - image.getpixel((i + 1, j + l))
                if pixel < yuzhi2:
                    flag = False
                # pixel = image.getpixel((i - l, j))
                # if pixel<yuzhi:
                #     flag=False
            # 如果像素灰度值小于150，说明不是缺口的地方
            for l in range(0, ll):
                # print((i, j + l))
                pixel = image.getpixel((i, j + l))
                if pixel < yuzhi:
                    flag = False

            if flag:
                # cropedimage = image.crop((i, j, i + 30, j + 30))
                return i - 7


def draw(img, result):
    draw = ImageDraw.Draw(img)
    a, b, c, d = result
    print(a, b, c, d)

    draw.line([(a, b), (a, d)], fill="red")
    draw.line([(a, d), (c, d)], fill="red")
    draw.line([(c, d), (c, b)], fill="red")
    draw.line([(c, b), (a, b)], fill="red")

    plt.imshow(img)
    plt.show()
    img.save("../readme_images/缺口2.jpg")


def main():
    img = Image.open("../readme_images/缺口1.jpg")
    r = get_position(img)
    print(r)
    result = [r, 0, r+8*2, 158]
    draw(img, result)


if __name__ == '__main__':
    main()