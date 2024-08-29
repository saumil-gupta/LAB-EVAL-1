# SAUMIL GUPTA 22103179 B6 LAB EVAL-1
class shopping:
    #CONSTRUCTOR
    def __init__(self):
        self.items = []
    
    #ADD AN ITEM TO THE LIST
    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            print(item," IS ADDED TO THE SHOPPING LIST")
        else:
            print(item," IS ALREADY IN THE SHOPPING LIST")
    
    #REMOVE AN ITEM FROM THE LIST
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(item," IS REMOVED FROM THE SHOPPING LIST")
        else:
            print(item," IS NOT THERE IN THE SHOPPING LIST")
    
    #SEARCH AN ITEM FROM THE LIST --> BUILT IN FUNCTION
    def search_item(self, item):
        if item in self.items:
            print(item," IS PRESENT IN THE SHOPPING LIST")
            return True
        else:
            print(item," IS NOT PRESENT IN THE SHOPPING LIST")
            return False
    
    #DISPLAY THE SHOPPING LIST
    def display_list(self):
        if self.items:
            print("SHOPPING LIST : ")
            for i in self.items:
                print(i)
        else:
            print("THE SHOPPING LIST IS EMPTY")
    
    # BINARY SEARCH
    def searching(self, item):
        flag=0
        for i in self.items:
            if i==item:
                flag=1
                print(item," IS PRESENT IN THE SHOPPING LIST")
                return True
                break
        if flag==0:
            print(item," IS NOT PRESENT IN THE SHOPPING LIST")
            return False

    #DISPLAY SHOPPING LIST IN REVERSED ORDER
    def reverse(self):
        reversed=[]
        flag=0
        if self.items:
            for i in self.items:
                reversed.append(i)
                flag=1
        else:
            print("THE SHOPPING LIST IS EMPTY")
        
        if flag==1:
            print("REVERSED SHOPPING LIST : ")
            for i in range(0,len(reversed)):
                print(reversed[len(reversed)-1-i])


    
s = shopping()
#ADD ITEM
cc=input("ENTER ITEM TO ADD : ")
s.add_item(cc)
dd=input("ENTER ITEM TO ADD : ")
s.add_item(dd)
s.display_list()    #DISPLAY SHOPPING LIST

#REMOVE ITEM
aa=input("ENTER ITEM TO REMOVE : ")
s.remove_item(aa)
s.display_list()

#SEARCH ITEM
"""
a=s.search_item("MILK")
print(a)
b=s.search_item("MEAT")
print(b)
"""

a=input("ENTER ITEM TO SEARCH USING BINARY SEARCH: ")
b=s.searching(a)
print(b)
s.reverse()         #DISPLAY SHOPPING LIST IN REVERSE ORDER