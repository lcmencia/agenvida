from __future__ import unicode_literals
from collections import OrderedDict

from django import forms 
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import ugettext, ugettext_lazy as _
import datetime
from .models import Purpose


class PurposeForm(forms.ModelForm):
    fecha_inicio =  forms.DateField(initial=datetime.date.today, label='Inicio')
    fecha_fin =  forms.DateField(initial=datetime.date.today, label='Fin')
    class Meta:
        model = Purpose
        fields = [
            "nombre",
            "fecha_inicio",
            "fecha_fin",
            "meta",
            "descripcion"
        ]

class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': _("Your old password was entered incorrectly. "
                                "Please enter it again."),
    })
    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput)

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password


PasswordChangeForm.base_fields = OrderedDict(
    (k, PasswordChangeForm.base_fields[k])
    for k in ['old_password', 'new_password1', 'new_password2']
)

