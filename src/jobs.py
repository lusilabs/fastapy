import time


def runTask():
	time.sleep(5) # simulate long running task
	return {'group_name': 'job complete!'}
