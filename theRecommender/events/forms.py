from django import forms
from .models import events,club

forms.DateInput.input_type = "date"
forms.TimeInput.input_type = "time"

class uploadclubform(forms.ModelForm):
    #clubtag = forms.CharField(max_length=3)
    class Meta:
        model=club
        fields = ('name','description')
    def __init__(self, *args, **kwargs):
        super(uploadclubform,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'id': 'group_name', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'id': 'message', 'cols':'30', 'rows':'7', 'class': 'form-control', 'placeholder': 'You can add your club description here...', 'name': 'message'})



class uploadeventform(forms.ModelForm):
    #clubtag = forms.CharField(max_length=3)
    class Meta:
        model=events
        fields = ('eventname','date','time','venue','description')
    def __init__(self, *args, **kwargs):
        super(uploadeventform,self).__init__(*args,**kwargs)
        #print(kwargs)
        #print(user)
        #self.fields['heading'].widget.attrs.update({'id': 'title', 'class': 'form-control'})
        self.fields['eventname'].widget.attrs.update({'id': 'group_name', 'class': 'form-control'})
        self.fields['tag']=forms.ModelChoiceField(queryset=club.objects.all() )
        self.fields['tag'].widget.attrs.update({'class':'form-control', 'placeholder':'Club Name'})
        self.fields['date'].widget.attrs.update({'class':'form-control' , 'id':'example-date-input'})
        self.fields['time'].widget.attrs.update({'id':'example-time-input', 'class': 'form-control'})
        self.fields['venue'].widget.attrs.update({'id': 'group_name', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'id': 'message', 'cols':'30', 'rows':'7', 'class': 'form-control', 'placeholder': 'You can add your event description here...', 'name': 'message'})

    def save(self,user,clubtag,commit=True):
        event=super(uploadeventform,self).save(commit=False)
        event.creator=user #or evt.user
        event.event_tags=clubtag
        #event['uni']=user.university #or evt.university

        if commit:
            event.save()
        return event
        '''
        def save(self, course, commit=True):
            event = super(uploadeventform, self).save(commit=False)
            event.creator = request.user
            if commit:
                event.save()
            return event
        '''        
