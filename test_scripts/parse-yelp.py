import urllib.request

# https://api.yelp.com/v3/autocomplete?text=del&latitude=37.786882&longitude=-122.399972

def getJson():
    
    url="https://api.yelp.com/v3/businesses/search"
    
    sk="YOUR_KEY"
	

# 	startTime = startTime.replace(' ','')
    urlcomplete =  url + "/" + sk + "/"
	
	#open URL 
    webURL = urllib.request.urlopen(urlcomplete)
    
    if (webURL.getcode() == 200):
        data = webURL.read()
        str_response = data.decode('utf-8')
        obj = json.loads(str_response)
        return obj
    else:
        print("Error: %d" % webURL.getcode())
        return None

print getJson()