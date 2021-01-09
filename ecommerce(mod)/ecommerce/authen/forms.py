from django import forms
from .models import Image,Additem
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields =('image','image2','title')

#CATEGORY_CHOICES= [
 #   ('chairs', 'Chairs'),
  #  ('armchairs', 'Armchairs'),
   # ('chaiselongues', 'Chaiselongues'),
   # ('sofas', 'Sofas'),
    #('wardrobes', 'Wardrobes'),
    #('beds', 'Beds'),
    #('shelving units', 'Shelving Units'),
    #('tables', 'Tables'),
    #]

#class AdditemForm(forms.Form):
 #   user = forms.CharField(max_length=100)
  #  image = forms.ImageField(upload_to="dashboard", blank=True, null=True)
   # description = forms.CharField(max_length=2000)
   # price = forms.FloatField()
   # date = forms.DateTimeField(auto_now_add=True)
   # count = forms.IntegerField()
   # category = forms.CharField(label='Select Category', widget=forms.Select(choices=CATEGORY_CHOICES))


class AdditemForm(forms.ModelForm):
    class Meta:
        model = Additem
        fields = ('image', 'description', 'price', 'count', 'category')



#class LoginForm(forms.ModelForm):
 #   class Meta:
  #      model=Login
   #     fields = ['email','pwd']


