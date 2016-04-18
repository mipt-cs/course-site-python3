#!/usr/bin/env python3

import re

MATCH = 'match'
SEARCH = 'search'
FINDALL = 'findall'
SUB = 'sub'

def regexp_test(module):
    def decorator(clazz):
        def gen_test(regexp, method, matches, not_matches=None):
            def test(self):
                _regexp = re.compile(getattr(module, regexp))
                if method == SUB:
                    _repl = getattr(module, regexp + '_REPL')
                if method == MATCH:
                    for t in matches:
                        self.assertTrue(not not _regexp.match(t))
                    for t in not_matches:
                        self.assertFalse(not not _regexp.match(t))
                elif method == SEARCH:
                    for (k, v) in matches.items():
                        self.assertEqual(v, _regexp.search(k).group())
                elif method == FINDALL:
                    for (k, v) in matches.items():
                        self.assertEqual(v, _regexp.findall(k))
                elif method == SUB:
                    for (k, v) in matches.items():
                        self.assertEqual(v, _regexp.sub(_repl, k))
                else:
                    raise Exception("Unknown re method")
            return test


        for (k,v) in clazz.TEST_DATA.items():
            setattr(clazz, 'test_' + k, gen_test(k, *v))

        return clazz
    return decorator
