import  os, requests
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
familybotid = "a2dc0da36676eec3febf7df4de"
funguys = "db6fba2dad56160da5223dcdf0"
 
def groupmesend(botid, message2group):
	website = "https://api.groupme.com/v3/bots/post"
	botparams = {
		"bot_id"  : botid,
		"text"    : message2group
	}
	requests.post(website, data = botparams)

@app.route('/')
def hello():
	return "Hello World!"


@app.route('/family', methods=['POST'])
def family():
	#groupmesend(familybotid, "No one cares")
	messageData = request.data
	boom = json.loads(messageData)
	if "hello" in boom['text'].lower():
		groupmesend(familybotid, "No one cares")

@app.route('/highlands', methods=['POST'])
def highlands():
	bot_name = "Fun Guy Locator"
	messageData = request.data
	boom = json.loads(messageData)
	poster = boom['name']
	messagetext = boom['text'].lower()
	if poster != bot_name:
		if "where are" in boom['text'].lower():
			groupmesend(funguys, "We're in the Highlands")
		elif "drew" in boom['text'].lower():
			 groupmesend(funguys, "Drew is nowhere to be found, unfortunately!")
		if  boom['text'] is []:
                        groupmesend(funguys, "You Most Likely Just Got Haid!!")
					
 
