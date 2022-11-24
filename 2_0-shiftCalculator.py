
import math
minStartLat = 45.01059
minStartLon = 7.606612 

dy = dx = 100/1000 #squares of 200 meters width and hight
r_earth = 6378.137 #km
pi = math.pi

new_latitude  = minStartLat  + (dy / r_earth) * (180 / pi)
new_longitude = minStartLon + (dx / r_earth) * (180 / pi) / math.cos(minStartLat * pi/180)

shiftLat = new_latitude - minStartLat
shiftLon = new_longitude - minStartLon