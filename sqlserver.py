#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import pymssql

class MSSQL():
	def __init__(self, host, user, password, database):
		self.host = host
		self.user = user
		self.password = password
		self.database = database

	def __getConnect(self):
		if not self.database:
			raise(NameError, "未指定需要连接的数据库名称")
		self.connection = pymssql.connect(host=self.host, user=self.user, password=self.password, database=self.database, charset="utf8")
		cur = self.connection.cursor()
		if not cur:
			raise(NameError, "连接数据库失败")
		else:
			return cur

	def executeUpdate(self, sql):
		cur2 = self.__getConnect()
		cur2.execute(sql)
		self.connection.commit()
		self.connection.close()
	
	def executeQuery(self, sql):
		cur1 = self.__getConnect()
		cur1.execute(sql)
		resList = cur1.fetchall()
		self.connection.close()
		return resList

