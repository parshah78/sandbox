#!/usr/local/bin/python3

import json
import codecs
import re

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

data = []

with codecs.open('/Users/parshah/Development/python/sandbox/metrics/uniquemetrics.json','rU','utf-8') as f:
    for line in f:
       line = line.rstrip('\n')
       data.append(flatten_json(json.loads(line)))

srtdata = sorted(data, key=lambda k: k['type'])

for idx in range(len(srtdata)):
	svrtype = srtdata[idx]['type'].lower()
	metric = srtdata[idx]['met'].lower()
	feature = srtdata[idx]['feat'].lower()
	for key in srtdata[idx]:
		if re.match("val\..+", key):
			val1 = re.match("val\.(.+)", key)
			print('{ "type": "path", "name": "%s.%s.%s.%s", "expr": "$.message.%s" },' % (svrtype, metric, feature, val1.group(1).lower(), key))

