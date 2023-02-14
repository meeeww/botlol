import cv2 as cv
import numpy as np

screen = cv.imread('imagenes/ingame/screen.png', cv.IMREAD_ANYCOLOR)
xubi = cv.imread('imagenes/ingame/xubi.png', cv.IMREAD_ANYCOLOR)

result = cv.matchTemplate(screen, xubi, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)


print("best match: " + str(max_loc))
print("best match" + str(max_val))

threshold = 0.8
if max_val >= threshold:
    print("found")

    needle_w = xubi.shape[1]
    needle_h = xubi.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(screen, top_left, bottom_right,
                        color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow("Result", screen)
    cv.waitKey()
else:
    print("holi")