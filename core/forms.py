from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "body"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full rounded-md border border-slate-300 px-3 py-2 dark:border-slate-700 dark:bg-slate-900"}),
            "email": forms.EmailInput(attrs={"class": "w-full rounded-md border border-slate-300 px-3 py-2 dark:border-slate-700 dark:bg-slate-900"}),
            "subject": forms.TextInput(attrs={"class": "w-full rounded-md border border-slate-300 px-3 py-2 dark:border-slate-700 dark:bg-slate-900"}),
            "body": forms.Textarea(attrs={"rows": 6, "class": "w-full rounded-md border border-slate-300 px-3 py-2 dark:border-slate-700 dark:bg-slate-900"}),
        }
