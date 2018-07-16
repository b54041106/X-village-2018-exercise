
class Shape:
    def set_edge(self, n):
        self.edge = n
    def display(self):
        n=self.edge+1
        for i in range(1, n):
            for j in range(1, n):
                if j<=i:
                   print("*",end=" "),
            print("\n")
x = Shape()
x.set_edge(5)
x.display()