FROM node:8

ENV USR node
ENV HOME /home/$USR

WORKDIR $HOME
COPY . .
RUN mkdir -p dist && chown -R 1000:1000 .

USER $USR
RUN yarn --non-interactive --no-progress --no-lockfile && \
  yarn cache clean
