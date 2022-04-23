from django.shortcuts import redirect, render

# Create your views here.
def admin_signin(request):
    if request.method =='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')

        if username == 'admin' and pwd == 'admin':
            print('hello')
            return redirect('admin_home')
        else:
            print('Invalid login')
    return render(request,'admin/admin-signin.html')

def admin_signup(request):
    return render(request,'admin/admin-signup.html')

def admin_view_bookings(request):
    
    return render(request,'admin/admin-view-bookings.html')

def admin_view_companies(request):
    return render(request,'admin/admin-view-companies.html')

def admin_view_feedbacks(request):
    return render(request,'admin/admin-view-feedbacks.html')

def admin_view_users(request):
    return render(request,'admin/admin-view-users.html')

def admin_home(request):
    return render(request,'admin/admin-home.html')
