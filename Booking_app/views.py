from django.shortcuts import render, redirect
from django.views import View

from Booking_app.models import ConferenceRoom


# Create your views here.
class AddNewRoomView(View):
    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        name = request.POST.get('room-name')
        capacity = request.POST.get('capacity')
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get('projector') == 'on'

        if not name:
            return render(request, 'add_room.html', {'error': 'The conference room name was not provided'})
        if capacity <=0:
            return render(request, 'add_room.html', {'error': 'The room capacity must be a positive number'})
        if ConferenceRoom.objects.filter(name=name).first():
            return render(request, 'add_room.html', {'error': 'The room with the provided name already exists'})

        ConferenceRoom.objects.create(name=name, number_of_seats=capacity, projector=projector)
        return redirect('room-list')


class RoomListView(View):
    def get(self, request):
        rooms = ConferenceRoom.objects.all()
        return render(request, 'rooms.html', {'rooms': rooms})


class DeleteRoomView(View):
    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        room.delete()
        return redirect('room-list')


class ModifyRoomView(View):
    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        return render(request, 'modify_room.html', {'room': room})

    def post(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        name = request.POST.get('room-name')
        capacity = request.POST.get('capacity')
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get('projector') == 'on'

        if not name:
            return render(request, 'modify_room.html', {'room': room, 'error': 'The conference room name was not provided'})
        if capacity <=0:
            return render(request, 'modify_room.html', {'room': room, 'error': 'The room capacity must be a positive number'})
        if name != room.name and ConferenceRoom.objects.filter(name=name).first():
            return render(request, 'modify_room.html', {'room': room, 'error': 'The room with the provided name already exists'})

        room.name = name
        room.number_of_seats = capacity
        room.projector = projector
        room.save()
        return redirect('room-list')


class ReserveRoomView(View):
    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        return render(request, 'reserve_room.html',{'room': room})

    def post(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        date = request.POST.get('reservation-date')
        comment = request.POST.get('comment')

        