from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

def index(request):
    return HttpResponse('Hello World')
    
    
    
def test(request):
    return HttpResponse('Welcome to my 2nd view')
    
def profile(request):
    jsonList = []
    req = requests.get('https://api.github.com/users/DrkSephy')
    jsonList.append(json.loads(req.content.decode('utf-8')))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
        
    parsedData.append(userData)
    return HttpResponse(parsedData)
        
        
        
        
        
        
        
    content = req.text
    return HttpResponse(content) 