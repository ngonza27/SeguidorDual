

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json
import random
import requests

AllowedActions = ['both', 'publish', 'subscribe']

# Custom MQTT message callback
def obtenerDatos(client, userdata, message):
  print("publish parameters")
  #Data value
  deviceId = "rpi4-SeguidorDual"
  voltaje = 99
  corriente = 99
  posicionX = random.randint(11,21)
  posicionZ = random.randint(11,21)
  temperatura = random.randint(45,90)
  #JSON
  data = json.dumps({ 'deviceId': deviceId, 'voltaje': voltaje, 'corriente': corriente, 'posicionX': posicionX, 'posicionZ': posicionZ, 'temperatura': temperatura })
  headers = { 'Content-Type': 'application/json'}
  #URL = 'http://192.168.0.17:3000/iot/liveData'
  #r = requests.request('POST', URL, headers=headers, data=data)
  print("Data:", data, " from rpi4 DIST")
  return data

def saveValues(client, userdata, message):
  return 0 
# string_data = message.payload.decode('utf-8')
  #json_data = json.loads(string_data)
  #print("Topic received", string_data, json_data)
  #print(json_data['ph'], json_data['conductividad'], json_data['riego'])
  #try:
    #ph = json_data['ph']
    #conductividad = json_data['conductividad']
    #riego = json_data['riego']
    #print("ppm: {}, conductividad: {}, riego: {}".format(ph, conductividad, riego))
    #con = DB.sql_connection()
    #DB.addData(con,ph,conductividad,riego)
    #global tiempoRiego
    #tiempoRiego = riego
    #print("GUARDO LA INFORMACION")
    #print(DB.getAllDB())
  #except:
    #print("No relevant data was sent")


def defaultCallback(client, userdata, message):
  print("Data:", message.payload, " from", message.topic)


# Read in command-line parameters
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host", help="a28yobe9j1e4my-ats.iot.us-east-2.amazonaws.com")
parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="x509")
parser.add_argument("-c", "--cert", action="store", dest="certificatePath", help="crt")
parser.add_argument("-k", "--key", action="store", dest="privateKeyPath", help="private")
parser.add_argument("-p", "--port", action="store", dest="port", type=int, help="Port number override")
parser.add_argument("-w", "--websocket", action="store_true", dest="useWebsocket", default=False,
                    help="Use MQTT over WebSocket")
parser.add_argument("-id", "--clientId", action="store", dest="clientId", default="basicPubSub",
                    help="Targeted client id")
parser.add_argument("-t", "--topic", action="store", dest="topic", default="sdk/test/Python", help="Targeted topic")
parser.add_argument("-t1", "--topic1", action="store", dest="topic1", default="topic/obtenerDatos", help="Target topic1")
parser.add_argument("-t2", "--topic2", action="store", dest="topic2", default="topic/saveValues", help="Target topic2")
parser.add_argument("-m", "--mode", action="store", dest="mode", default="both",
                    help="Operation modes: %s"%str(AllowedActions))
parser.add_argument("-M", "--message", action="store", dest="message", default="Hello World!",
                    help="Message to publish")

args = parser.parse_args()
host = args.host
rootCAPath = args.rootCAPath
certificatePath = args.certificatePath
privateKeyPath = args.privateKeyPath
port = args.port
useWebsocket = args.useWebsocket
clientId = args.clientId
topic = args.topic
topic1 = args.topic1
topic2 = args.topic2

if args.mode not in AllowedActions:
    parser.error("Unknown --mode option %s. Must be one of %s" % (args.mode, str(AllowedActions)))
    exit(2)

if args.useWebsocket and args.certificatePath and args.privateKeyPath:
    parser.error("X.509 cert authentication and WebSocket are mutual exclusive. Please pick one.")
    exit(2)

if not args.useWebsocket and (not args.certificatePath or not args.privateKeyPath):
    parser.error("Missing credentials for authentication.")
    exit(2)

# Port defaults
if args.useWebsocket and not args.port:  # When no port override for WebSocket, default to 443
    port = 443
if not args.useWebsocket and not args.port:  # When no port override for non-WebSocket, default to 8883
    port = 8883

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
if useWebsocket:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath)
else:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
if args.mode == 'both' or args.mode == 'subscribe':
    myAWSIoTMQTTClient.subscribe(topic, 1, defaultCallback)
    myAWSIoTMQTTClient.subscribe(topic1, 1, obtenerDatos)
    myAWSIoTMQTTClient.subscribe(topic2, 1, saveValues)
time.sleep(5)

# Publish to the same topic in a loop forever
loopCount = 0
timeStart = time.time()/60
#con = DB.sql_connection()
tiempoObtenerBD = 10
while True:
	timeNow = time.time()/60
	if args.mode == 'both' or args.mode == 'publish':
		print(timeStart , timeNow)
		if (timeStart - timeNow) % tiempoObtenerBD == 0:
			print('!!!!!!')
			print("REGANDO PLANTAS")
		#if (timeStart - timeNow) % 1 == 0:
		##python_object will contain the sensors data
		#python_object = {'Device Id': 'raspberryPi4','time': time.time(),'Temperature': random.randint(0,10) }
		#json_string = json.dumps(python_object)
		datosPanel = obtenerDatos(1,1,1)
		#Mandar la informacion recolectada de los sensores...
		try:
			myAWSIoTMQTTClient.publish(topic1, datosPanel, 1)
		except:
			myAWSIoTMQTTClient.connect()
			time.sleep(10)
			myAWSIoTMQTTClient.publish(topic1, datosPanel, 1)
		if args.mode == 'publish':
			print('Published topic %s: %s\n' % (topic1, json_string))
		loopCount += 1
	time.sleep(5)
