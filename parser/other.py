import jsonpickle
from jsonpickle.handlers import BaseHandler


class Room(object):      # note: class name is Capitalized
    def __init__(self, number, name):
        self.number = number
        self.name = name

    # get_ methods are non-Pythonic.
    # If you need to do some processing to retrieve room number,
    # make it a @property; otherwise, just use the field name

class House(object):
    def __init__(self, num_rooms):
        # I assume you don't want a room 0?
        self.rooms = [Room(i, 'Room#' + str(i)) for i in range(1, num_rooms+1)]
    def __iter__(self):
        return iter(self.rooms)


jsonpickle.handlers.register(Room, base=True)
class RoomHandler(BaseHandler):

    def flatten(self, obj, data):
        data = {}
        data['id'] = obj.number
        data['name'] = obj.name
        return data

    def restore(self, obj):
        raise NotImplementedError


@jsonpickle.handlers.register(House, base=True)
class HouseHandler(BaseHandler):

    def flatten(self, obj, data):
        data = {}
        # data['rooms'] = list(obj.__getattribute__('rooms'))
        if obj.rooms is not None:
            rooms = [self.context.flatten(x, reset=False) for x in obj.rooms]
            data['rooms'] = rooms
        return data

    def restore(self, obj):
        raise NotImplementedError


def main():
    house = House(5)
    print(house.__dict__)
    HouseHandler.handles(House)
    RoomHandler.handles(Room)

    room0 = jsonpickle.encode(house.rooms[0])
    print(room0)

    house1 = jsonpickle.encode(house)
    print(house1)

if __name__ == "__main__": main()