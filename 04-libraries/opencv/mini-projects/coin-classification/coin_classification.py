#!/bin/env python3

import numpy as np
import cv2
from pathlib import Path

"""
Calssifier les pieces de monnais
"""
def av_pix( img, circles, size ):
	av_value = []
	for c in circles[0,:]:
		col = np.mean( img[ c[1]-size:c[1]+size,c[0]-size:c[0]+size ] )
		#print(img[ c[1]-size:c[1]+size,c[0]-size:c[0]+size ] )
		av_value.append(col)
	return av_value
	
def get_radius(circles):
	radius = []
	for c in circles[0,:]:
		radius.append(c[2])
	return radius


PROJECT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = PROJECT_DIR / "assets" / "capstone_coins.png"

img = cv2.imread(str(IMAGE_PATH), cv2.IMREAD_GRAYSCALE)
original_image = cv2.imread(str(IMAGE_PATH), cv2.IMREAD_COLOR)

img = cv2.GaussianBlur(img,(5,5),0)
#cv2.imshow('Detected Coin', original_image)

# Vecteur contenant les les coordonnees d'une des circles dans l'image'
circles = cv2.HoughCircles( img, cv2.HOUGH_GRADIENT,0.9,120,param1=50,param2=27,minRadius=60,maxRadius=120 )
print(circles)

# Dessiner les circles sur l'image d'origine
circles = np.uint16(np.around(circles))
count = 1
for i in circles[0,:]:
	#dessiner le circle exterieur
	cv2.circle(original_image,(i[0],i[1]),i[2],(0,255,0),2)
	#Dessiner le centre du circle
	cv2.circle( original_image,(i[0],i[1]),2,(0,255,0),3 )
	#cv2.putText(original_image,str(count),(i[0],i[1]),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
	count+=1

# Classification en utisant les Rayons et brightness:
  # Les Rayons :
radii = get_radius(circles)
print(f"circles[0,:] = {circles[0,:]}")
print(f"radii = {[int(i) for i in radii]}")

  # Brightness:
bright_values = av_pix(img, circles, 20) 
print(f"\nbright_values = {[ int(i) for i in bright_values ]}")

  # Classification:
values = []
for a,b in zip(bright_values,radii):
	if a > 150 and b > 110:
		values.append(10)
	elif a > 150 and b <= 110:
		values.append(5)
	elif a < 150 and b > 110:
		values.append(2)
	elif a < 150 and b < 110:
		values.append(1)

print(f"values = {values}")
count_2 = 0
for i in circles[0,:]:
	cv2.putText(original_image, str(values[count_2])+'p',(i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0),2)
	count_2+=1
	
#cv2.putText(original_image, 'ESTIMATED TOTAL VALUE: '+str(sum(values))+'p',(200,100]), cv2.FONT_HERSHEY_SIMPLEX, 1.3, 255)
cv2.putText(original_image, 'ESTIMATED TOTAL VALUE: ' + str(sum(values)) + 'p', (200,100), cv2.FONT_HERSHEY_SIMPLEX, 1.3, 255)
cv2.imshow('Detected Coin', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()






























































