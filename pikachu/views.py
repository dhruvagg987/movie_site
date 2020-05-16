from django.shortcuts import render

def home(request):
    import requests
    import json
    
    
    api_request= requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=5d7a2a12")
    # api_request= requests.get("http://www.omdbapi.com/?s="+"Guardians of the Galaxy Vol. 2"+"&apikey=e8ac2654")
    api=json.loads(api_request.content)

    api1_request= requests.get("http://www.omdbapi.com/?i=tt0468569&apikey=e8ac2654")
    api1=json.loads(api1_request.content)
    api2_request= requests.get("http://www.omdbapi.com/?i=tt0167260&apikey=e8ac2654")
    api2=json.loads(api2_request.content)
    api3_request= requests.get("http://www.omdbapi.com/?i=tt7476494&apikey=e8ac2654")
    api3=json.loads(api3_request.content)

    return render(request, 'home.html',{ 'api':api , 'api1':api1, 'api2':api2, 'api3':api3 })

def lookup(request):

    if request.method == 'POST':
        import requests
        import json
        # q="Guardians of the Galaxy Vol. 2"
        movies = request.POST['movief']
        movie_request = requests.get("http://www.omdbapi.com/?s="+movies+"&apikey=e8ac2654")
        # print(movies.imdbID)
        movie = json.loads(movie_request.content)
        print(movie)
        # return render(request,'lookup.html',{'movie':movie})
        return render(request,'lookup.html',{'movie':movie})
    else:
        return render(request,'lookup.html',{})