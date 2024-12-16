from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('entries/create/', views.create_entry, name='create_entry'),
    path('summary/', views.summary, name='summary'),
    path('expense_types/', views.expense_type_list, name='expense_type_list'),
    path('expense_types/create/', views.create_expense_type, name='create_expense_type'),
    path('expense_types/delete/<int:expense_type_id>/', views.delete_expense_type, name='delete_expense_type'),
    path('logout/', views.user_logout, name='user_logout'),
    path('summary-category/', views.summary_by_category, name='summary_by_category'),
    path('summary_by_category_and_type/', views.summary_by_category_and_type, name='summary_by_category_and_type'),
    path('summary_by_type/', views.summary_by_type, name='summary_by_type'),
    path('entries/', views.list_entries, name='list_entries'),
    path('entries/update/<int:entry_id>/', views.update_entry, name='update_entry'),
    path('entries/delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]




