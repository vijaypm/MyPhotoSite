from django.http import HttpResponse
# from django.template import RequestContext, loader
# from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404

from MyPhotos.models import User, UserAlbum


def index(request):
    user_list = User.objects.order_by('username')
    # Approach 1
    # output = ', '.join(str(u) for u in user_list) # join([str(u) for u in user_list]) # map(str, user_list)
    # return HttpResponse(output)
    # Approach 2
    # template = loader.get_template('myphotos/index.html')
    # context = RequestContext(request, {
    #     'user_list':user_list,
    # })
    # return HttpResponse(template._render(context))
    # Approach 3
    context = {'user_list':user_list}
    return render(request, 'myphotos/index.html', context)

def profile(request, user_id):
    # try:
    #     user = User.objects.get(pk=user_id)
    # except User.DoesNotExist:
    #     raise Http404
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'myphotos/profile.html', {'user':user})

def albums(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    album_list = get_list_or_404(UserAlbum, user_id=user_id)
    return render(request, 'myphotos/albums.html', {'user':user, 'album_list':album_list})

def photos(request, album_id):
    return HttpResponse("You are viewing photos in album %s" % album_id)