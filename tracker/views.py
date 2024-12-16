# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login, logout, authenticate
# from tracker.forms import UserRegistrationForm, UserLoginForm, CategoryForm, FinancialEntryForm, ExpenseTypeForm
# from .models import Category, FinancialEntry, ExpenseType, Budget
# from django.db.models import Sum, Q




# def index(request):
#     return render(request, 'tracker/index.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'tracker/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('index')
#     else:
#         form = UserLoginForm()
#     return render(request, 'tracker/login.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('login')

# def create_category(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             category = form.save(commit=False)
#             category.user = request.user
#             category.save()
#             return redirect('index')
#     else:
#         form = CategoryForm()
#     return render(request, 'tracker/create_category.html', {'form': form})

# def delete_category(request, category_id):
#     category = Category.objects.get(id=category_id, user=request.user)
#     category.delete()
#     return redirect('index')

# def category_list(request):
#     categories = Category.objects.filter(user=request.user)
#     return render(request, 'tracker/category_list.html', {'categories': categories})

# def create_entry(request):
#     if request.method == 'POST':
#         form = FinancialEntryForm(request.POST)
#         if form.is_valid():
#             entry = form.save(commit=False)
#             entry.user = request.user
#             entry.save()
#             return redirect('index')
#     else:
#         form = FinancialEntryForm()
#     return render(request, 'tracker/create_entry.html', {'form': form})


# def delete_entry(request, entry_id):
#     entry = get_object_or_404(FinancialEntry, id=entry_id)
#     entry.delete()
#     return redirect('list_entries') 


# def summary(request):
#     income = FinancialEntry.objects.filter(entry_type='income', user=request.user).aggregate(Sum('value'))['value__sum'] or 0
#     expense = FinancialEntry.objects.filter(entry_type='expense', user=request.user).aggregate(Sum('value'))['value__sum'] or 0
#     category_summary = FinancialEntry.objects.values('category__name').filter(user=request.user).annotate(total=Sum('value'))
    
#     context = {
#         'income': income,
#         'expense': expense,
#         'category_summary': category_summary,
#     }
#     return render(request, 'tracker/summary.html', context)

# def create_expense_type(request):
#     if request.method == 'POST':
#         form = ExpenseTypeForm(request.POST)
#         if form.is_valid():
#             expense_type = form.save(commit=False)
#             expense_type.user = request.user
#             expense_type.save()
#             return redirect('expense_type_list')
#     else:
#         form = ExpenseTypeForm()
#     return render(request, 'tracker/create_expense_type.html', {'form': form})

# def delete_expense_type(request, expense_type_id):
#     expense_type = get_object_or_404(ExpenseType, id=expense_type_id, user=request.user)
#     if request.method == 'POST':
#         expense_type.delete()
#         return redirect('expense_type_list')
#     return render(request, 'tracker/confirm_delete_expense_type.html', {'expense_type': expense_type})

# def expense_type_list(request):
#     expense_types = ExpenseType.objects.filter(user=request.user)
#     return render(request, 'tracker/expense_type_list.html', {'expense_types': expense_types})

# def check_budget(entry):
#     budget = Budget.objects.filter(user=entry.user, category=entry.category).first()
#     if budget:
#         total_spent = FinancialEntry.objects.filter(user=entry.user, category=entry.category).aggregate(total_spent=models.Sum('value'))['total_spent']
#         if total_spent >= (budget.budgeted_amount * 0.85) and not budget.notification_sent:
#             # Send notification (could be in-app notification)
#             # Update the budget's notification_sent field
#             budget.notification_sent = True
#             budget.save()
#             # Send in-app notification logic here


# def summary_by_category(request):
#     category_summary = FinancialEntry.objects.values('category__name') \
#         .annotate(total_value=Sum('value')) \
#         .order_by('category__name')  # Optional: to order by category name
    
#     return render(request, 'tracker/summary_by_category.html', {'category_summary': category_summary})

# def summary_by_type(request):
#     income = FinancialEntry.objects.filter(entry_type='income').aggregate(Sum('value'))['value__sum'] or 0
#     expense = FinancialEntry.objects.filter(entry_type='expense').aggregate(Sum('value'))['value__sum'] or 0
#     return render(request, 'tracker/summary_by_type.html', {'income': income, 'expense': expense})

# def summary_by_category_and_type(request):
#     category_type_summary = FinancialEntry.objects.values('category__name', 'entry_type') \
#         .annotate(total_value=Sum('value')) \
#         .order_by('category__name', 'entry_type') 
    
#     return render(request, 'tracker/summary_by_category_and_type.html', {'category_type_summary': category_type_summary})

# def list_entries(request):
#     entries = FinancialEntry.objects.all()
#     return render(request, 'tracker/list_entries.html', {'entries': entries})

# def update_entry(request, entry_id):
#     entry = get_object_or_404(FinancialEntry, id=entry_id)
    
#     if request.method == 'POST':
#         form = FinancialEntryForm(request.POST, instance=entry)
#         if form.is_valid():
#             form.save()
#             return redirect('list_entries')
#     else:
#         form = FinancialEntryForm(instance=entry)

