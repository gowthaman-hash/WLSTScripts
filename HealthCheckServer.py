connect('devadmin','devadmin123',
 url='http://aw-lx0024:28000')
stoppedServers = [] 
servers = cmo.getServers() 
for server in servers:
 try:
     serverRuntime()
     currentState = get('HealthState').getState()
     if currentState == 0:
        print server.getName() + ': ' + get('State') + ': HEALTH_OK'
     elif currentState == 1:
        print server.getName() + ': ' + get('State') + ': HEALTH_WARN'
     elif currentState == 2:
        print server.getName() + ': ' + get('State') + ': HEALTH_CRITICAL'
        stoppedServers.append(server.getName())
     elif currentState == 3:
        print server.getName() + ': ' + get('State') + ': HEALTH_FAILED'
        stoppedServers.append(server.getName())
     elif currentState == 4:
        print server.getName() + ': ' + get('State') + ': HEALTH_OVERLOADED'
     else:
        print server.getName() + ': ' + get('State') + ': UNKNOWN HEALTH STATE (' + currentState + ')'
        
 except WLSTException, e:
	print server.getName() + " is not running."
	stoppedServers.append(server.getName())

disconnect()

if stoppedServers: 
	print "Found stopped servers first one is " + stoppedServers[0] 
else:
	print "All Ok"