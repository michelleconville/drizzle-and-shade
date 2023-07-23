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
