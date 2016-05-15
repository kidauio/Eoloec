import urllib2
import json

def main():
	#to find username go to  FB page, copy the end of URL 
	#e.g. http://facebook.com/walmart, walmart is the username
	list_companies = ["walmart", "cisco", "pepsi", "facebook"]
	graph_url = "http://graph.facebook.com/"

import urllib2
import json
 
def main():
    #to find username go to  FB page, copy the end of URL 
    #e.g. http://facebook.com/walmart, walmart is the username
    list_companies = ["walmart", "cisco", "pepsi", "facebook"]
    graph_url = "http://graph.facebook.com/"
    for company in list_companies:
		#make graph api url with company username
		current_page = graph_url + company
		
		#open public page in facebook graph api
		web_response = urllib2.urlopen(current_page)
		readable_page = web_response.read()
		json_fbpage = json.loads(readable_page)

		#print page data to console
		print company + " page"
		print json_fbpage["id"]
		print json_fbpage["likes"]
		print json_fbpage["talking_about_count"]
		print json_fbpage["username"]
		print "            "

if __name__ == "__main__":
	main()    