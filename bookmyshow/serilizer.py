from rest_framework import serializers


# model 1
class CreateBookingRequestDto(serializers.Serializer):
    user_id = serializers.IntegerField()
    show_id = serializers.IntegerField()
    show_seat_id = serializers.ListField(child=serializers.IntegerField())

#req data = { user 1:showId :3,show seat id :[2,3]}