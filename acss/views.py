
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.shortcuts import render
from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer
chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
training_data_quesans = open('data/ques_ans.txt').read().splitlines()
training_data_personal = open('data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data) 
# Train based on the english corpus

#Already trained and it's supposed to be persistent
#chatbot.train("chatterbot.corpus.english")
import pyrebase
import os

config = {
    "apiKey": "AIzaSyAPurpHf0cbK1U684_Q67QHsn2f5U2Y6og",
    "authDomain": "chatbot-b7646.firebaseapp.com",
    "projectId": "chatbot-b7646",
    "storageBucket": "chatbot-b7646.appspot.com",
    "messagingSenderId": "344015977001",
    "appId": "1:344015977001:web:4af07bf5fa1cf542773a38",
    "measurementId": "G-31VCTRHECD",
    "databaseURL":"https://console.firebase.google.com/project/chatbot-b7646/database/chatbot-b7646-default-rtdb/data/~2F"
  }
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		message = data['message']

		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)



def dash(request):
    return render(request, 'home.html')
def home(request):
    return render(request, 'home1.html')

