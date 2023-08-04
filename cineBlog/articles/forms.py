from django import forms
from .models import Article, Comments

class Create_new_article(forms.ModelForm):
    image = forms.ImageField(label='image', required=False)

    class Meta:
        model = Article
        fields = [ "title", "description", "tags", "content", "image", "video_url"]

class Edit_existing_article(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description", "tags", "content", "image", "video_url"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']

    def init(self, args, **kwargs):
        user = kwargs.pop('user', None)
        super(CommentForm, self).init(args, **kwargs)
        if user:
            self.instance.comment_ownership = user

class Edit_existing_comment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']