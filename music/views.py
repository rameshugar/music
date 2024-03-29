from django.shortcuts import render, get_object_or_404

from .models import Album




def index(request):
	all_album = Album.objects.all()
	context = {'all_album': all_album}
	return render(request, 'index.html', context)
	


def detail(request, album_id):

	#album = Album.objects.get(pk=album_id)
	album = get_object_or_404(Album, pk=album_id)	
	
	return render(request, 'detail.html',{'album':album} )


def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])

	except (KeyError, Song.DoesNotExist):
		return render(request, 'detail.html', {'album':album, 'error_message': 'you did not select a valid song'})

	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'detail.html', {'album': album})


