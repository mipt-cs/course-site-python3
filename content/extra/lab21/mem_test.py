#!/bin/env python3

import objgraph


a = list(range(10))

objgraph.show_refs([a], filename='python_memory_layout.dot')
 

