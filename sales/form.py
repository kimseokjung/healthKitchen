from django import forms
from sales.models import Product
from ckeditor_uploader.fields import RichTextUploadingField


class ProductForm(forms.ModelForm):
    pcode = forms.CharField(
        max_length=100,
        label='상품 코드',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '상품 코드 입력'
            }
        )
    )
    pname = forms.CharField(
        max_length=100,
        label='상품명',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '상품명 입력'
            }
        )
    )

    class Meta:
        model = Product
        fields = ['pcode', 'pname', 'imgfile', 'unitprice', 'discountrate', 'description']
        labels = {
            'imgfile': '샘플 이미지',
            'unitprice': '가격',
            'discountrate': '할인율',
            'description': '상세 내용',
        }
