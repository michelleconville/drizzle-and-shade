from .models import Faqs
from django import forms


class FaqsForm(forms.ModelForm):
    """
    Display form to the page
    """

    class Meta:
        model = Faqs
        fields = [
            "category",
            "questions",
            "answers",
        ]

        labels = {
            "category": "Select a category",
            "questions": "Add your question",
            "answers": "Add your answer",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Add Placeholder to form fields
        """
        placeholders = {
            'category': 'category',
            'questions': 'questions',
            'answers': 'answers',
        }

        for field in self.fields:
            if field != 'topic':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            # add class to fields
            self.fields[field].widget.attrs['class'] = 'border-blue rounded-0'

            # Set custom IDs for form fields
            if field == 'category':
                self.fields[field].widget.attrs['id'] = 'category-field'
            elif field == 'questions':
                self.fields[field].widget.attrs['id'] = 'questions-field'
            elif field == 'answers':
                self.fields[field].widget.attrs['id'] = 'answers-field'

            # Set aria-labelledby attributes to use the custom IDs
            self.fields[field].widget.attrs['aria-labelledby'] = (
                f"{self.fields[field].widget.attrs['id']}-label"
                )
