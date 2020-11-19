import random
value=random.randint(1,13)
import winsound
duration_ms=1000

if value==1:
    winsound.Beep(523, duration_ms)
elif value==2:
    winsound.Beep(554, duration_ms)
elif value==3:
    winsound.Beep(587, duration_ms)
elif value==4:
    winsound.Beep(622, duration_ms)
elif value==5:
    winsound.Beep(659, duration_ms)
elif value==6:
    winsound.Beep(698, duration_ms)
elif value==7:
    winsound.Beep(740, duration_ms)
elif value==8:
    winsound.Beep(784, duration_ms)
elif value==9:
    winsound.Beep(830, duration_ms)
elif value==10:
    winsound.Beep(880, duration_ms)
elif value==11:
    winsound.Beep(932, duration_ms)
elif value == 12:
    winsound.Beep(988, duration_ms)
else:
    winsound.Beep(1047, duration_ms)