from django.shortcuts import render
from .models import box

def home(request):
    boxes = box.objects.all()
    lenboxes = box.objects.count()

    boxes1 = []
    boxes2 = []
    boxes3 = []

    third = round(lenboxes/3)

    boxes1= boxes[:third]
    boxes2 = boxes[third:third*2]
    boxes3 = boxes[third * 2:lenboxes]


    # for i in range(len(boxes)):
    #     if i % 3 == 0:
    #         boxes1.append(boxes[i])
    #     elif i % 3 == 1:
    #         boxes2.append(boxes[i])
    #     else:
    #         boxes3.append(boxes[i])

    return render(request, 'card/home.html', {'boxes': boxes, 'boxes1': boxes1, 'boxes2': boxes2, 'boxes3': boxes3})
