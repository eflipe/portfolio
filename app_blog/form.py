from django import forms

my_default_errors = {
    'required': 'Este campo es requerido.',
    'invalid': 'Ingrese un dato válido.'
}

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
    name = forms.CharField(max_length=25, label="Nombre",
                           error_messages=my_default_errors,
                           widget=forms.TextInput(attrs={
                            "class": "form-control",
                            "placeholder": "Nombre..."
                            })
                           )
    email = forms.EmailField(label="De",
                             error_messages={'required': 'Por favor, ingrese un email válido.', },
                             widget=forms.EmailInput(attrs={
                              "class": "form-control",
                              "placeholder": "Tu email"
                             })
                            )
    to = forms.EmailField(label="Para",
                          error_messages={'required': 'Por favor, ingrese un email válido.', },
                          widget=forms.EmailInput(attrs={
                           "class": "form-control",
                           "placeholder": "Email destinatario"
                          })
                         )

    comments = forms.CharField(required=False, label="Comentarios",
                               widget=forms.Textarea(
                                attrs={
                                    "class": "",
                                    "placeholder": "Escribe algo bonito..."
                                    })
                               )
