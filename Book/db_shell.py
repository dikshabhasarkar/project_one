from Book.models  import Book

# to run python file in dbshell or django shell
#exec(open('myscript.py').read()) ## command to execute 
#exec(open('F:\\python practice\\Django\\Library\Book\\db_shell.py').read())

## ORM queries
#all data
# all_data = Book.objects.all()
# print(all_data)
# print("-" * 50)

# #single data
# sid=6
# b2 = Book.objects.get(id=sid)
# print(b2)
# print("-" * 50)

# #create data or record
# b3 = Book.objects.create(name="oracle",author="A bnm",qty=10,price=200)
# print(b3.id)
# print("-" * 50)

# #update data
# sid = 7
# b4 = Book.objects.get(id=sid)
# b4.name ="try"
# b4.author="pop"
# b4.qyt= 20
# b4.save()
# print("-" * 50)

# #delete data
# sid = 6
# b5 = Book.objects.get(id=sid)
# b5.delete()

# all_data = Book.objects.all()
# print(all_data)
# for book in all_data:
    #print(book)
    # print("-------- Details for Id number: ",book.id ,"-------")
    # print("Book Name: ",book.name)
    # print("Book authour: ",book.author)
    # print("Book Quantity: ",book.qty)
    # print("Book per price: ",book.price)
# -----details for id number----
# Book name:-
# author name:-
# qty:-
# price per book:-
# -----details for id number----

#for updating and deleting records
# all_data = Book.objects.all()
# print(all_data)
# for book in all_data:
#     book.qty = 15
#     book.save()
#     #book.delete

# all_data = Book.objects.all()
# for i in all_data:
#     print(i.__dict__)

# all_data = Book.objects.all().values("id","name","qty")
# print(list(all_data))
# for i in all_data:
#     #print(i.__dict__)
#     print(i)

# all_data = Book.objects.values_list()
# print(all_data)

# all_data = Book.objects.values_list()
# #print(all_data)
# for i in all_data:
#     print(i[0])

# #create data or record
# b3 = Book.objects.create(name="java",author="A",qty=10,price=200)
# print(b3.id)

# import random
# for  i in range (1,10):
#     b = Book(name=(chr(random.randint(65, 90)))*5 ,author="A" ,qty=random.randint(20, 50) ,price=random.randint(200,700))
#     b.save()

# for greter than 
# books = Book.objects.filter(id__gt=15)
# for i in books:
#     print(i.__dict__)

#for greterthan equalto
# books = Book.objects.filter(id__gte=15)
# for i in books:
#     print(i.__dict__)

#less than
# books = Book.objects.filter(id__lt=15)
# for i in books:
#     print(i.__dict__)

#for lessthan equalto
# books = Book.objects.filter(id__lte=15)
# for i in books:
#     print(i.__dict__)

# books = Book.objects.filter(id__lte=15).values("id","name")
# for i in books:
#     print(i)

# books = Book.objects.filter(name__startswith='V').values("id","name")
# for i in books:
#     print(i)

#for case incensitive
# books = Book.objects.filter(name__istartswith='V').values("id","name")
# for i in books:
#     print(i)

# b = Book.objects.all().order_by("name")  #accending
# print(b)

# b = Book.objects.all().order_by("-name")  # decending
# print(b) 

# b = Book.objects.all().count() ##count data
# print(b)

# b = Book.objects.all()[0:5]  ##from 0 to 5
# print(b)

# l = [i for i in range(1,16)]
# book = Book.objects.filter(id__in=l)
# print(book)

# l = [ i for i in range(12,20)]
# book = Book.objects.filter(id__in=l)
# print(book)

# books = Book.objects.filter(id__lte=15).values("id","name")
# for i in books:
#     print(i)

# l = [i for i in range(12,20)]   ####ntgeting id
# # books = Book.objects.filter(id__in=l)
# # print(books)

# books = Book.objects.exclude(id__in=l)
# print(books)

# sid = 17
# b5 = Book.objects.get(id=17)
# b5.delete()

# Book.objects.bulk_create([
# Book(name="java1",author="A ",qty=10,price=200),
# Book(name="java2",author="B",qty=12,price=200),
# Book(name="java3",author="C",qty=15,price=200),
# Book(name="java4",author="D",qty=19,price=200),
# ])

# l = [i for i in range(5,10)]
# books = Book.objects.filter(id__in=l)
# print(books)