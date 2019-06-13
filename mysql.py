#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import MySQLdb

class MySQL():
	def __init__(self, host, port, user, password, database):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.database = database

	def __getConnect(self):
		if not self.database:
			raise(NameError, "未指定需要连接的数据库名称")
		self.connection = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.database, use_unicode=True, charset='utf8')
		cur = self.connection.cursor()
		if not cur:
			raise(NameError, "连接数据库失败")
		else:
			return cur

	def executeUpdate(self, sql):
		cur2 = self.__getConnect()
		cur2.execute(sql)
		self.connection.commit()
		cur2.close()
		self.connection.close()
	
	def executeQuery(self, sql):
		cur1 = self.__getConnect()
		aa = cur1.execute(sql)
		resList = cur1.fetchmany(aa)
		cur1.close()
		self.connection.close()
		return resList