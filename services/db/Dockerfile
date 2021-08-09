FROM amazonlinux:2
RUN yum -y update && yum -y install python3-pip shadow-utils && \
pip3 install cherrypy requests pymongo && \
yum clean all && useradd app && mkdir /public && chown -R app /public
COPY app.py /
USER app
EXPOSE 8080
CMD ["python3","app.py"]
