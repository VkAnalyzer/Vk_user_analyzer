from django.shortcuts import render
from django.http import HttpResponse


def music_recommendation(user_id):
    return HttpResponse('Музыка')