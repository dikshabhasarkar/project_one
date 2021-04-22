from django.db import models

# Create your models here.

#app name- Book, model name - Book
class BookActiveManager(models.Manager): #custom manager
    def get_queryset(self):
        return super(BookActiveManager, self).get_queryset().filter(is_deleted='N') 

class BookInactiveManager(models.Manager):  # Custom Manager
    def get_queryset(self):
        return super(BookInactiveManager, self).get_queryset().filter(is_deleted='Y')   

class Book(models.Model):
    #id is created by django by default - 
    # columns will generate for below fields 
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    is_deleted = models.CharField(max_length=1, default="N")
    
    # columns will not generate for below fields 
    active_objects = BookActiveManager()
    inactive_objects = BookInactiveManager()
    objects = models.Manager() 

    def __str__(self):
        return f"{self.id}----{self.author}"

    class Meta:
        db_table = "bookinfo"

# appname= modelname= small case
#create table book_book (id int unique Auto_increment,name varchar(100),author(100),qty int, price float)

Hi Hello!!!


Good Night
