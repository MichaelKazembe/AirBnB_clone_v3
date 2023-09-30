#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.city import City

# Create and save State objects
state1 = State(name="California")
state2 = State(name="New York")
state1.save()
state2.save()

# Create and save City objects associated with States
city1 = City(name="Los Angeles", state_id=state1.id)
city2 = City(name="New York City", state_id=state2.id)
city1.save()
city2.save()

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

# Retrieve the first state
first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
