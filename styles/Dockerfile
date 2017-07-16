FROM node:8-slim

ENV USR node
ENV HOME /home/$USR

RUN yarn global add gulp --non-interactive --no-progress --no-lockfile && \
  yarn cache clean --force

WORKDIR $HOME

COPY . .
RUN chmod +x entrypoint.sh
RUN chown -R 1000:1000 .

USER $USR
RUN yarn add semantic-ui --ignore-scripts --non-interactive --no-progress --no-lockfile && \
  yarn cache clean --force