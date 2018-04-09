# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
#
# # Train based on the english corpus
# chatbot.train("chatterbot.corpus.english")
# chatbot.train("chatterbot.corpus.chinese")

# Get a response to an input statement
print chatbot.get_response(u"你是")