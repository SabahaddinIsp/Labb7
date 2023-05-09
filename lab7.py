import cv2
image = cv2.imread("C:\\Users\\sabah\\Desktop\\ph\\1552568115372.jpg")
blue, green, red = cv2.split(image)
cv2.imshow('Blue Channel', blue)
cv2.imshow('Green Channel', green)
cv2.imshow('Red Channel', red)
cv2.waitKey(0)
green[:] = 0
red[0:255]
blue[0:255]
merged_Image = cv2.merge((blue, green, red))
cv2.imshow('Modified Image', merged_Image)
cv2.waitKey(0)