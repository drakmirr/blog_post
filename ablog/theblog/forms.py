from django import forms
from .models import Post, Category
# choices= [ ('coding','coding'), ('sport' ,'sport'), ('entertaiment','entertaiment')]
choices= Category.objects.all().values_list('name','name')

choice_list= []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_teg','author','category','body')

        widgets={
            'title': forms.TextInput(attrs={'class':' form-control', 'placeholder':'This is Title placeholder' }),
            'title_teg': forms.TextInput(attrs={'class': ' form-control'}),
            'author': forms.Select(attrs={'class': ' form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': ' form-control'}),
            'body': forms.Textarea(attrs={'class': ' form-control'})
        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','title_teg')

        widgets={
            'title': forms.TextInput(attrs={'class':' form-control', 'placeholder':'This is Title placeholder' }),
            'title_teg': forms.TextInput(attrs={'class': ' form-control'}),
            #'author': forms.Select(attrs={'class': ' form-control'}),
            'body': forms.Textarea(attrs={'class': ' form-control'})
        }