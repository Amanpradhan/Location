# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Loc
import json as simplejson
#from django.utils import simplejson
from django.core.serializers import serialize
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
from django.http import HttpResponse
from django.core import serializers

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, json):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)

lat = 0
lon = 0
# Create your views here.
#d1 = [("lat": (28.6781724), "lon": (77.4797189)),("lat": (28.6768652), "lon": (77.4728990)),("lat": (28.6763763), "lon": (77.4701303))]
#loc = serializers.serialize('json', Loc.objects.all(), fields=('lat','lon'))
loc = [{"lat": 28.6781724, "lon": 79.4797189},{"lat": 28.6768652, "lon": 77.4728990},{"lat": 28.6763763, "lon": 77.4701303}]
def index(request):
	#loc = Loc.objects.all();
	#context = 
	#{
	#'loc': loc
	#}
	#d = simplejson.dumps(d1)
	#d = serialize('json', Loc.objects.all(), cls=LazyEncoder)
	#locs = serializers.serialize('json', loc)
	#locs=simplejson.dumps(d1)
	#locs=json.dumps(locs)
	#loc = serializers.serialize('json', Loc.objects.all())
	return render(request, 'inventory.html', {'locs':loc})

def request_access(request):
    print("DJANGO VIEW")
    loc = [{"lat": 28.6781724, "lon": 77.4797189},{"lat": 28.6768652, "lon": 77.4728990}]
    if request.method == "POST":
        print("DATA: ", request.POST.get('request_data'))
        #return HttpResponse(loc, content_type="application/json")
        return render(request, 'inventory.html', {'locs':loc})
