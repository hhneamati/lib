import datetime
from django import forms 


from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class RnewBookForm(forms.Form):
    renewal_date = forms.forms.DateField(help_text = "تاریخ جدید را برای حداکثر چهار هفته دیگر ثبت کنید", required=False)

    def clean_renewal_date(self):
        data = self.cleaned_data["renewal_date"]
        return data

        if data < datetime.date.today():
            raise ValueError(_('تاریخی بعد از امروز انتخاب کنید'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValueError(_('نه می تونی بیشتر از یه ماه نگه داریش'))

        return data
    