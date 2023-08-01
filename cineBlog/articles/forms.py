from django import forms
from .models import Article, Comments

class Create_new_article(forms.ModelForm):
    image = forms.ImageField(label='image', required=False)
    
    class Meta:
        model = Article
        fields = [ "title", "description", "tags", "content", "image"]

class Edit_existing_article(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description", "tags", "content", "image"]
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields =['content']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.author = user.username