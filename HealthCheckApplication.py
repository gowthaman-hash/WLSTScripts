connect('devadmin','devadmin123',
 url='http://aw-lx0024:28000')
myapps=cmo.getAppDeployments()
outputbuffer=[]
outputbuffer.append("--"*40)
outputbuffer.append(" \t\t\tAPPLICATION STATUS WEBLOGIC\t\t")
outputbuffer.append("--"*40)
outputbuffer.append (" %-50s%20s" %("APPLICATION NAME","STATUS"))
outputbuffer.append("--"*40)
for app in myapps:        
	domainConfig()        
	bean=getMBean('/AppDeployments/'+app.getName()+'/Targets/')        
	targetsbean=bean.getTargets()       
	domainRuntime()
	cd('AppRuntimeStateRuntime')      
	cd('AppRuntimeStateRuntime')  
	for target in targetsbean:    
	 domainRuntime()     
	 appstatus=cmo.getCurrentState(app.getName(),target.getName())
	 outputbuffer.append(" %-50s%20s" %(app.getName(),appstatus))
	 serverConfig()
	 outputbuffer.append("--"*40)
	 print (outputbuffer)
