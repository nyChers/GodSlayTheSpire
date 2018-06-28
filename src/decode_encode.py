#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  NingYu Zhang
# @Date:    Created on 2018/6/27 19:03

import base64

def xorWithKey(b,key):
    pass
    res = bytearray()
    for i in range(len(b)):
        res.append(b[i] ^ key[i % len(key)])
    return res


def decode(s, key):
    return xorWithKey(base64.b64decode(s), bytes(key, encoding='utf-8'))


def encode(s, key):
    return base64.b64encode(xorWithKey(bytes(s, encoding='utf-8'), bytes(key, encoding='utf-8')))