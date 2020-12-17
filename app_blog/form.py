from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=66,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "aplaceholder": "Nombre..."
        })
    )
    body = forms.CharField(widget=forms.Textarea(
    attrs={
        "class": "form-control",
        "placeholder": "Comentario..."
    })
)
