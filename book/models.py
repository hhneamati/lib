from django.db import models

from phone_field import PhoneField




class Genre(models.Model):
    name = models.CharField(max_length = 200 ,help_text = "ژانر کتاب را وارد کنید",verbose_name='ژانر') 

    def __str__(self):
        return self.name



class Author(models.Model):
    first_name = models.CharField(max_length=20 , verbose_name='نام')
    last_name = models.CharField(max_length=40 ,verbose_name='نام خانوادگی')
    date_of_birth = models.DateField(null=True ,blank=True, verbose_name='تاریخ تولد')
    date_of_death = models.DateField(null=True , blank=True , verbose_name='تاریخ وفات')
    nick_name = models.CharField(max_length=20 , null=True , blank=True , verbose_name='تخلص' )

    class Meta:
        ordering =["last_name" , "first_name"]

    def __str__(self):
        return '{} {}'.format(self.last_name , self.first_name)
  



class Book(models.Model):
    title = models.CharField(max_length=200 ,verbose_name='عنوان')
    summary = models.TextField(max_length=500 , verbose_name='خلاصه ')
    pages= models.IntegerField()
    year = models.DateField(auto_now=False , auto_now_add=False)

    isbn = models.CharField(
        max_length=13 ,
        null=True ,
        blank=True ,
        help_text='مراجعه شود به اینجا http://www.isbn.ir/Forms/faq.aspx' ,
        verbose_name='شابک'
        )
    genre = models.ManyToManyField(Genre , verbose_name='ژانر')
    author = models.ManyToManyField(
        Author ,
        related_name="books",
        verbose_name='نویسنده'
         )
    publisher = models.ForeignKey(
        'Publisher' ,
        on_delete= models.SET_NULL ,
        related_name="books",
        null=True,
        verbose_name='ناشر'
        )

    img = models.ImageField( 
        upload_to='%Y/%m/%d/', 
        height_field=None, 
        width_field=None, 
        max_length=None ,
        null=True,
        blank=True,
        )
    def __str__(self):
        return self.title
    
    

      



class Publisher(models.Model):
    name = models.CharField(max_length=60 , verbose_name='نام انشارات')
    phone = PhoneField(blank=True, help_text='پیش شماره و شماره تلفن' , verbose_name='تلقن')
    address =models.TextField(max_length=100 , blank=True , verbose_name='آدرس')

    def __str__(self):
        return self.name

