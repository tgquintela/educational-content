FROM kaggle/python:latest
LABEL mantainer "tgquintela"

#ADD data/. home/user/input/.
#VOLUME ~/data /working
RUN mkdir /working
WORKDIR /working

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888
CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0"]
