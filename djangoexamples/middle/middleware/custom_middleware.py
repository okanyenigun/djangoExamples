import time
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse

# 
class CustomDemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("[Middleware Initialized]")  # Runs only once at server start

    def __call__(self, request):
        start_time = time.time()
        print(f"[Request Start] Path: {request.path}")

        # Pass the request to the next middleware or view
        response = self.get_response(request)

        duration = time.time() - start_time
        print(f"[Request End] Duration: {duration:.2f}s")

        return response

# class CustomDemoMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("[Middleware Initialized]")

#     def __call__(self, request):
#         self.process_request(request)
#         response = self.get_response(request)
#         return response

#     def process_request(self, request):
#         method = request.method
#         path = request.path
#         print(f"[Request] Method: {method}, Path: {path}")

# from django.shortcuts import redirect
# from django.urls import reverse

# class CustomDemoMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.protected_classes = ['AjaxViewer']  # Use your CBV class names
#         print("[Middleware Initialized]")

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         if hasattr(view_func, 'view_class'):
#             view_class_name = view_func.view_class.__name__
#             if view_class_name in self.protected_classes:
#                 if not request.user.is_authenticated:
#                     print(f"[Redirecting Unauthenticated User] Tried to access {view_class_name}")
#                     return redirect(reverse('account_login'))  # Your login URL name here
#         return None

# from django.shortcuts import render

# class CustomDemoMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.protected_classes = ['AjaxViewer']
#         print("[Middleware Initialized]")

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         if hasattr(view_func, 'view_class'):
#             view_class_name = view_func.view_class.__name__
#             if view_class_name in self.protected_classes:
#                 if not request.user.is_authenticated:
#                     return redirect(reverse('account_login'))
#         return None

#     def process_exception(self, request, exception):
#         print(f"[Exception Caught] Path: {request.path}")
#         print(f"Error: {str(exception)}")

#         # Return a custom error page
#         return render(request, 'error_page.html', status=500)



# class CustomDemoMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.protected_classes = ['AjaxViewer']
#         print("[Middleware Initialized]")

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         if hasattr(view_func, 'view_class'):
#             view_class_name = view_func.view_class.__name__
#             if view_class_name in self.protected_classes:
#                 if not request.user.is_authenticated:
#                     return redirect(reverse('account_login'))
#         return None

#     def process_exception(self, request, exception):
#         print(f"[Exception Caught] Path: {request.path}")
#         print(f"Error: {str(exception)}")
#         return render(request, 'error_page.html', status=500)

#     def process_template_response(self, request, response):
#         print(f"[Template Response Hook] Adding app_name to context")
#         response.context_data['app_name'] = 'My Cool Django App'
#         return response

# class CustomDemoMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.protected_classes = ['AjaxViewer']
#         print("[Middleware Initialized]")

#     def __call__(self, request):
#         response = self.get_response(request)
#         response = self.process_response(request, response)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         if hasattr(view_func, 'view_class'):
#             view_class_name = view_func.view_class.__name__
#             if view_class_name in self.protected_classes:
#                 if not request.user.is_authenticated:
#                     return redirect(reverse('login'))
#         return None

#     def process_exception(self, request, exception):
#         print(f"[Exception Caught] Path: {request.path}")
#         print(f"Error: {str(exception)}")
#         return render(request, 'error_page.html', status=500)

#     def process_template_response(self, request, response):
#         print(f"[Template Response Hook] Adding app_name to context")
#         response.context_data['app_name'] = 'My Cool Django App'
#         return response

#     def process_response(self, request, response):
#         response['X-App-Name'] = 'MyDjangoProject'
#         print(f"[Response Hook] Added X-App-Name header to response")
#         return response
