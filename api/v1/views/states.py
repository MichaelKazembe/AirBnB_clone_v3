#!/usr/bin/python3
"""
Defines the RESTful API actions for State objects
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def get_states():
    """ Retrieves the list of all State objects """
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """ Retrieves a State object by ID """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ Deletes a State object by ID """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ Creates a new State object """
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Updates a State object by ID """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    data.pop('id', None)
    data.pop('created_at', None)
    data.pop('updated_at', None)
    for key, value in data.items():
        setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
