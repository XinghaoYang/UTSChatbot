from rasa.core.channels.socketio import SocketIOInput
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig
#from MyIo import RestInput

action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
nlu_interpreter = RasaNLUInterpreter('/data/xingyang/Documents/Hangzhou Dianzi University - Chatbot/capstone-master/models/20190717-114901/nlu')
agent = Agent.load('/data/xingyang/Documents/Hangzhou Dianzi University - Chatbot/capstone-master/models/20190717-114901/core', interpreter=nlu_interpreter, action_endpoint=action_endpoint)
#input_channel = RestInput()

input_channel = SocketIOInput(
            # event name for messages sent from the user
            user_message_evt="user_uttered",
            # event name for messages sent from the bot
            bot_message_evt="bot_uttered",
            # socket.io namespace to use for the messages
            namespace=None
    )
    
#s = agent.handle_channels([input_channel],5005, serve_forever=True)
agent.handle_channels([input_channel], http_port=5005,route="/webhooks/",cors="*")
