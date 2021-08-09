FROM amazonlinux:2
RUN yum -y upgrade i&& yum -y install shadow-utils && useradd app
COPY stress.sh /stress.sh
USER app
CMD ["sh", "-c", "/stress.sh $TARGET"]
