from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

bx = []


def print_numbers(n=51, f_size=100, border=100, border_n=50, file_name='ix.png'):
    myFont = ImageFont.truetype('Roboto-Regular.ttf', f_size)

    img = Image.new('RGB', (2480, 3508), (255, 255, 255))
    width, height = img.size

    I1 = ImageDraw.Draw(img)

    for i in range(1, n):
        x = 0
        y = 0
        collision = True
        while collision:
            x = random.randint(border, width - border - border_n - f_size)
            y = random.randint(border, height - border - border_n - f_size)

            collision = False
            for p in bx:
                if p[0] - f_size - border_n * 2 < x - border_n < p[2] and p[1] - f_size - border_n * 2 < y - border_n < p[3]:
                    print("Collision: ", i)
                    collision = True
                    break

        I1.text((x, y), str(i), font=myFont, fill=(0, 0, 0))
        bx.append([x - border_n, y - border_n, x + f_size + border_n, y + f_size + border_n, i])

    img.save(file_name)

    for p in bx:
        print(p)


def test_array():
    bx.append([1, 2, 3, 4])
    print(len(bx))
    print(bx[0])


if __name__ == '__main__':
    print_numbers(51, 100, 100, 50, 'i1.png')
    print_numbers(13, 200, 100, 50, 'i2.png')
    # test_array()
