FROM node:9

ENV USR node
ENV HOME /home/$USR

WORKDIR $HOME
COPY . .
RUN chmod +x entrypoint.sh
RUN chown -R 1000:1000 .

USER $USR
RUN yarn --non-interactive --no-progress --no-lockfile && \
  yarn cache clean
