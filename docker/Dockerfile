FROM whyour/qinglong:2.17
COPY ./qldepinstall.sh /tmp/qldepinstall.sh
COPY ./qlpreinitrepo.sh /tmp/qlpreinitrepo.sh
RUN chmod +x /tmp/qldepinstall.sh && \
  /tmp/qldepinstall.sh && \
  chmod +x /tmp/qlpreinitrepo.sh && \
  /tmp/qlpreinitrepo.sh
