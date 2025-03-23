v = int(input())  
t = int(input())  

s = v * t

point = (s % 109 + 109) % 109

print(point)
