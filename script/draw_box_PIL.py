# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


def draw(filename, result):
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)

    for r in result:
        # center point is (A, B) 
        A, B, w, h = r
        a = A - (h / 2)
        c = A + (h / 2)
        b = B - (w / 2)
        d = B + (w / 2)

        print(a, b, c, d)

        draw.line([(a, b), (a, d)], fill="red")
        draw.line([(a, d), (c, d)], fill="red")
        draw.line([(c, d), (c, b)], fill="red")
        draw.line([(c, b), (a, b)], fill="red")
        # break

    plt.imshow(img)
    plt.show()
    img.save("../readme_images/点选2.jpg")


def main():
    filename = "../readme_images/点选1.jpg"
    inflection = [
        ('word', 0.9977150559425354, (211.69094848632812, 96.27708435058594, 34.80897521972656, 32.95333480834961)),
        ('word', 0.9969455599784851, (63.864295959472656, 118.94916534423828, 39.05336380004883, 26.741514205932617)),
        ('word', 0.9953688383102417, (76.27388763427734, 47.417152404785156, 32.8591194152832, 34.27583694458008)),
        ('word', 0.9929825067520142, (155.02427673339844, 49.5576286315918, 36.80773162841797, 33.70331954956055)),
        ('word', 0.9849220514297485, (133.80186462402344, 102.25910186767578, 36.13843536376953, 36.53313064575195))]

    result = []

    for inf in inflection:
        inf = inf[2]
        result.append(inf)
    print(result)
    draw(filename, result)


if __name__ == '__main__':
    main()
