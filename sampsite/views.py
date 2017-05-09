from django.http import HttpResponse
import random

def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return HttpResponse("root home page")

def random_number(request, max_random=100):
    random_num = random.randrange(0,int(max_random))

    msg = "Random number between 0 and %s : %d" %(max_random, random_num)
    return HttpResponse(msg)

