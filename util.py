#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import ConfigParser, os

def read_config(section, key):
	cur_path = os.path.dirname(os.path.realpath(__file__))
	ini_path = cur_path + os.sep + "config.ini"
	config = ConfigParser.ConfigParser()
	f = open(ini_path)
	config.readfp(f)
	v = config.get(section, key)
	f.close()
	return v
