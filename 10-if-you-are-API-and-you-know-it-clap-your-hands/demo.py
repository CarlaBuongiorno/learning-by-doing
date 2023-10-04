# Requests is the module we'll be using to study web API stuff.
# It is possible to do everything with just the standard Python
# modules, but Requests makes things much easier.
import requests


# Easiest example I could find. There's a website, https://isevenapi.xyx.
# They offer "Is Number Even As A Service". It's a joke, obviously;
# who needs to call a web API to do x % 2 == 0? However, it's a
# very nice simple API to get started. The URL is:
url = 'https://api.isevenapi.xyz/api/iseven/'
# That's the location of the API method; that's where their computer
# is listening for our requests to their API. However, we haven't
# said which number we actually want to check.
# 
# So, most of that URL stays the same, but we need to add the number
# we want to check for evenness.
combined_url = f'{url}6'
# Cool. Now we need to actually talk to the server. There are few
# different verbs you can use to talk to an HTTP server, and we're
# going to start with the simplest; GET. GET, unsurprisinly, gets
# information from a web server.
r = requests.get(combined_url)
# That was is. The information from that URL is now in your program.
# Let's have a look at it.
print(r)
# The response code (200) means "OK", but that's not much use.
# Like most web APIs, Is Even returns structured JSON data,
# which Requests can turn into a Python dictionary for us:
obj = r.json()
# Great! Let's take a peek:
print(obj)
# So, we can see the answer, and... an advert? The bastards!
# Let's just index into that dictionary with the 'iseven' key
# to get just the result, and ignore the advert.
print(obj['iseven'])
# Again, a lot of work for `not x%2`, but it hopefully shows that
# calling web APIs doesn't have to be difficult. I strongly
# suggest you go to Is Even's website, and ready their documentation;
# it's super simple, but practicing reading documentation is an
# important skill. You may as well practice on the easy stuff.



# Next one! Do you want cat facts as a service? Well, we're doing
# it anyway. You can read the documentation for this API here:
    # https://github.com/wh-iterabb-it/meowfacts#description
# So, let's ask the user how many cat facts they want:
number_of_facts = input("How many cat facts do you want to know? : ")
# ...and let's store the URL of the API.
url = "https://meowfacts.herokuapp.com/"
# You can see in the documentation that this API takes its
# arguments in a slightly different way. Rather than just putting
# the number of facts on the end of the URL, it needs what's called
# a Query String - the bit at the end with a question mark, named
# parameters and values:
    # https://meowfacts.herokuapp.com/?count=3
# We could edit the URL ourselves, but Requests has a way to make
# it easier and less prone to errors:
arguments = {'count': number_of_facts, 'lang': 'esp-mx'}
r = requests.get(url, params=arguments)
# Easy as that. Now we convert the response to a Python dictionary...
obj = r.json()
# And print out all the amazing cat facts.
for fact in obj['data']:
    print(fact)

# EXERCISE
# Can you print the cat facts in Spanish? (hint: read the documentation)
