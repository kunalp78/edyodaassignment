import os
from time import sleep
class Menu:
    def __init__(self):
        self.no_of_seats = 0
        self.no_of_booked_user = 0
        self.seat_row = []
        self.seat_col = []
#         self.booked = False
#         self.book_row = 0
#         self.book_col = 0
        self.UserData = dict([])
    def set_cinema_hall(self,row,col):
        self.row = row
        self.col = col
        l=[]
        for i in range(self.row):
            for j in range(self.col):
                self.seat_col.append('S')
#             print(self.seat_col,end='\n')
            l= self.seat_col
            self.seat_col = []
            self.seat_row.append(l)

    def no_of_purchased_tickets(self,seat_row):
        count=0
#         print(seat_row)
        for i in seat_row:
            for j in i:
                if j == 'B':
                    count+=1
        return count
    def percentage_of_booked_tickets(self):
        return (self.no_of_purchased_tickets(self.seat_row)/(self.col*self.row))*100
    def total_income(self):
        
        if self.col*self.row <= 60:
            return self.no_of_purchased_tickets(self.seat_row) * 10
        elif self.row%2==0:
            return self.no_of_purchased_tickets(self.seat_row[:self.row//2+1])*10 + self.no_of_purchased_tickets(self.seat_row[self.row//2:])*8
        else:
            return self.no_of_purchased_tickets(self.seat_row[:self.row//2])*10 + self.no_of_purchased_tickets(self.seat_row[self.row//2:])*8
        

    def show_seats(self):
        for i,val in enumerate(self.seat_row):
            if i == 0:
                print(' ',end=' ')
                for j in range(self.col):
                    print(j+1,end=" ")
                print(end="\n")
                print(i+1,end=' ')
                for j,val1 in enumerate(val):
                    print(val1,end=" ")
            else:
                print(i+1,end=' ')
                for j,val1 in enumerate(val):
                    if j == 0:
                        print(val1, end=' ')
                    else: 
                        print(val1,end=' ')
            print(end='\n')
            
class User(Menu):
    def __init__(self,name,gender,age,phn):
        super().__init__()
        self.name = name
        self.gender = gender
        self.age = age
        self.phn = phn
        self.profile_dict = dict({'name':self.name,'gender':self.gender,'age':self.age,'phone':self.phn,'booked':False,'book_row':0,'book_col':0}) 
        
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
      # for windows platfrom
        _ = os.system('cls')
def buy_ticket(name,gender,age,phn,book_col,book_row,booked=False):       
#         self.name,self.gender,self.age,self.phn = name,gender,age,phn
    A.profile_dict['name'] = name
    A.profile_dict['gender'] = gender
    A.profile_dict['age'] = age
    A.profile_dict['phone'] = phn
    A.profile_dict['booked'] = booked
    A.profile_dict['book_row'] = book_row
    A.profile_dict['book_col'] = book_col  
    
    if True not in ['S' in i for i in startmenu.seat_row]:
        print('All tickets are already booked is already booked PLS ')
    elif True not in ['S' in i for i in startmenu.seat_row[A.profile_dict['book_row']-1]]:
        print('Choose another row ')
    elif startmenu.seat_row[A.profile_dict['book_row']-1][A.profile_dict['book_col']-1] == 'B':
        print('Chooses another seat')
    else:
        startmenu.seat_row[A.profile_dict['book_row']-1][A.profile_dict['book_col']-1] = 'B'
        A.profile_dict['booked'] = 'True' 
        

def current_income(row,col,book_row,book_col):
    if row*col <= 60:
        return str(10) + '$ /-'
    elif row*col>60 and row%2==0 and startmenu.seat_row.index(startmenu.seat_row[A.profile_dict['book_row']-1])<= row//2:
#         print(startmenu.seat_row.index(startmenu.seat_row[A.profile_dict['book_row']])+1)
        return str(10) + '$ /-'
    elif row*col>60 and row%2==0 and startmenu.seat_row.index(startmenu.seat_row[A.profile_dict['book_row']-1])> row//2:
        return str(8) + '$ /-'
    elif row*col>60 and row%2!=0 and startmenu.seat_row.index(startmenu.seat_row[A.profile_dict['book_row']-1])< row//2:
        return str(10) + '$ /-'
    elif row*col>60 and row%2!=0 and startmenu.seat_row.index(startmenu.seat_row[A.profile_dict['book_row']-1])>= row//2:
        return str(8) + '$ /-'

def Set_user_by_row_col(row,col):
    startmenu.UserData[row]={}
    startmenu.UserData[row][col] = A.profile_dict

def Get_user_by_row_col(row,col,row1,col1):
    print('Name {}'.format(startmenu.UserData[row1][col1]['name']))
    print('Gender {}'.format(startmenu.UserData[row1][col1]['gender']))
    print('Age {}'.format(startmenu.UserData[row1][col1]['age']))
    print('Ticket Price {}'.format(current_income(row,col,row1,col1)))
    print('Phone {}'.format(startmenu.UserData[row1][col1]['phone']))
    
    
def Statistics(row,col,book_row,book_col):
    print('1> Number of Purchased Ticket {}'.format(startmenu.no_of_purchased_tickets(startmenu.seat_row)))
    print('2> Percentage of Ticket booked {}'.format(startmenu.percentage_of_booked_tickets()))
    print('3> Current Income {}'.format(current_income(row,col,book_row,book_col)))
    print('4> Total Income {}'.format(startmenu.total_income()))

if __name__ == "__main__":
    choice = input('!!Want to create the cinema!!(Y/N)')
    while(choice=='Y'):    
        print('Create the cinema Hall')
        row = int(input("Enter row"))
        col = int(input("Enter Column"))
        startmenu = Menu()
        startmenu.set_cinema_hall(row,col) 
        screen_clear()
        choice1=''
        while(choice1!=0 or choice1!=0):
            print('1> Show the Seats')
            print('2> Buy ticket')
            print('3> Statictics')
            print('4> Show booked Tickets User Info')
            print('0> Exit')
            choice1 = int(input("Enter your choice here : "))
            if choice1 == 1:
                print('Here')
                startmenu.show_seats()
                choice = input("Want to Enter more...Press 0 to exit")
            elif choice1 == 2:    
                name = input("Enter Name")
                age = int(input("Enter Age"))
                gender = input('Enter Gender')
                phn = input("Enter Phone number")
                book_col,book_row = int(input("Enter the col from top")),int(input("Enter the row from Top"))
                A = User(name,gender,age,phn)
                buy_ticket(name,gender,age,phn,book_col,book_row)
                Set_user_by_row_col(book_row,book_col)
                print('Success!!')
                # 5 sec halt for message to show
                sleep(2)
                screen_clear()
                choice = input("Want to Enter more...Press 0 to exit")
            elif choice1 == 3:
                Statistics(row,col,book_row,book_col)
                choice = input("Want to Enter more")
            elif choice1 == 4:
                row1 = int(input("Enter the row you want to search: "))
                col1 = int(input("Enter the col you want to search"))
                Get_user_by_row_col(row,col,row1,col1)
                # 5 sec halt for message to show
                sleep(2)
                screen_clear()
                choice = input("Want to Enter more(Y/N)...Press 0 to exit")
            elif choice1 == 0:
                break
        choice = input("Want to Create new cinema Hall(Y/N)")
