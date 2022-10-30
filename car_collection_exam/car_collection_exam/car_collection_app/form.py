from django import forms

from car_collection_exam.car_collection_app.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Car.objects.all().delete()
        return self.instance



class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    pass

class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


    def _disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = True


    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

class CarEditForm(CarBaseForm):
    pass



