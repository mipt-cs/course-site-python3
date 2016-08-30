#!/bin/env python3
import os
import subprocess
import sys
import shutil
import tabulate

checker_path = os.path.dirname(os.path.abspath(__file__))
tests_path = os.path.join(checker_path, 'tests')
path = os.path.dirname(checker_path)
status = {}

total_problems = 0
total_programs = 0
problems_solved = 0

call = lambda args: subprocess.call(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)

program_input = os.path.join(path, 'input.txt')
program_output = os.path.join(path, 'output.txt')
for problem in os.listdir(tests_path):
    total_problems += 1
    status[problem] = {}
    program = os.path.join(path, problem+'.py')
    if os.path.isfile(program):
        total_programs += 1
        for test in os.listdir(os.path.join(tests_path, problem)):
            if not test.endswith('.a'):
                continue
            test_name = test[:-2]
            full_test_path_in = os.path.join(tests_path, problem, test_name)
            if not os.path.isfile(full_test_path_in):
                continue
            full_test_path_out = full_test_path_in+ '.a'
            shutil.copy(full_test_path_in, program_input)
            try:
                retcode = call(['python3', program])
            except subprocess.TimeoutExpired:
                status[problem][test_name] = 'T'
                retcode = -1
                continue
            if retcode != 0:
                status[problem][test_name] = 'E'
                continue
            retcode = call(['diff', '-wBq', program_output, full_test_path_out])
            status[problem][test_name] = '+' if retcode == 0 else '-'
        if len(list(filter(lambda x: x in ['T', 'E', '-'], status[problem].values()))) == 0:
            problems_solved += 1

print('Всего задач: %d' % total_problems)
print('Отправлено решений: %d' % total_programs)
print('Правильно решено: %d' % problems_solved)
print()
for (problem, stat) in sorted(status.items()):
    if not bool(stat):
        print('%s: решение не отправлено' % problem)
    else:
        print('%s: пройдено тестов — %d/%d' % (problem, len(list(filter(lambda x: x == '+', stat.values()))), len(stat.keys())))
        print(tabulate.tabulate(list(zip(*sorted(stat.items())))))

if os.path.isfile(program_output):
    os.remove(program_output)

sys.exit(0 if problems_solved == total_problems else 1)
