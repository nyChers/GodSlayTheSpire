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
    data = s
    pos = []
    for i in range(len(data)):
        if data[i] == "'":
            pos.append(i)
    redata = data[:pos[0]] + "\\u0027" + data[pos[0] + 1:pos[1]] + "\\u0027" + data[pos[1] + 1:pos[
        2]] + "\\u0027" + data[pos[2] + 1:pos[3]] + "\\u0027" + data[pos[3] + 1:]

    return base64.b64encode(xorWithKey(bytes(redata, encoding='utf-8'), bytes(key, encoding='utf-8')))