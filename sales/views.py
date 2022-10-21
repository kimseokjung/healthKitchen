from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .form import ProductForm
from django.core.paginator import Paginator
from django.contrib import messages


def index(request):
    return render(request, 'main.html')


def product_list(request):
    """
    sales 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지
    # 조회
    product_data = Product.objects.order_by('-create_date')
    paginator = Paginator(product_data, 9)  # 9개씩 페이지 보여 주기
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


@login_required(login_url='common:login')
def product_create(request):
    """
    sales 상품 등록
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_data = form.save(commit=False)
            product_data.author = request.user
            product_data.create_date = timezone.now()
            product_data.save()
            return redirect('sales:index')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'sales/product_form.html', context)


@login_required(login_url='common:login')
def product_modify(request, product_id):
    """
    sales 상품 수정
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.user != product.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('sales:detail', product_id=product.id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.create_date = timezone.now()
            product.save()
            return redirect('sales:detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'sales/product_form.html', context)


@login_required(login_url='common:login')
def product_delete(request, product_id):
    """
    sales 상품 삭제
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.user != product.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('sales:detail', product_id=product.id)
    product.delete()
    return redirect('sales:product_list')













