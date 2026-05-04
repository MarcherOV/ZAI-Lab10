from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories', verbose_name="Kategoria nadrzędna")
    name = models.CharField(max_length=255, verbose_name="Nazwa")
    is_published = models.BooleanField(default=True, verbose_name="Publikuj")
    order = models.IntegerField(default=0, verbose_name="Kolejność")

    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria")
    order = models.IntegerField(default=0, verbose_name="Kolejność")
    number = models.CharField(max_length=50, verbose_name="Numer")
    title = models.CharField(max_length=255, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena")
    hours = models.IntegerField(verbose_name="Liczba godzin")
    is_published = models.BooleanField(default=True, verbose_name="Publikuj")

    def __str__(self):
        return self.title
    
class Registration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Id szkolenia")
    rodo_consent = models.BooleanField(default=False, verbose_name="Zgoda RODO")
    status = models.CharField(max_length=50, default='Nowa', verbose_name="Status")
    date_registered = models.DateTimeField(auto_now_add=True, verbose_name="Data i godzina rejestracji")
    first_name = models.CharField(max_length=100, verbose_name="Imię")
    last_name = models.CharField(max_length=100, verbose_name="Nazwisko")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course}"

class MessageTemplate(models.Model):
    name = models.CharField(max_length=100)
    content_html = models.TextField()