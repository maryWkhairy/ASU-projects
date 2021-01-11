from django.db import models

# Create your models here.


class Image(models.Model):

    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to="pictures", blank=True, null=True)
    image2 = models.ImageField(upload_to="pictures", blank=True, null=True)


#CATEGORY_CHOICES= [
 #   ('chairs', 'Chairs'),
  #  ('armchairs', 'Armchairs'),
   # ('chaiselongues', 'Chaiselongues'),
    #('sofas', 'Sofas'),
    #('wardrobes', 'Wardrobes'),
    #('beds', 'Beds'),
    #('shelving units', 'Shelving Units'),
    #('tables', 'Tables'),
    #]


class Additem(models.Model):
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to="dashboard", blank=True, null=True)
    description = models.CharField(max_length=2000)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()
    category = models.CharField(max_length=70,
    choices=[
      ('chairs', 'Chairs'),
      ('armchairs', 'Armchairs'),
      ('chaiselongues', 'Chaiselongues'),
      ('sofas', 'Sofas'),
      ('wardrobes', 'Wardrobes'),
      ('beds', 'Beds'),
      ('shelving units', 'Shelving Units'),
      ('tables', 'Tables'),
     ]
    )
    #username = models.ForeignKey(Register, related_name='username', on_delete=models.CASCADE)


    #def __str__(self):
     #   return self.title

    #@property
    #def imageURL(self):
     #   try:
      #      url=self.image.url
       # except:
        #    url = ''
        #return url

# Create your models here.
