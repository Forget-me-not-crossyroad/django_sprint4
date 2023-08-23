from django import forms

from django.utils.translation import ugettext_lazy as _

from .models import Comment, Post, User


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        labels = {
            'name': _('Пользователь'),
        }
        help_texts = {
            'name': _('Форма для ввода данных пользователя'),
        }


class PostEditForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ("author", "created_at")
        widgets = {
            "text": forms.Textarea({"rows": "5"}),
            "pub_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
        labels = {
            'name': _('Пост'),
        }
        help_texts = {
            'name': _('Форма для ввода данных поста'),
        }


class CommentEditForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {
            "text": forms.Textarea({"rows": "5"})
        }
        labels = {
            'name': _('Комментарий'),
        }
        help_texts = {
            'name': _('Форма для ввода текста комментария'),
        }
