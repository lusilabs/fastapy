import time


def runTask():
	time.sleep(5) # simulate long running task
	return {'group_name': 'job complete!'}

def anotherJob(name, kwarg1=None):
	time.sleep(5)
	return {'result': name, 'kwargs': kwarg1}
