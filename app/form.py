from django import forms


class ContactForm(forms.Form):
    title = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(), required=False)

    def clean(self):
        data = super(ContactForm, self).clean()
        print(data)

        title = data.get('title')
        email = data.get('email')
        message = data.get('message')
        # if len(message)<100:
        #     raise forms.ValidationError("message should have minimum 100 character")