from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': _('Комментировать')
        }
        widgets = {
            'text': Textarea(attrs={'rows': 4})
        }