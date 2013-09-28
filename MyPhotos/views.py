from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext, loader
# from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.contrib.auth.models import User
from MyPhotos.models import UserAlbum, AlbumPhoto
from MyPhotos.forms import PhotoUploadForm

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

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
        album_list = UserAlbum.objects.filter(user_id=request.user.id)
    except UserAlbum.DoesNotExist:
        album_list = ()
    return render(request, 'myphotos/albums.html', {'user':request.user, 'album_list':album_list})

@login_required()
def add_album(request):
    if request.method == 'POST':
        album = UserAlbum(
            user=request.user,
            name=request.POST['name'])
        album.save()
        return HttpResponseRedirect('/myphotos/%d/photos' % album.id)

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
        photo_list = AlbumPhoto.objects.filter(album_id=album_id)
    except AlbumPhoto.DoesNotExist:
        photo_list = ()
    return render(request, 'myphotos/photos.html', {'user':request.user, 'album':album, 'photo_list':photo_list})

@login_required()
def add_photo(request, album_id):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                AlbumPhoto.objects.get(album_id=album_id, filename=request.FILES['imageFile'].name)
            except AlbumPhoto.DoesNotExist:
                instance = form.save(commit=False)
                instance.filename = request.FILES['imageFile'].name
                instance.album_id = album_id
                instance.save()
    return HttpResponseRedirect('/myphotos/%s/photos' % album_id)

@login_required()
def del_photo(request, album_id, photo_id):
    photo = get_object_or_404(AlbumPhoto, pk = photo_id)
    photo.delete()
    return HttpResponseRedirect('/myphotos/%s/photos' % album_id)