# -*- coding: utf-8 -*-
def IntersectingTriangles(rectangle1, rectangle2):
	#rectangle1 = {‘left_x’: 1, ‘bottom_y’: 5, ’width’: 10, ‘height’: 4}
	#rectangle2 = {left_x’: 8 , ‘bottom_y’: 3, ’width’: 4, ‘height’: 6}
	
	#rectanle1
	Height1 = rectangle1['height']
	Width1 = rectangle1['width']
	Point1_1 = (rectangle1['left_x'],rectangle1['bottom_y'])
	print Point1_1
	#Point2_1 = (Point1_1[0] + Width1, Point1_1[1])
	#Point3_1 = (Point1_1[0], Point1_1[1] + Height1)
	Point4_1 = (Point1_1[0] + Width1, Point1_1[1] + Height1)
	

	#Rectangle2
	#Height2 = rectangle2['height']
	#Width2 = rectangle2['width']
	Point1_2 = (rectangle2['left_x'], rectangle2['bottom_y'])
	print Point1_2
	
	#Check if there is a 100% intersection
	if Point1_1 == Point1_2:
	       return 'There is a 100% intersection!'
	
	#Now we have the intersecting rectangle information
	# Intersecting_rectangle points (8,3), (11,9)
	Int_rectangle_Point1 = Point1_2
	Int_rectangle_Point2 = Point4_1
	#calculate a and b to get the height and width of the intersecting rectangle
	a = Int_rectangle_Point2[0] - Int_rectangle_Point1[0]
	b = Int_rectangle_Point2[1] - Int_rectangle_Point1[1]
	
	print a, b
	
	if a <= 0 or b <= 0:
	   return 'There is no intersection'
	else:
           	Intersecting_rectangle = {}
           	Intersecting_rectangle['left_x'] =  Int_rectangle_Point1[0]
           	Intersecting_rectangle['bottom_y'] = Int_rectangle_Point1[1]
           	Intersecting_rectangle['width'] = a
           	Intersecting_rectangle['height'] = b
                return Intersecting_rectangle