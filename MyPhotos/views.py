from django.http import HttpResponse
# from django.template import RequestContext, loader
# from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.contrib.auth.models import User
from MyPhotos.models import UserAlbum, AlbumPhoto

from django.contrib.auth.decorators import login_required

# def index(request):
#     user_list = User.objects.order_by('username')
#     # Approach 1
#     # output = ', '.join(str(u) for u in user_list) # join([str(u) for u in user_list]) # map(str, user_list)
#     # return HttpResponse(output)
#     # Approach 2
#     # template = loader.get_template('myphotos/index.html')
#     # context = RequestContext(request, {
#     #     'user_list':user_list,
#     # })
#     # return HttpResponse(template._render(context))
#     # Approach 3
#     context = {'user_list':user_list}
#     return render(request, 'myphotos/index.html', context)

@login_required()
def index(request):
    try:
        album_list = UserAlbum.objects.get(user_id=request.user.id)
    except UserAlbum.DoesNotExist:
        album_list = ()
    return render(request, 'myphotos/albums.html', {'user':request.user, 'album_list':album_list})

@login_required()
def profile(request):
    # # try:
    # #     user = User.objects.get(pk=user_id)
    # # except User.DoesNotExist:
    # #     raise Http404
    # user = get_object_or_404(User, pk=user_id)
    return render(request, 'myphotos/profile.html', {'user':request.user})

@login_required()
def photos(request, album_id):
    # return HttpResponse("You are viewing photos in album %s" % album_id)
    album = get_object_or_404(UserAlbum, pk = album_id)
    try:
        photo_list = AlbumPhoto.objects.get(album_id=album_id)
    except AlbumPhoto.DoesNotExist:
        photo_list = ()
    return render(request, 'myphotos/photos.html', {'user':request.user, 'photo_list':photo_list})