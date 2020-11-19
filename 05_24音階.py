import cv2
import random
import winsound
duration_ms=1000

img01 = cv2.imread('sound=color_01.JPG')
img02 = cv2.imread('sound=color_02.JPG')
img03 = cv2.imread('sound=color_03.JPG')
img04 = cv2.imread('sound=color_04.JPG')
img05 = cv2.imread('sound=color_05.JPG')
img06 = cv2.imread('sound=color_06.JPG')
img07 = cv2.imread('sound=color_07.JPG')
img08 = cv2.imread('sound=color_08.JPG')
img09 = cv2.imread('sound=color_09.JPG')
img10 = cv2.imread('sound=color_10.JPG')
img11 = cv2.imread('sound=color_11.JPG')
img12 = cv2.imread('sound=color_12.JPG')
img13 = cv2.imread('sound=color_13.JPG')
img14 = cv2.imread('sound=color_14.JPG')
img15 = cv2.imread('sound=color_15.JPG')
img16 = cv2.imread('sound=color_16.JPG')
img17 = cv2.imread('sound=color_17.JPG')
img18 = cv2.imread('sound=color_18.JPG')
img19 = cv2.imread('sound=color_19.JPG')
img20 = cv2.imread('sound=color_20.JPG')
img21 = cv2.imread('sound=color_21.JPG')
img22 = cv2.imread('sound=color_22.JPG')
img23 = cv2.imread('sound=color_23.JPG')
img24 = cv2.imread('sound=color_24.JPG')
img25 = cv2.imread('sound=color_25.JPG')

cv2.imshow('sound=color.JPG', img01)
cv2.moveWindow('sound=color.JPG', 100, 40)
cv2.waitKey(1)
winsound.Beep(523, duration_ms)
cv2.waitKey(250)

while True:
    value = random.randint(1, 25)
    if value == 1:
        cv2.imshow('sound=color.JPG', img01)
        cv2.waitKey(1)
        winsound.Beep(523, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 2:
        cv2.imshow('sound=color.JPG', img02)
        cv2.waitKey(1)
        winsound.Beep(538, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 3:
        cv2.imshow('sound=color.JPG', img03)
        cv2.waitKey(1)
        winsound.Beep(554, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 4:
        cv2.imshow('sound=color.JPG', img04)
        cv2.waitKey(1)
        winsound.Beep(570, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 5:
        cv2.imshow('sound=color.JPG', img05)
        cv2.waitKey(1)
        winsound.Beep(587, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 6:
        cv2.imshow('sound=color.JPG', img06)
        cv2.waitKey(1)
        winsound.Beep(604, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 7:
        cv2.imshow('sound=color.JPG', img07)
        cv2.waitKey(1)
        winsound.Beep(622, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 8:
        cv2.imshow('sound=color.JPG', img08)
        cv2.waitKey(1)
        winsound.Beep(640, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 9:
        cv2.imshow('sound=color.JPG', img09)
        cv2.waitKey(1)
        winsound.Beep(659, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 10:
        cv2.imshow('sound=color.JPG', img10)
        cv2.waitKey(1)
        winsound.Beep(678, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 11:
        cv2.imshow('sound=color.JPG', img11)
        cv2.waitKey(1)
        winsound.Beep(698, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 12:
        cv2.imshow('sound=color.JPG', img12)
        cv2.waitKey(1)
        winsound.Beep(719, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 13:
        cv2.imshow('sound=color.JPG', img13)
        cv2.waitKey(1)
        winsound.Beep(740, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 14:
        cv2.imshow('sound=color.JPG', img14)
        cv2.waitKey(1)
        winsound.Beep(762, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 15:
        cv2.imshow('sound=color.JPG', img15)
        cv2.waitKey(1)
        winsound.Beep(784, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 16:
        cv2.imshow('sound=color.JPG', img16)
        cv2.waitKey(1)
        winsound.Beep(807, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 17:
        cv2.imshow('sound=color.JPG', img17)
        cv2.waitKey(1)
        winsound.Beep(831, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 18:
        cv2.imshow('sound=color.JPG', img18)
        cv2.waitKey(1)
        winsound.Beep(855, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 19:
        cv2.imshow('sound=color.JPG', img19)
        cv2.waitKey(1)
        winsound.Beep(880, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 20:
        cv2.imshow('sound=color.JPG', img20)
        cv2.waitKey(1)
        winsound.Beep(906, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 21:
        cv2.imshow('sound=color.JPG', img21)
        cv2.waitKey(1)
        winsound.Beep(932, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 22:
        cv2.imshow('sound=color.JPG', img22)
        cv2.waitKey(1)
        winsound.Beep(960, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 23:
        cv2.imshow('sound=color.JPG', img23)
        cv2.waitKey(1)
        winsound.Beep(988, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 24:
        cv2.imshow('sound=color.JPG', img24)
        cv2.waitKey(1)
        winsound.Beep(1012, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    else:
        cv2.imshow('sound=color.JPG', img25)
        cv2.waitKey(1)
        winsound.Beep(1047, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break