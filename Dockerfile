FROM ubuntu
MAINTAINER zengjing@szboanda.net
RUN apt-get update \
	&& apt-get -y dist-upgrade \
	&& apt-get install -y python2.7-dev python-pip  \
	&& apt-get install -y libmysqlclient-dev \ 
	&& pip install MySQL \ 
	&& pip install pymssql \
	&& apt-get clean      \
 	&& apt-get autoclean  \
 	&& mkdir -p /usr/local/aqi \
 	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD config.ini /usr/local/aqi/
ADD main.py /usr/local/aqi/
ADD util.py /usr/local/aqi/
ADD mysql.py /usr/local/aqi/
ADD sqlserver.py /usr/local/aqi/
CMD ["python", "/usr/local/aqi/main.py"]