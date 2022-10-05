from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


# class PostModelForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['message', 'is_public']

# form = PostModelForm(request.POST)
# if form.is_valid():
#     post = form.save(commit=False)
#     post.author = request.user
#     post.ip = request.META['REMOTE_ADDR']
#     post.save()


# class PostForm(forms.Form):
#     email = forms.EmailField()
#     content = forms.CharField(widget=forms.Textarea)
#     created_at = forms.DateTimeField()
