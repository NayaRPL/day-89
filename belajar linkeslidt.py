# cara membuta linkedlist kita terlabih dahulu membuat class node
class node:
    def __init__(self,element,next=None):
        self.element=element
        self.next=next
# mendefenisikan atribut atribut
class linkedlist:
    def __init__ (self):
        self.head=None # digunakan untuk menunjuk simpul pertama dalam list
        self.tail=None # di gunakan untuk simpul terakhir dalam tuple
        self.size=0 # du gunakan menyatakan jumlah simpul terakhir list 
# memeriksa ukuran list
    def isempty(self):
        return self.size == 0 # di dunakan untuk mengecek ukuran list
     
    def addfirst(self, element):
        newnode=node(element,self.head)# menambah simpul pada posisi pertama 
        self.head= newnode # head menuju simpul baru 
        self.size+=1 # menambah ukuran list 
        if self.tail == None:  # jika list hanya satu simpul
            self.tail=self.head
    def getfirst(self):
        if self.isempty():
            return None
        else:
            return self.head.element
    def removefirst(self):
        if not self.isempty():
            temp= self.head
            self.head=self.head.next
            self.size -=1 # mengurangi ukuran list
            del temp
            
    

    
    
        
    
      
        
        