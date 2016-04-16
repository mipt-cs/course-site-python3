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
                if method == MATCH:
                    for t in matches:
                        self.assertTrue(not not re.match(getattr(module, regexp), t))
                    for t in not_matches:
                        self.assertFalse(not not re.match(getattr(module, regexp), t))
                elif method == SEARCH:
                    for (k, v) in matches.items():
                        self.assertEqual(re.search(getattr(module, regexp), k).group(), v)
            return test


        for (k,v) in clazz.TEST_DATA.items():
            setattr(clazz, 'test_' + k, gen_test(k, *v))

        return clazz
    return decorator
