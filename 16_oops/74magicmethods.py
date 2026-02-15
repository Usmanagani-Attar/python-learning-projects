class book:
    def __init__(self,tittle,author,num_pages):
        self.tittle=tittle
        self.author=author
        self.num_pages=num_pages

    def __str__(self):
        return f"{self.tittle} by {self.author}"

    def __eq__(self, value):
        return self.tittle==value.tittle and self.author==value.author
    
    def __lt__(self,value):
        return self.num_pages < value.num_pages
    
    def __gt__(self,value):
        return self.num_pages > value.num_pages
    
    def __add__(self,value):
        return f"{self.num_pages + value.num_pages} pages"
    
    def __contains__(self,key):
        return key in self.tittle or key in self.author 
    
    def __getitem__(self,key):
        if key =="tittle":
            return self.tittle
        elif key =="author":
            return self.author
        elif key == "num_pages":
            return self.num_pages     
        else:
            return f"Key {key} was not found"


book1 =book("The physics","H.c verma",540)
book2 =book("The spr","santu",245)
book3 =book("The chemistry","jeevit",172)

print(book1)
print(book2)
print(book3)

print()
print(book1==book2)
print(book1==book3)
print(book3==book2)
print(book1==book1)
print(book2==book2)
print(book3==book3)
print()


print()
print(book1['tittle'])
print(book1 < book3)
print(book3 < book2)
print(book1 < book1)
print()


print()
print(book3 > book2)
print(book1 > book2)
print(book1 > book3)
print(book1 > book1)
print()


print()
print(book1 + book2)
print(book1 + book3)
print(book3 + book2)
print(book1 + book1)
print()


print()
print("The pysics" in book1)
print("The pysics" in book2)
print("The spr" in book2)
print("The spr" in book3)
print("The chemistry in book2 " in book2)
print("The chemistry" in book3)
print()


print(book1["audio"])
print(book1["santu"])

print(book1["Pm"])