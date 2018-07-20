# coding: UTF-8
# 御风
from .models import *
from django import forms
from django.forms import ValidationError
from django.forms import widgets



class BookForm(forms.Form):
    # name = models.CharField(max_length=32, verbose_name='图书名')
    # publish_year = models.DateField(verbose_name='出版日期')
    # publish_add = models.DateTimeField(verbose_name='上架日期')
    # price = models.IntegerField(verbose_name='价格')
    # stocks = models.IntegerField(verbose_name='图书库存')
    # status = models.BooleanField(verbose_name='出版状态，0未出版，1出版', default=True)
    # type = models.ForeignKey('TypeBook')
    # author = models.ManyToManyField('Author')
    # publisher = models.ForeignKey('Publisher')
    # info = models.OneToOneField('Details', blank=True, null=True, unique=True)

    status = [(1, "出版"), (0, "未出版")]

    name = forms.CharField(
        max_length=32,
        min_length=2,
        widget=widgets.TextInput(
            attrs={'type': 'text', 'placeholder': '书名', 'class': 'form-control', 'id': 'bookname', }
        )
    )

    publish_year = forms.DateField(
        widget=widgets.DateInput(
            attrs={'placeholder': '出版日期：2017-1-1', 'class': 'form-control', 'id': 'publish_yesr', }
        )
    )

    price = forms.IntegerField(
        widget=widgets.NumberInput(
            attrs={"placeholder": "价格", "class": "form-control", "id": "price", }
        )
    )

    stocks = forms.IntegerField(
        widget=widgets.NumberInput(
            attrs={"placeholder": "库存", "class": "form-control", "id": "stocks", }
        )
    )

    author = forms.MultipleChoiceField(
        widget=widgets.SelectMultiple(
            attrs={"id": "demo-cs-multiselect"}
        ))

    status = forms.ChoiceField(
        choices=status,
        widget=widgets.Select(
            attrs={"class": "magic-select", "type": "select", "id": 'status', }
        )

    )

    type = forms.ChoiceField(
        initial=0,
        widget=widgets.Select(
            attrs={"class": "selectpicker", "data-live-search": "true", "data-width": "100%", "id": "type", }
        )
    )

    publisher = forms.ChoiceField(
        initial=0,
        widget=widgets.Select(
            attrs={"class": "selectpicker", "data-live-search": "true", "data-width": "100%", "id": "publisher", }
        )
    )


    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        author_name = Author.objects.all().values_list("id", "name")
        type_name = TypeBook.objects.all().values_list("id", "type_book")
        publish_name = Publisher.objects.all().values_list("id", "name")

        self.fields['author'].choices = author_name
        self.fields['type'].choices = [(0, u'------------')] + list(type_name)
        self.fields['publisher'].choices =  [(0, u'------------')] + list(publish_name)



class DetailsForm(forms.Form):
    """
    chapter = models.CharField(max_length=32, verbose_name='章节')
    pages = models.IntegerField(verbose_name='页数')
    words = models.IntegerField(verbose_name='字数')
    contentinfo = models.TextField(verbose_name='内容简介')
    logo = models.ImageField(verbose_name='书本图片', upload_to='images/logos/%Y/%m', max_length=100)
    catalog = models.TextField(verbose_name='目录')
    """

    chapter = forms.IntegerField(
        widget=widgets.NumberInput(
            attrs={"placeholder": "章节", "class": "form-control", 'id': 'chapter', }
        )
    )

    pages = forms.IntegerField(
        widget=widgets.NumberInput(
            attrs={"placeholder": "页数", "class": "form-control", "id": "pages", }
        )
    )

    words = forms.IntegerField(
        widget=widgets.NumberInput(
            attrs={"placeholder": "字数", "class": "form-control", "id": "words", }
        )
    )

    contentinfo = forms.CharField(
        widget=widgets.Textarea(
            attrs={"rows": 8, "class": "form-control", "id": "demo-textarea-input-1", "placeholder": "内容简介", }
        )
    )

    catalog = forms.CharField(
        widget=widgets.Textarea(
            attrs={"rows": 8, "class": "form-control", "id": "demo-textarea-input-2", "placeholder": "目录", }
        )
    )

    logo = forms.ImageField(
        required=False,
        widget=widgets.FileInput(
            attrs={"id": "logo_file", "class": "fileinput-new btn btn-primary btn-file", "style": ""}
        )
    )