from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("Cookie Set")
    cookie = request.COOKIES.get('cookie_name')
    print("cookie", cookie)
    if cookie:
        response.set_cookie(key='cookie_name', value='cookie_value_updated', max_age=1000)
    else:
        response.set_cookie('cookie_name', 'cookie_value', max_age=1000)
    # to delete
    # response.delete_cookie('cookie_name')
    return response

def set_test_cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("Test cookie set")

def check_test_cookie(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()  # Clean up after check
        return HttpResponse("Test cookie worked!")
    else:
        return HttpResponse("Test cookie failed!")



def home(request):
    return HttpResponse("Welcome to the homepage!")
