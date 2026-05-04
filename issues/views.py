from django.shortcuts import render, redirect, get_object_or_404
from .models import Issue
from .forms import IssueForm
from django.contrib.auth.decorators import login_required

def issue_report(request):
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)
            if request.user.is_authenticated:
                issue.author = request.user
            # Якщо користувач не залогінений, можна призначити дефолтного або зробити поле author необов'язковим
            issue.save()
            return redirect('problem_list')
    else:
        form = IssueForm()
    return render(request, 'issues/report_form.html', {'form': form})

@login_required
def problem_list(request):
    issues = Issue.objects.all().order_by('-date_reported')
    return render(request, 'issues/problem_list.html', {'issues': issues})

@login_required
def problem_detail(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    return render(request, 'issues/problem_detail.html', {'issue': issue})