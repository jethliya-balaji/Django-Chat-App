from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Room
from .forms import SignUpForm, RoomCreationsForm

# Create your views here.


def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('rooms')

    return render(request, 'chat/signup.html', {'form': form})


@login_required
def rooms(request):
    my_rooms = request.user.created_rooms.all()
    rooms = Room.objects.all().exclude(id__in=my_rooms.values_list('id', flat=True))
    return render(request, 'chat/rooms.html', context={'my_rooms': my_rooms, 'rooms': rooms})


@login_required
def room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    websocket_url = request.get_host() + '/ws/room/' + room.name + '/'

    if room.private_room:
        if request.method == 'POST':
            passcode = request.POST.get('auth_passcode')
            if room.check_passcode(passcode):
                return render(request, 'chat/room.html', context={'room': room, 'websocket_url': websocket_url})
            else:
                error_message = '!! Incorrect Passcode !!'
                return render(request, 'chat/private_room.html', context={'room': room, 'error_message': error_message})
        else:
            error_message = ''
            return render(request, 'chat/private_room.html', context={'room': room, 'error_message': error_message})
    else:
        return render(request, 'chat/room.html', context={'room': room, 'websocket_url': websocket_url})


@login_required
def create_room(request):
    form = RoomCreationsForm(request.POST or None)
    if form.is_valid():
        room = form.save(commit=False)
        room.created_by = request.user
        room.save()
        return redirect('room', pk=room.pk)

    return render(request, 'chat/create_room.html', {'form': form})


@login_required
def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)

    if request.user != room.created_by:
        return redirect('rooms')

    if request.method == 'POST':
        if 'passcode' in request.POST:
            form = RoomCreationsForm(request.POST, instance=room)
            if form.is_valid():
                form.save()
                return redirect('rooms')
        else:
            passcode = request.POST.get('auth_passcode')
            if not room.check_passcode(passcode):
                error_message = '!! Incorrect Passcode !!'
                return render(request, 'chat/private_room.html', context={'room': room, 'error_message': error_message})

        form = RoomCreationsForm(instance=room)
    else:
        form = RoomCreationsForm(instance=room)

        if room.private_room:
            error_message = ''
            return render(request, 'chat/private_room.html', context={'room': room, 'error_message': error_message})

    return render(request, 'chat/edit_room.html', {'form': form, 'room': room})

@login_required
def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('rooms')
    return render(request, 'chat/delete_room.html', {'room': room})
