from django import forms
from djrichtextfield.widgets import RichTextWidget
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    description = forms.CharField(
            label='Description',
            required=False, widget=RichTextWidget
            )
    image = forms.ImageField(
            label='Image', required=False, widget=CustomClearableFileInput
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-blue rounded-0'


class CategoryForm(forms.ModelForm):
    """ Category form"""
    class Meta:
        """category model fields"""
        model = Category
        fields = '__all__'
