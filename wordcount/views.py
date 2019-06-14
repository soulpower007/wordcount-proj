from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext =request.GET['fulltext']

    wordlist=fulltext.split()
    #splits fulltext into a list of the words inside fulltext
    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #increase value
            worddictionary[word]+=1
        else:
            #add the word to the worddictionary
            worddictionary[word]=1

            sw=sorted(worddictionary.items(),key=operator.itemgetter(1), reverse= True)
    return render(request, 'count.html',{'fulltext':fulltext, 'score':len(wordlist), 'wd':sw})
