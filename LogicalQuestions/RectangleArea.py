class RectangleArea:
    def rectangleArea(self, A, B, C, D, E, F, G, H):
        width = 0
        if C > E and A < G:
            left = (max(A, E))
            right = (max(min(C, G), left))
            width = right - left

        height = 0
        if D > F and B < H:
            bottom = (max(B, F))
            top = (max(min(D, H), bottom))
            height = top - bottom

        # area of first rectangle + area of second rectangle - common area
        return (C-A)*(D-B) + (G-E)*(H-F) - (width * height)


object = RectangleArea()
A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2
#print(object.rectangleArea(A, B, C, D, E, F, G, H))
A = -2
B = -2
C = 2
D = 2
E = -4
F = -4
G = -3
H = -3
#print(object.rectangleArea(A, B, C, D, E, F, G, H))
A = -2
B = -2
C = 2
D = 2
E = 1
F = -3
G = 3
H = -1
print(object.rectangleArea(A, B, C, D, E, F, G, H))