# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:33:37 2019

@author: BHASKAR NEOGI
"""
                 # Level-? *
                 
while(True) :
    
    p = '''     1. Square
     2. Rectangle
     3. Circle '''
    print(p)
    t = int(input("Enter The Option Number : "))
    
    # Unit Solution : 
    u = input("Enter The Unit [none for default] : ")
    y = 'unit'
    if (u=='none') :
        y == 'unit'
        
    else :
        y = u
        
## Shape Choice : 
        
          # Square : 
    if (t==1) :
        
        class Shape(object) :
            
            def __init__(self) :
                pass
            def area(self) :
                return 0
            
        class Square(Shape) :
            
            def __init__(self,x) :
                Shape.__init__(self)
                self.length = x
                
            def area(self) :
                return self.length*self.length
            
        aSquare = Square(int(input("Enter The length of Square : ")))
        print("Area of Square Is : ",aSquare.area(),y,"square")
        
           # Rectangle : 
    elif (t==2) :
        
        class Rectangle(object) :
            
            def __init__(self,l,w) :                
                self.length = l
                self.width = w
                
            def area2(self) :
                return self.length*self.width
            
        l = int(input("Enter The Length : "))  
        w = int(input("Enter The Width : "))  
        bRectangle = Rectangle(l,w)
        print("Area of Rectangle Is : ",bRectangle.area2(),y,"square")
        
            # Circle : 
    elif (t==3) :
        
        class Circle(object) :
            
            def __init__(self,r) :        
                self.radius = r
                
            def area3(self) :                 
                return self.radius**2*(22/7)
            
        cCircle = Circle(int(input("Enter The Radius  : ")))
        print("Area Of Circle Is : ",cCircle.area3(),y,"square")
    else :
        print("What The Fuck Are You Writing !!")
        
    # Exit Condition : 
    c = int(input("Press 1 to Continue & 0 to Exit : "))
    if c==0 :
        
        break