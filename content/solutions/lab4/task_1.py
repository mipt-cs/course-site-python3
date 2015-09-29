import robot
r = robot.rmap()
r.lm('task1')

def task():
	r.up()
	r.rt()
	r.dn()
	r.rt()
	r.up()
	r.rt()
	r.dn()

r.start(task)

