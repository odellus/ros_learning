#! /usr/bin/env python3
# -*- coding: utf-8

import json

def serialize(obj, fname):
    with open(fname, 'w') as f:
        json.dump(obj, f)

def deserialize(fname):
    with open(fname, 'r') as f:
        return json.load(f)

fname = 'custom_packages_and_more.json'
d = deserialize(fname)

print(d.keys())
prefixes = [x[1] for x in d['commonly_occuring_prefixes']]

custom = d['custom']

families = {}
for pkg in custom:
    prefix = pkg.split('_')[0]
    if prefix not in families:
        families[prefix] = [pkg]
    else:
        families[prefix].append(pkg)

d['packages_by_prefix'] = families

serialize(d, fname)
