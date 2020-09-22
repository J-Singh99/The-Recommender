from django import forms
from .models import Group


class CreateGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_name', 'description', "image")
    def __init__(self, *args, **kwargs):
        super(CreateGroup,self).__init__(*args,**kwargs)
        self.fields['group_name'].widget.attrs.update({'id': 'group_name', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'id': 'message', 'cols':'30', 'rows':'7', 'class': 'form-control', 'placeholder': 'Write your notes or questions here...', 'name': 'message'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'name':'image'})

    def save(self, user, commit=True):
        group = super(CreateGroup, self).save(commit=False)
        group.admin = user
        if commit:
            group.save()
        return group