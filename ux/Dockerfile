FROM node:9

ENV USR node
ENV HOME /home/$USR

WORKDIR $HOME
COPY --chown=1000:1000 . .
RUN chmod +x entrypoint.sh

USER $USR
RUN yarn --non-interactive --no-progress --no-lockfile && \
  yarn cache clean
