#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

from mysql import MySQL
from sqlserver import MSSQL
import util
import datetime, time

def main():
	#获取当前的月份
	last_month = firstday_of_last_month()
	suffix = '%d%02d'%(last_month.year, last_month.month)
	handler(suffix, 'MYSQL')
	handler(suffix, 'SQLSERVER')

def handler(suffix, type):
	#判断数据库是否存在
	table1 = 'tbl_live_data'
	if table_exists(table1, suffix, type) == 0:
		#迁移数据
		migrate_table_data(table1, suffix, type)
		#清理数据
		clean_table_data(table1, suffix, type)
	table2 = 'tbl_live_data_sites'
	if table_exists(table2, suffix, type) == 0:
		#迁移数据
		migrate_table_data(table2, suffix, type)
		#清理数据
		clean_table_data(table2, suffix, type)

def table_exists(table, suffix, type):
	result = 0
	table_name = table + "_" + suffix
	if type == 'MYSQL':
		ms = init_db(type)
		sql = "select table_name from information_schema.TABLES WHERE table_name ='%s'" % (table_name, )
		rs = ms.executeQuery(sql)
		if len(rs) > 0:
			result = 1
	elif type == 'SQLSERVER':
		ms = init_db(type)
		sql = "select * from sys.tables where name='%s' and type = 'u'" % (table_name, )
		rs = ms.executeQuery(sql)
		if len(rs) > 0:
			result = 1
	return result

def firstday_of_last_month():
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1
    res = datetime.datetime(year, month, 1)
    return res

def migrate_table_data(table, suffix, type):
	where = suffix[:4] + '-' + suffix[4:]
	ms = init_db(type)
	if type == 'MYSQL':
		sql = "CREATE TABLE %s_%s SELECT * FROM %s WHERE time_point LIKE '%s-%%'" % (table, suffix, table, where)
		ms.executeUpdate(sql)
	elif type == 'SQLSERVER':
		sql = "SELECT * INTO %s_%s FROM %s WHERE time_point LIKE '%s-%%'" % (table, suffix, table, where)
		ms.executeUpdate(sql)

def clean_table_data(table, suffix, type):
	where = suffix[:4] + '-' + suffix[4:]
	ms = init_db(type)
	if type == 'MYSQL':
		sql = "DELETE FROM %s WHERE time_point LIKE '%s-%%'" % (table, where)
		ms.executeUpdate(sql)
	elif type == 'SQLSERVER':
		sql = "DELETE FROM %s WHERE time_point LIKE '%s-%%'" % (table, where)
		ms.executeUpdate(sql)
	
def init_db(type):
	result = None
	if type == 'MYSQL':
		host = util.read_config('MYSQL', 'host')
		port = int(util.read_config('MYSQL', 'port'))
		user = util.read_config('MYSQL', 'username')
		password = util.read_config('MYSQL', 'password')
		database = util.read_config('MYSQL', 'database')
		result = MySQL(host=host, port=port, user=user, password=password, database=database)
	elif type == 'SQLSERVER':
		host = util.read_config('SQLSERVER', 'host')
		user = util.read_config('SQLSERVER', 'username')
		password = util.read_config('SQLSERVER', 'password')
		database = util.read_config('SQLSERVER', 'database')
		result = MSSQL(host=host, user=user, password=password, database=database)
	return result

if __name__ == '__main__':
	main()