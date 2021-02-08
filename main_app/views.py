from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artist, Flash
from .forms import TatsForm, FlashForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def artists_index(request):
    artists = Artist.objects.all()
    context = { 'artists_data': artists }
    return render(request, 'artists/index.html', context)

def artists_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    tats_form = TatsForm()
    flashs_artist_doesnt_have = Flash.objects.exclude(id__in = artist.flash.all().values_list('id'))
    context = {
        'artist': artist, 
        'tats_form': tats_form,
        'flashs': flashs_artist_doesnt_have
    }
    return render(request, 'artists/detail.html', context)

def add_tats(request, artist_id):
    form = TatsForm(request.POST)

    if form.is_valid():
        new_tats = form.save(commit=False)
        new_tats.artist_id = artist_id
        new_tats.save()

    return redirect('artists_detail', artist_id=artist_id)

def assoc_flash(request, artist_id, flash_id):
    artist = Artist.objects.get(id=artist_id)
    artist.flash.add(flash_id)
    return redirect('artists_detail', artist_id=artist_id)

def remove_flash(request, artist_id, flash_id):
    artist = Artist.objects.get(id=artist_id)
    artist.flash.remove(flash_id)
    return redirect('artists_detail', artist_id=artist_id)

def add_flash(request, artist_id, flash_id):
    artist = Artist.objects.get(id=artist_id)
    artist.flash.add(flash_id)
    return redirect('artists_detail', artist_id=artist_id)

def edit_flash(request, artist_id, flash_id):
  flash = Flash.objects.get(id=flash_id)

  if request.method == 'GET':
    flash_form = FlashForm(instance=flash)
    context = {'form': flash_form}
    return render(request, 'flash/edit.html', context)

  else:
    flash_form = FlashForm(request.POST, instance=flash)
    if flash_form.is_valid():
      flash_form.save()
      return redirect('artists_detail', artist_id=artist_id)