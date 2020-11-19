import cv2
import random
import winsound
duration_ms=1000

img01 = cv2.imread('sound=color_01.JPG')
img03 = cv2.imread('sound=color_03.JPG')
img05 = cv2.imread('sound=color_05.JPG')
img07 = cv2.imread('sound=color_07.JPG')
img09 = cv2.imread('sound=color_09.JPG')
img11 = cv2.imread('sound=color_11.JPG')
img13 = cv2.imread('sound=color_13.JPG')
img15 = cv2.imread('sound=color_15.JPG')
img17 = cv2.imread('sound=color_17.JPG')
img19 = cv2.imread('sound=color_19.JPG')
img21 = cv2.imread('sound=color_21.JPG')
img23 = cv2.imread('sound=color_23.JPG')
img25 = cv2.imread('sound=color_25.JPG')

cv2.imshow('sound=color.JPG', img01)
cv2.moveWindow('sound=color.JPG', 100, 40)
cv2.waitKey(1)
winsound.Beep(523, duration_ms)
cv2.waitKey(250)

while True:
    value = random.randint(1, 13)
    if value == 1:
        cv2.imshow('sound=color.JPG', img01)
        cv2.waitKey(1)
        winsound.Beep(523, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 2:
        cv2.imshow('sound=color.JPG', img03)
        cv2.waitKey(1)
        winsound.Beep(554, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 3:
        cv2.imshow('sound=color.JPG', img05)
        cv2.waitKey(1)
        winsound.Beep(587, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 4:
        cv2.imshow('sound=color.JPG', img07)
        cv2.waitKey(1)
        winsound.Beep(622, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 5:
        cv2.imshow('sound=color.JPG', img09)
        cv2.waitKey(1)
        winsound.Beep(659, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 6:
        cv2.imshow('sound=color.JPG', img11)
        cv2.waitKey(1)
        winsound.Beep(698, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 7:
        cv2.imshow('sound=color.JPG', img13)
        cv2.waitKey(1)
        winsound.Beep(740, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 8:
        cv2.imshow('sound=color.JPG', img15)
        cv2.waitKey(1)
        winsound.Beep(784, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 9:
        cv2.imshow('sound=color.JPG', img17)
        cv2.waitKey(1)
        winsound.Beep(831, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 10:
        cv2.imshow('sound=color.JPG', img19)
        cv2.waitKey(1)
        winsound.Beep(880, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 11:
        cv2.imshow('sound=color.JPG', img21)
        cv2.waitKey(1)
        winsound.Beep(932, duration_ms)
        if cv2.waitKey(250) > 0:
            cv2.destroyAllWindows()
            break

    elif value == 12:
        cv2.imshow('sound=color.JPG', img23)
        cv2.waitKey(1)
        winsound.Beep(988, duration_ms)
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