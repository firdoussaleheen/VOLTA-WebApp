from django import forms
from django.contrib.auth.models import User


# Creates a profile for the User with first name, last name, and TUid.
# This profile information is used when generating a Word Document to
# submit for an official Lab Report which is turned in to the TA.
class UserSimulationImage(forms.Form):
    image = forms.FileField(label='Select a file',
                            help_text='<br>')
    
    def clean_file(self):
        file = self.cleaned_data.get("file", False)
        filetype = magic.from_buffer(file.read())
        if not "PNG" in filetype:
            raise ValidationError("File is not PNG.")
        return file
