from django import forms

from blog.models import Post


class NuevoPost(forms.ModelForm):
    """Form to add new posts."""
    
    class Meta:
        model = Post  # Modelo del cual importa
        fields = [
            'name',
            'city',
            'title',
            'subtitle',
            'content',
            'image',
            ]
        #  Widget para agrandar el area de texto(TextField) a 80 columnas
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}
