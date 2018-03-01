FROM node:9-slim

ENV USR node
ENV HOME /home/$USR

RUN yarn global add gulp --non-interactive --no-progress --no-lockfile && \
  yarn cache clean --force

WORKDIR $HOME

COPY --chown=1000:1000 . .
RUN chmod +x entrypoint.sh

USER $USR
RUN yarn add semantic-ui --ignore-scripts --non-interactive --no-progress --no-lockfile && \
  yarn cache clean --force