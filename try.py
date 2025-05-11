from serpapi import GoogleSearch
params = {
"engine": "google",
"q": "Is there any popular recommendation for commuter car choice",
"api_key": "c18bc6ba16a4fa7599247699d5831030442f4a93a298dcf4a1aae1612b46a648",
"start": 30
}

# s = serpapi.search(q="Is there any popular recommendation for printer choice", engine="google", location="Austin, Texas", hl="en", gl="us")
# organic_results = s["organic_results"]
search =GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]
# write organic results to json file
import json
with open('4.json', 'w') as f:
    json.dump(organic_results, f, indent=4)