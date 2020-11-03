from django import forms
from django.core.validators import validate_comma_separated_integer_list


class MultiplyPhoneField(forms.Field):
    def to_python(self, value):
        return value.replace(" ", "")

    def validate(self, value):
        super().validate(value)
        validate_comma_separated_integer_list(value)


class NewFormApplication(forms.Form):
    email = forms.EmailField(
        label="Your email",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Write your email...'
            }
        )
    )
    address = forms.CharField(
        label="Your address",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your address...'
            }
        )
    )
    city = forms.CharField(
        max_length=100,
        label="Your city",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your city...'
            }
        )
    )

    phone_numbers = MultiplyPhoneField(
        label="Write phone numbers with comma"
    )
    #
    # def as_strong(self):
    #     "Return this form rendered as HTML <tr>s -- excluding the <table></table>."
    #     return self._html_output(
    #         normal_row='<strong%(html_class_attr)s><strong>%(label)s</strong><td>%(errors)s%(field)s%(help_text)s</td></tr>',
    #         error_row='<strong><td colspan="2">%s</td></tr>',
    #         row_ender='</td></tr>',
    #         help_text_html='<br><span class="helptext">%s</span>',
    #         errors_on_separate_row=False,
    #     )

    def clean(self):
        cleaned_data = super().clean()
        phones = cleaned_data.get('phone_numbers')
        if not phones:
            raise forms.ValidationError("Must add comma")
        phones_cleaned = phones.split(',')
        if len(phones_cleaned) < 2:
            self.add_error("phone_numbers", "Must put at least 2 phone numbers.")
        cleaned_data['phone_numbers'] = phones_cleaned
        return cleaned_data

    def clean_address(self):
        address = self.cleaned_data['address']
        if not address.isalnum():
            raise forms.ValidationError("Address must be allnum")
        return address



