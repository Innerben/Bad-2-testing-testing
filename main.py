from world import World
from entity import GameEntity
from actor import Actor
from room import Room
from location import Location
from need import Need
from desire import Desire
from button import LocationButtonSpot, ActorButtonSpot
from career import Career, Role
from clock import Time

world = World()

GameEntity.setFindEntityDelegate(world.findEntity)

#Add Locations
world.addEntities(

    Location(name='apartment1').addRooms(
        Room(name='bedroom').addButtonSpots(
            LocationButtonSpot(100, 100, 'apartment1', 'livingroom'),
            ActorButtonSpot(0, 0),
            ActorButtonSpot(1, 0, Need.ENERGY),
        ),
        Room('kitchen').addButtonSpots(
            ActorButtonSpot(0, 0, Need.HUNGER),
        ),
        Room('bathroom').addButtonSpots(
            ActorButtonSpot(0, 0, Need.HYGIENE),
        ),
        Room('livingroom').addButtonSpots(
            ActorButtonSpot(0, 0, Need.SOCIAL),
            ActorButtonSpot(0, 1, Need.SOCIAL),
            ActorButtonSpot(0, 2, Need.SOCIAL),
            ActorButtonSpot(0, 3, Need.SOCIAL),
        ),
    ),

    Location('apartment2').addRooms(
        Room('bedroom').addButtonSpots(
            LocationButtonSpot('apartment1', 'livingroom', 100, 100),
            ActorButtonSpot(0, 0),
            ActorButtonSpot(1, 0, Need.ENERGY),
        ),
        Room('kitchen').addButtonSpots(
            ActorButtonSpot(0, 0, Need.HUNGER),
        ),
        Room('bathroom').addButtonSpots(
            ActorButtonSpot(0, 0, Need.HYGIENE),
        ),
        Room('livingroom').addButtonSpots(
            ActorButtonSpot(0, 0, Need.SOCIAL),
            ActorButtonSpot(0, 1, Need.SOCIAL),
            ActorButtonSpot(0, 2, Need.SOCIAL),
            ActorButtonSpot(0, 3, Need.SOCIAL),
        ),
    ),

    Location('tower').addRooms(
        Room('office'),
        Room('breakroom').addButtonSpots(
            ActorButtonSpot(0, 0, Need.HUNGER),
            ActorButtonSpot(0, 0, Need.SOCIAL),
        ),
        Room('bathroom').addButtonSpots(
            ActorButtonSpot(0, 0, Need.HYGIENE),
        ),
    ),

    Location('gym').addRooms(
        Room('weights').addButtonSpots(
            ActorButtonSpot(0, 0, Desire.PHYSIQUE)
        ),
        Room('yoga').addButtonSpots(
            ActorButtonSpot(0, 0, Desire.PHYSIQUE)
        ),
        Room('snack bar').addButtonSpots(
            ActorButtonSpot(0, 0, Need.HUNGER)
        ),
        Room('sauna').addButtonSpots(
            ActorButtonSpot(0, 0, Need.HYGIENE)
        ),
    ),
)

#Add Careers
world.addEntities(
    Career(name='business', location='tower').addRoles(
        Role(title='drone', startTime=9, endTime=17),
        Role('lead', 8, 17),
        Role('manager', 7, 18),
        Role('ceo', 6, 20),
    )
)

#Add Actors
world.addEntities(
    Actor(name='geo', locationName='apartment1', roomName='bedroom'),
    Actor('leo', 'apartment1', 'livingroom'),
    Actor('deo', 'apartment1', 'bathroom'),
    Actor('neo', 'apartment1', 'kitchen'),
    Actor('jeb', 'apartment2', 'bedroom'),
)

#Set Actor attributes
world.findEntity('geo', store=True)
world.storedEntity.setCareer(careerName='business', careerLevel=0)