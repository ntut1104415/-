import streamlit as st
import cv2
import numpy as np

if __name__ == __main__:
st.image(os.path.join('CX9.jpg'), use_column_width  = True)
img = cv2.imread("CX9.jpg")

cv2.nameWindow("CX9",cv2.WINDOW_NORMAL)
cv2.imshow("CX9",img)
cv2.waitKey(0)
cv2.destroyALLWindows()
