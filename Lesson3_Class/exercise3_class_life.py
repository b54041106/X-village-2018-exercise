class Map:
    map= []
    def set_map(self,n):
        self.boarder = n
        for i in range(n):
            row=[]
            for j in range(n):
                row.append('*')
            self.map.append(row)

    def set_pattern(self,p):
        n=int(self.boarder/2)-1
        if p==1: #建置Gilder圖案 
            for j in range(n,n+3):
                self.map[n][j]="0"
            for i in range(n,n+2):
                self.map[i][n]="0"
            self.map[n+2][n+1]="0"

    def set_display(self):
        for i in range(self.boarder):
            for j in range(self.boarder):
                print(self.map[i][j],end=" ")
            print('\n')
                        
my_map = Map() #建立 instance object
my_map.set_map(5) # n=5, 代表地圖為 5x5 大小
my_map.set_pattern(1)
my_map.set_display() #


class Map1:
    map= []
    boarder=1
    def set_map(self,number):
        self.boarder = number
        for i in range(number):
            row=[]
            for j in range(number):
                row.append('*')
            self.map.append(row)
    def set_pattern(self,p):
        n=int(self.boarder/2)-1
        a =[0,1,2,3,7]
        if p==1:
            for i in a:
                self.map[n+int(i/3)][n+int(i%3)]="0"
    def set_display(self):
        for i in range(self.boarder):
            for j in range(self.boarder):
                print(self.map[i][j],end=" ")
            print('\n')
my_map = Map1() #建立 instance object
my_map.set_map(5) # n=5, 代表地圖為 5x5 大小
my_map.set_pattern(1)
my_map.set_display() #

# class Map:
#     map = []
#     def set_map(self,n):
#         self.boarder = n
#     def set_display(self):
#         n = self.boarder+1
#         for i in range(1,n):
#             for j in range(1,n):
#                 print("*",end=" "),
#             print("\n")

# my_map = Map() #建立 instance object
# my_map.set_map(5) # n=5, 代表地圖為 5x5 大小
# my_map.set_display()

