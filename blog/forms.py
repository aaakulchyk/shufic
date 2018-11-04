from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }
        labels = {
            'text': _('Комментировать'),
        }