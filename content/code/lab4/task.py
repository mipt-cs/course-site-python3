import robot
r = robot.rmap()
r.lm('task1')

def task():
	r.rt()
	r.res.config(text='Done')

r.start(task)

