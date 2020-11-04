from django import forms


class UserSearchForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your first or last name'}
        )
    )


class NewSearchForm(forms.Form):
    text = forms.CharField(
        label='Enter Text: ',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter more than 3 chars'}
        )
    )
    choices = (
       ('first_name', 'Filter by first name'),
       ('last_name', 'Filter by last name'),
    )
    search_by = forms.MultipleChoiceField(
        choices=choices,
        widget=forms.CheckboxSelectMultiple(
            attrs={"checked": ""}
        )
    )
