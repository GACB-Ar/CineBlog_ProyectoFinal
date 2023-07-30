from django import forms
from .models import Article

class Create_new_article(forms.ModelForm):
    image = forms.ImageField(label='image', required=False)
    
    class Meta:
        model = Article
        fields = [ "title", "description", "tags", "content", "image"]