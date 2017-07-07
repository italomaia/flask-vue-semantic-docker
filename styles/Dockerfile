FROM node:8-slim

ENV USR node
ENV HOME /home/$USR

RUN yarn global add gulp --non-interactive --no-progress --no-lockfile && yarn cache clean

WORKDIR $HOME
USER $USR
RUN yarn add semantic-ui --non-interactive --no-progress --no-lockfile && yarn cache clean