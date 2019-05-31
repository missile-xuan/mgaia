from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.

#战术地图首页处理视图函数
def index(request):
    return render(request,'tacticalmap/index.html',{})

#地图房间处理视图函数
def maproom(request, room_name):
    return render(request, 'tacticalmap/maproom.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

