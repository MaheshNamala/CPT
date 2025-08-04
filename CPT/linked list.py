class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None

    def insert_begining(self,data):
        k=node(data)
        k.next=self.head
        self.head=k

    def insert_position(self,pos,data):
        k=node(data)
        temp=self.head
        i=0
        while i<pos-1:
            temp=temp.next
            i+=1
        k.next=temp.next
        temp.next=k


    def insert_ending(self,data):
        k=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=k

    def display(self):
        while self.head:
            print(self.head.data,end=" --> ")
            self.head=self.head.next
l=sll()
n1=node(10)
l.head=n1
n2=node(20)
n1.next=n2
n3=node(30)
n2.next=n3
n4=node(40)
n3.next=n4
l.insert_begining(5)
l.insert_position(2,15)
l.insert_ending(50)
l.insert_ending(60)
l.display()