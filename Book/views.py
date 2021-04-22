from django.shortcuts import render,redirect
from django.http import HttpResponse
from Book.models import Book
# Create your views here.

#html- hyper text markup language
#http
# port = 8000

 #view-function based view(fbv) #http request  #user defined
def homepage(request):
    # all_books = Book.objects.all().filter(is_deleted='N')
    all_books= Book.active_objects.all()  # thru custom nanager
    #print(all_books)
    return render (request, template_name='home.html',context={"books":all_books})

def save_book(request):
    #print("In Save Book")
    print(request.POST)
    b_name = request.POST.get("name") 
    b_author = request.POST.get("author") 
    b_qty = request.POST.get("qty") 
    b_price= request.POST.get("price") 
    b_is_published = request.POST.get("is_published")

    if b_is_published == "on":
        flag = True
    else:
        flag = False
    if request.POST.get("id"):
        book_obj = Book.objects.get(id=request.POST.get("id"))
        book_obj.name = b_name
        book_obj.author = b_author
        book_obj.qty = b_qty
        book_obj.price = b_price
        book_obj.is_published = flag
        book_obj.save()
        return redirect("Welcome") 

    else:
        b = Book(name=b_name,author=b_author,qty=b_qty,price=b_price,is_published=flag)
        b.save()    
        return redirect("Welcome") 

def edit_book(request,id):   #pk---primary key
    try:
        #print ("AA")
        book_obj = Book.objects.get(id=id)
    except Book.DoesNotExist:
        msg =f"No book found for id:{id}" 
        return HttpResponse(msg)
    #all_books= Book.objects.all().filter(is_deleted='N')
    all_books= Book.active_objects.all()
    return render (request, template_name='home.html',context={"book":book_obj,"books":all_books})

def delete_book(request,pk):   #pk---primary key
    book_obj = Book.objects.get(id=pk)
    # book_obj.delete()
    book_obj.is_deleted = "Y"
    book_obj.save()
    return redirect("Welcome") 
    
def hard_delete_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.delete()
    return redirect('welcome')

def restore_book(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = 'N'
    book_obj.save()
    return redirect('welcome')

def show_deleted_data(request):
    all_deleted_books = Book.inactive_objects.all()  # thru custom manager
    return render(request, template_name='home.html', context={"books": all_deleted_books})

def delete_all(request):   #pk---primary key
    #book_obj = Book.objects.get(id=pk)
    # book_obj.delete()
    all_books = Book.active_objects.all()
    for book in all_books:
        book.obj.is_deleted = "Y"
        book.obj.save()
    return redirect('Welcome') 

def restore_all(request):
    all_books = Book.inactive_objects.all()
    for book in all_books:
        #book_obj = Book.objects.get(id=id)
        book.obj.is_deleted = 'N'
        book.obj.save()
    return redirect('welcome')