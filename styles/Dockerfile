FROM node:8-slim

ENV USR node
ENV HOME /home/$USR

RUN yarn global add gulp --non-interactive --no-progress --no-lockfile && \
  yarn cache clean --force

COPY . .
RUN mkdir dist && chown -R 1000:1000 .

WORKDIR $HOME
USER $USR

RUN yarn install semantic-ui --ignore-scripts --non-interactive --no-progress --no-lockfile && \
  yarn cache clean --force