from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import Pizza
from datetime import datetime
import json
def create(request):
    if request.method == 'POST':
        try:
            order = json.loads(request.body.decode('utf-8'))
            type = order['pizza']['type']
            size = order['pizza']['size']
            toppings = order['pizza']['toppings']
            id = type+str(datetime.now())
            if type == "regular" or type =="square":
                Pizza.objects.create(p_id = id,p_size = size, p_type = type, p_toppings = toppings)
                data = {"Message":"Pizza created"}      
                return HttpResponse(json.dumps(data), status=200, content_type="application/json")
            else:
                data = {"Message":"this pizza type is not available"}
                return HttpResponse(json.dumps(data), status=200, content_type="application/json")
        except:
            data={"Message":"Invalid json provided"}
            return HttpResponse(json.dumps(data), status=200, content_type="application/json")
    else:
        data={"Service":"Online pizza api","Error":"404!","Message":"Access Forbiden"}
        return HttpResponse(json.dumps(data), status=200, content_type="application/json")
def list(request):
    if request.method == 'POST':
        try:
            order = json.loads(request.body.decode('utf-8'))
            type = order['pizza']['type']
            size = order['pizza']['size']
            data = Pizza.objects.filter(p_type = type, p_size = size)
            data = serializers.serialize('json', data)
            return HttpResponse(json.dumps(data), status=200, content_type="application/json")
        except:
            data = Pizza.objects.all()
            data = serializers.serialize('json', data)
            return HttpResponse(json.dumps(data), status=200, content_type="application/json")
    else:
        data={"Service":"Online pizza api","Error":"404!","Message":"Access Forbiden"}
        return HttpResponse(json.dumps(data), status=200, content_type="application/json")
def edit(request):
    if request.method == 'POST':
        try:
            order = json.loads(request.body.decode('utf-8'))
            operation = order['pizza']['operation']
            id = order['pizza']['id']
            if operation == "edit":
                toppings = order['pizza']['toppings']
                type = order['pizza']['type']
                size = order['pizza']['size']
                if type == "regular" or type == "square":
                    Pizza.objects.filter(p_id = id). update(p_size = size, p_type = type, p_toppings = toppings)
                    data = {"Message":"Pizza created"}      
                    return HttpResponse(json.dumps(data), status=200, content_type="application/json")
                else:
                    data = {"Message":"this pizza type is not available"}
                    return HttpResponse(json.dumps(data), status=200, content_type="application/json")
            elif operation == 'delete':
                Pizza.objects.filter(p_id = id). delete()
                data = {"Message":"Pizza deleted"}
                return HttpResponse(json.dumps(data), status=200, content_type="application/json")
        except:
            data={"Message":"Invalid json provided"}
            return HttpResponse(json.dumps(data), status=200, content_type="application/json")
    else:
        data={"Service":"Online pizza api","Error":"404!","Message":"Access Forbiden"}
        return HttpResponse(json.dumps(data), status=200, content_type="application/json")