#     return render(request, 'tracker/update_entry.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from tracker.forms import UserRegistrationForm, UserLoginForm, CategoryForm, FinancialEntryForm, ExpenseTypeForm
from .models import Category, FinancialEntry, ExpenseType, Budget
from django.db.models import Sum, Q
from django.contrib.auth.decorators import login_required  # Ensure that only authenticated users can access these views


# Ensure user is logged in before accessing the following views
@login_required
def index(request):
    return render(request, 'tracker/index.html')


# User Registration view (no change needed)
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'tracker/register.html', {'form': form})


# User Login view (no change needed)
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'tracker/login.html', {'form': form})


# User Logout view (no change needed)
def user_logout(request):
    logout(request)
    return redirect('login')


# Category CRUD views with user filter
@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user  # Associate category with the current user
            category.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'tracker/create_category.html', {'form': form})


@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)  # Ensure user owns the category
    category.delete()
    return redirect('index')


@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)  # Only get categories for the logged-in user
    return render(request, 'tracker/category_list.html', {'categories': categories})


# Financial Entry CRUD views with user filter
@login_required
def create_entry(request):
    if request.method == 'POST':
        form = FinancialEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user  # Associate entry with the current user
            entry.save()
            return redirect('index')
    else:
        form = FinancialEntryForm()
    return render(request, 'tracker/create_entry.html', {'form': form})


@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(FinancialEntry, id=entry_id, user=request.user)  # Ensure user owns the entry
    entry.delete()
    return redirect('list_entries')


@login_required
def update_entry(request, entry_id):
    entry = get_object_or_404(FinancialEntry, id=entry_id, user=request.user)  # Ensure user owns the entry
    
    if request.method == 'POST':
        form = FinancialEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('list_entries')
    else:
        form = FinancialEntryForm(instance=entry)

    return render(request, 'tracker/update_entry.html', {'form': form})


# Summary views with user filtering
@login_required
def summary(request):
    income = FinancialEntry.objects.filter(entry_type='income', user=request.user).aggregate(Sum('value'))['value__sum'] or 0
    expense = FinancialEntry.objects.filter(entry_type='expense', user=request.user).aggregate(Sum('value'))['value__sum'] or 0
    category_summary = FinancialEntry.objects.filter(user=request.user) \
        .values('category__name') \
        .annotate(total=Sum('value')) \
        .order_by('category__name')

    context = {
        'income': income,
        'expense': expense,
        'category_summary': category_summary,
    }
    return render(request, 'tracker/summary.html', context)


@login_required
def summary_by_category(request):
    category_summary = FinancialEntry.objects.filter(user=request.user) \
        .values('category__name') \
        .annotate(total_value=Sum('value')) \
        .order_by('category__name')  # Optional: to order by category name
    
    return render(request, 'tracker/summary_by_category.html', {'category_summary': category_summary})


@login_required
def summary_by_type(request):
    income = FinancialEntry.objects.filter(entry_type='income', user=request.user).aggregate(Sum('value'))['value__sum'] or 0
    expense = FinancialEntry.objects.filter(entry_type='expense', user=request.user).aggregate(Sum('value'))['value__sum'] or 0
    return render(request, 'tracker/summary_by_type.html', {'income': income, 'expense': expense})


@login_required
def summary_by_category_and_type(request):
    category_type_summary = FinancialEntry.objects.filter(user=request.user) \
        .values('category__name', 'entry_type') \
        .annotate(total_value=Sum('value')) \
        .order_by('category__name', 'entry_type')

    return render(request, 'tracker/summary_by_category_and_type.html', {'category_type_summary': category_type_summary})


# Expense Type CRUD views with user filter
@login_required
def create_expense_type(request):
    if request.method == 'POST':
        form = ExpenseTypeForm(request.POST)
        if form.is_valid():
            expense_type = form.save(commit=False)
            expense_type.user = request.user  # Associate expense type with the current user
            expense_type.save()
            return redirect('expense_type_list')
    else:
        form = ExpenseTypeForm()
    return render(request, 'tracker/create_expense_type.html', {'form': form})


@login_required
def delete_expense_type(request, expense_type_id):
    expense_type = get_object_or_404(ExpenseType, id=expense_type_id, user=request.user)  # Ensure user owns the expense type
    if request.method == 'POST':
        expense_type.delete()
        return redirect('expense_type_list')
    return render(request, 'tracker/confirm_delete_expense_type.html', {'expense_type': expense_type})


@login_required
def expense_type_list(request):
    expense_types = ExpenseType.objects.filter(user=request.user)  # Only get expense types for the logged-in user
    return render(request, 'tracker/expense_type_list.html', {'expense_types': expense_types})


# Budget check logic (no changes needed here)
def check_budget(entry):
    budget = Budget.objects.filter(user=entry.user, category=entry.category).first()
    if budget:
        total_spent = FinancialEntry.objects.filter(user=entry.user, category=entry.category).aggregate(total_spent=models.Sum('value'))['total_spent']
        if total_spent >= (budget.budgeted_amount * 0.85) and not budget.notification_sent:
            # Send notification (could be in-app notification)
            # Update the budget's notification_sent field
            budget.notification_sent = True
            budget.save()
            # Send in-app notification logic here\

def list_entries(request):
    entries = FinancialEntry.objects.filter(user=request.user)
    return render(request, 'tracker/list_entries.html', {'entries': entries})

