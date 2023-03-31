import cv2

img = cv2.imread("E:\BT PHYTON CODING\C2\PROJECT 116\solar-system.jpg")

#sun
cv2.putText (img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

#mercury
cv2.putText (img,
            "Mercury",
            (115,235),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

#venus
cv2.putText (img,
            "Venus",
            (200,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

#earth
cv2.putText (img,
            "Earth",
            (290,255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

#mars
cv2.putText (img,
            "Mars",
            (380,245),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

#jupiter
cv2.putText (img,
            "Jupiter",
            (545,370),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

#saturn
cv2.putText (img,
            "Saturn",
            (750,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

#uranus
cv2.putText (img,
            "Uranus",
            (970,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

#neptnue
cv2.putText (img,
            "Neptune",
            (1130,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.imshow("",img)
cv2.waitKey(0)
 