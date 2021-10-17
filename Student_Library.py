from tabulate import tabulate
class book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
    def __str__(self):
        return f"{self.name} by {self.author}"

class student:
    def __init__(self,name,Id):
        self.name = name
        self.id = Id
        self.booksBorrowed =[]
    def borrowedBooks(self):
        if self.booksBorrowed.__len__() == 0:
            return "Empty"
        else:
            bookstr = str(self.booksBorrowed[0])
            for i in range(1,self.booksBorrowed.__len__()):
                bookstr = bookstr + "\n" + str(self.booksBorrowed[i])
            return bookstr
                
class Library:
    lt = []
    count =[]
    borrowers = []
    def registerBook(self,name,author,numberOfCopies):
        newBook = book(name,author)
        for i in range(0,self.lt.__len__()):
            if self.lt[i].name.lower() == newBook.name.lower():
                self.count[i] +=int(numberOfCopies)
                return
        self.lt.append(newBook)
        try:
            self.count.append(int(numberOfCopies))
        except Exception:
            print(Exception)
            print("\n")

    def displayBooks(self):
        for i in range(0,self.lt.__len__()):
            if int(self.count[i])>1 :
                print(self.lt[i].name + " by "+self.lt[i].author + " ( "+str(self.count[i])+" copies )")
            else:
                print(self.lt[i].name + " by "+self.lt[i].author + " ( "+str(self.count[i])+" copy )")
        print("\n")
    
    def borrow(self,bookName,studentName,ID):
        index =0
        for i in range(0,self.borrowers.__len__()):
            if self.borrowers[i].id == ID:
                temp = self.borrowers[i]
                index =i
                break
            index = i+1
        if index == self.borrowers.__len__():
            temp = student(studentName,ID)
            self.borrowers.append(temp)
        for j in range(0,temp.booksBorrowed.__len__()):
            if bookName.lower() == temp.booksBorrowed[j].name.lower():
                print("You can't borrow more than one copy of one book\n")
                return
        for i in range(0,self.lt.__len__()):
            if bookName.lower() == self.lt[i].name.lower():
                newBook = book(self.lt[i].name,self.lt[i].author)
                temp.booksBorrowed.append(newBook)
                if self.count[i] == 1:
                    print("You have successfully borrowed "+self.lt[i].name+" by "+self.lt[i].author+"\n")
                    self.lt.pop(i)
                    self.count.pop(i)
                else:
                    self.count[i] -= 1
                    print("You have successfully borrowed "+self.lt[i].name+" by "+self.lt[i].author+"\n")
                return
        print("Either "+bookName+" is currently not available or you may have entered wrong name of book\n")
    
    def displayBorrowers(self):
        l = []
        for i in range(0,self.borrowers.__len__()):
            student = self.borrowers[i]
            l.append([ student.name, student.id, student.borrowedBooks()])
        table = tabulate(l, headers=['Name', 'ID', 'Books'], tablefmt='orgtbl')
        print(table)
        print("\n")

lib = Library()
while(True):
    try:
        option = int(input("Enter 1 to Register book(s), 2 to display books, 3 to borrow book(s), 4 to display borrowers,\n5 to exit: "))
    except Exception:
        print(Exception)
        print("\n")
    if option == 1:
        name = input("Enter name of book: ")
        author = input("Author Name: ")
        numberOfcopies = input("Number of copies: ")
        lib.registerBook(name,author,numberOfcopies)
        print("Registered successfully\n")
    elif option == 2:
        lib.displayBooks()
    elif option == 3:
        studentName = input("Enter student's(borrower) name: ")
        id = int(input("Enter student ID: "))
        bookName = input("Enter book name: ")
        lib.borrow(bookName,studentName,id)
    elif option == 4:
        lib.displayBorrowers()
    elif option == 5:
        exit()
    else: 
        print("Invalid Entry")