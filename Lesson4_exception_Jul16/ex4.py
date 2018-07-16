class RelationException(Exception):
    def __init__(self,pa,pb):
        self.pa = pa
        self.pb = pb
    # def __str__(self):
    #     print(self.pa,self.pb)
    #     return 

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}

def check(pa, pb):
    x=pa in relation.keys()
    y=pb in relation.keys()
    
    if relation[pa]!=pb:
        raise RelationException(pa,pb)
    
    elif x==False or y==False:
        raise Exception()
    
    else:
        pass

try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))

except RelationException as e:
    print("No relation found,Are you sure that "+p1+" and "+p2+" are in love with each other?")
    
except Exception as e:
    print("Are you sure that "+p1+" and "+p2+" are in love with each other?")

