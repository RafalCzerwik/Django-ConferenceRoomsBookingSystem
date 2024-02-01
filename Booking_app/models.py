from django.db import models


# Create your models here.
class ConferenceRoom(models.Model):
    """
    Model representing a conference room.

    Attributes:
    - name (CharField): The name of the conference room, unique.
    - number_of_seats (IntegerField): The number of seats in the room.
    - projector (BooleanField): Indicates whether the room is equipped with a projector.

    Method:
    - __str__(): Method returning a readable representation of the object.
    """
    name = models.CharField(max_length=255, unique=True)
    number_of_seats = models.IntegerField()
    projector = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RoomReservation(models.Model):
    """
    Model representing a reservation for a conference room.

    Attributes:
    - room_id (ForeignKey): Foreign key to the ConferenceRoom model, specifying the room.
    - date (DateField): Reservation date.
    - comment (TextField): Comment for the reservation, optional.

    Meta:
    - unique_together: Parameter set to ensure the uniqueness of the combination of room_id and date.
    """
    room_id = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)


class Meta:
    unique_together = ('room_id', 'date')
