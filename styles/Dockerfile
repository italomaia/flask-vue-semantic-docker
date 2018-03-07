FROM node:9-slim

ENV USR node
ENV HOME /home/${USR}

RUN yarn global add gulp --non-interactive --no-progress --no-lockfile && \
  yarn cache clean --force

USER ${USR}
WORKDIR ${HOME}

COPY --chown=node:node . .
RUN chmod +x entrypoint.sh

RUN yarn add semantic-ui --ignore-scripts --non-interactive --no-progress --no-lockfile && \
  yarn cache clean --force