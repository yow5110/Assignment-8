# Problem 1

def midpoint(n):
    # n is the number of increments between a and b
    n = int(n)
    import numpy as np
    a = 0
    b = np.pi
    dx=(b-a)/n
    
    # a simple for loop that performs the integration
    integral = 0
    for i in range(n):
        integral = integral + np.sin((i+0.5)*dx)*dx    

    print(integral) 

    
    
def midpoint_vec(n):
    n = int(n)
    import numpy as np
    a = 0
    b = np.pi
    dx=(b-a)/n
    
    # Write a vectorized version of the same integration here
    # without using any loop or list comprehension.
    

    
