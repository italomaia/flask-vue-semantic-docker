FROM node:8

ENV USR node
ENV HOME /home/$USR

COPY . .
RUN chown -R 1000:1000 .

WORKDIR $HOME
USER $USR
RUN mkdir dist
RUN yarn --non-interactive --no-progress --no-lockfile && yarn cache clean