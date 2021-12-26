from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from Chat.models import Thread
#First Person = Company
#Second Person = Developer
@login_required
def messages_page(request):
    # user_status = online_users.models.OnlineUserActivity.get_user_activities(timedelta(seconds=60))
    # users = (user for user in  user_status)
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads,
        # "online_users": users,
    }
    return render(request, 'messages.html', context)
# @login_required
# def user_search(request):
#     # user_status = online_users.models.OnlineUserActivity.get_user_activities(timedelta(seconds=60))
#     # users = (user for user in  user_status)
#     threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
#     context = {
#         'Threads': threads,
#         # "online_users": users,
#     }
#     return render(request, 'messages.html', context)

# class SearchResultsView(ListView):
#     model = Thread
#     template_name = 'messages.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         Company = Thread.first_person
#         Developer= Thread.second_person
#         Threads = Thread.objects.filter(
#             Q(first_person__username__icontains=query) |  Q(second_person__username__icontains=query)
#         )
#         return Threads
@login_required
def search(request):
    if 'q' in request.GET:
        keyword = request.GET['q']
        user = get_user_model()
        if keyword:
          #if user.type == developer:
            #Threads = Thread.objects.filter(Q(first_person__username__icontains=keyword)
          #else:
            #Threads = Thread.objects.filter(Q(second_person__username__icontains=keyword)
          Threads = Thread.objects.filter(Q(first_person__username__icontains=keyword) |  Q(second_person__username__icontains=keyword))            #Products = Product.objects.all().filter(is_available=True)
    context = {
            'Threads' : Threads,
        }
    return render(request, 'messages.html', context)