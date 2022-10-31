from django.shortcuts import render, get_object_or_404, redirect
from customer.form import *
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return render(request, 'main.html')


def question_list(request):
    """
    customer 게시판 목록 출력
    """
    page = request.GET.get('page', '1')  # 페이지

    question = Question.objects.order_by('cdate')
    paginator = Paginator(question, 10)  # 9개씩 페이지 보여 주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'customer/question_list.html', context)


def detail(request, question_id):
    """
    customer 게시판 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'customer/question_detail.html', context)


def question_write(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():  # form이 유효하다면 형태 저장
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('customer:question_list')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'customer/question_form.html', context)