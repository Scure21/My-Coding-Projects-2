def answer(vertices):
    '''
    Function that calculate the integral points of a triangle
    '''
    # Pick's Theorem  A = i + b/2 -1,  A : Area of the Polygon
    #                                  i : interior points
    #                                  b : boundary points
    # Triangle's area given 3 coordinate points M,N,O: Area = abs(Mx(Ny-Oy) + Nx(Oy-My) + Ox(My-Ny) / 2) 
    
    #Vertices
    M = vertices[0]
    N = vertices[1]
    O = vertices[2]
    
    #Calculate the area of the triangle
    A = triangleArea(M,N,O)
    
    #Calculate the # of boundary points
    B = boundaryPoint(M,N) + boundaryPoint(M,O) + boundaryPoint(N,O) + 3
    
    #Using Pick's theorem calculate the interior points of the triangle
    return (A - B/2 + 1)
    
    
    
def triangleArea(M,N,O):
    ''' Triangle's area given 3 coordinate points M=(Mx,My),N=(Nx,Ny),O=(Ox,Oy): Area = abs(Mx(Ny-Oy) + Nx(Oy-My) + Ox(My-Ny) / 2) 
    '''
    return abs(M[0]*(N[1] - O[1]) + N[0]*(O[1] - M[1]) + O[0]*(M[1] - N[1])) * 1/2
   
   
def boundaryPoint(pointA, pointB):
    '''
    Function to know if there is a boundary point between two vertex
    '''
    if pointA[0] == pointB[0]:
        return abs(pointA[1] - pointB[1]) - 1
    if pointA[1] == pointB[1]:
        return abs(pointA[0] - pointB[0]) - 1
    return gcd(abs(pointA[0] - pointB[0]), abs(pointA[1] - pointB[1])) - 1
    
def gcd(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b==0:
        return a
    return gcd(b,a%b)
    
    