from django.shortcuts import render
from django.http import HttpResponse
from mipcl_py.models.trip import Trip

import json

with open("places.json") as f:
    data = json.load(f)

def health(request):
    return HttpResponse(json.dumps({'status': 'good'}), content_type = "application/json")

def trip(request):
    cost = [[0,10,15,20], [5,0,9,10], [6,13,0,12], [8,8,9,0]]
    n = 4
    prob = Trip("Test0")
    prob.model(n, cost)
    prob.optimize()
    prob.setSolution()
    return HttpResponse(json.dumps({'min-distance': data }), content_type = "application/json")