from fileinput import filename
from turtle import width
import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)
f = cv2.VideoWriter_fourcc(*"XVID")
print("Enter filename:")
filename=input()
print("Enter FPS:")
fps=int(input())
output = cv2.VideoWriter(filename+".mp4", f, fps, dim)
now_start_time = time.time()
print("Enter duration:")
dur=int(input())
dur = dur+4
end_time = now_start_time + dur

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break
output.release()
print("Done Recording")
