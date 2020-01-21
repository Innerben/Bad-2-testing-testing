from world import World
from entity import Entity
from actor import Actor
from room import Room
from location import Location
from need import Need
from desire import Desire
from button import LocationSpot, ActorSpot
from career import Career, Role
from clock import Time
import event

world = World()

Entity.findEntityDelegate = world.findEntity
Entity.addEntitiesDelegate = world.addEntities
Entity.isPlayerDelegate = world.isPlayer

#Add Locations
world.addEntities(

    Location(name='apartment1').addRooms(
        Room(name='bedroom').addButtonSpots(
            LocationSpot(100, 100, destination=('apartment1','livingroom')),
            ActorSpot(0, 0),
            ActorSpot(1, 0, Need.ENERGY),
        ),
        Room('kitchen').addButtonSpots(
            ActorSpot(0, 0, Need.HUNGER),
        ),
        Room('bathroom').addButtonSpots(
            ActorSpot(0, 0, Need.HYGIENE),
        ),
        Room('livingroom').addButtonSpots(
            ActorSpot(0, 0, Need.SOCIAL),
            ActorSpot(0, 1, Need.SOCIAL),
            ActorSpot(0, 2, Need.SOCIAL),
            ActorSpot(0, 3, Need.SOCIAL),
        ),
    ),

    Location('apartment2').addRooms(
        Room('bedroom').addButtonSpots(
            LocationSpot(100, 100, destination=('apartment1','livingroom')),
            ActorSpot(0, 0),
            ActorSpot(1, 0, Need.ENERGY),
        ),
        Room('kitchen').addButtonSpots(
            ActorSpot(0, 0, Need.HUNGER),
        ),
        Room('bathroom').addButtonSpots(
            ActorSpot(0, 0, Need.HYGIENE),
        ),
        Room('livingroom').addButtonSpots(
            ActorSpot(0, 0, Need.SOCIAL),
            ActorSpot(0, 1, Need.SOCIAL),
            ActorSpot(0, 2, Need.SOCIAL),
            ActorSpot(0, 3, Need.SOCIAL),
        ),
    ),

    Location('tower').addRooms(
        Room('office'),
        Room('breakroom').addButtonSpots(
            ActorSpot(0, 0, Need.HUNGER),
            ActorSpot(0, 0, Need.SOCIAL),
        ),
        Room('bathroom').addButtonSpots(
            ActorSpot(0, 0, Need.HYGIENE),
        ),
    ),

    Location('gym').addRooms(
        Room('weights').addButtonSpots(
            ActorSpot(0, 0, Desire.PHYSIQUE)
        ),
        Room('yoga').addButtonSpots(
            ActorSpot(0, 0, Desire.PHYSIQUE)
        ),
        Room('snack bar').addButtonSpots(
            ActorSpot(0, 0, Need.HUNGER)
        ),
        Room('sauna').addButtonSpots(
            ActorSpot(0, 0, Need.HYGIENE)
        ),
    ),
)

#Set LocationButton destination references
for locationButton in world.entities[LocationSpot].itervalues():
    locationName = locationButton.destination[0]
    roomName = locationButton.destination[1]
    locationButton.setDestination(locationName, roomName)

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

#Set player
world.setPlayer(world.findEntity('geo'))