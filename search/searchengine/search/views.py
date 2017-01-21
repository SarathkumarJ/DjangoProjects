from django.shortcuts import render,HttpResponse
from bs4 import BeautifulSoup as BS
import requests
import re



def home(request):
    return render(request,'home.html')
    
def get_result(request):
#    query = result.POST['query']
     query =request.POST['query']
     response_set=[]
     for n in [0,10,20,30] :  # first 4 pages 10 resukt in single page 
         search_url = "https://www.google.co.in/search?q=%s&start=%s&sa=N" %(query, n)
         response = requests.get(search_url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
         soup = BS(response.content, "lxml")
         for url in soup.select('.r a'):
             valid_url =re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url.prettify())
             if valid_url :
                 response_set.append(valid_url[0])
     response= ''
     for each_url in set(response_set):
         response = "%s<p>%s</p>"%(response,each_url)
     #response
     return HttpResponse(response)

