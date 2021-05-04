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


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25,
                           widget=forms.TextInput(attrs={
                            "class": "form",
                            "placeholder": "Nombre..."
                            })
                           )
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(
                                attrs={
                                    "class": "",
                                    "placeholder": "Comentario..."
                                    })
                               )
