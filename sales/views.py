from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .form import ProductForm
from django.core.paginator import Paginator


def index(request):
    """
    sales 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지
    # 조회
    product_list = Product.objects.order_by('-create_date')
    paginator = Paginator(product_list, 9)  # 9개씩 페이지 보여 주기
    page_obj = paginator.get_page(page)

    context = {'product_list': page_obj}
    return render(request, 'sales/product_list.html', context)


def detail(request, product_id):
    """
    sales 내용 출력
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'sales/product_detail.html', context)


def product_create(request):
    """
    sales 상품 등록
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_data = form.save(commit=False)
            product_data.create_date = timezone.now()
            product_data.save()
            return redirect('sales:index')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'sales/product_form.html', context)
