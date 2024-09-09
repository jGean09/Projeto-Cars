from django import forms
from cars.models import Brand, car

"""
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        new_car = car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            value=self.cleaned_data['value'],
            photo=self.cleaned_data['photo'],
        )
        new_car.save()
        return new_car

"""

class CarModelForm(forms.ModelForm):
    class Meta:
        model = car
        fields = '__all__'



    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'valor mínimo do carro deve ser de R$ 20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'O carro não é possível cadastrar carro fabricados antes de 1975')
        return factory_year
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            self.add_error('photo','Não pode cadastrar carro sem foto')
        return photo
   
    