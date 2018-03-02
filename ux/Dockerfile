FROM node:9

ENV USR node
ENV HOME /home/${USR}
ENV PROJECT_DIR ${HOME}/code

# make sure project_dir exists before moving into it
USER $USR
RUN mkdir ${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}
COPY --chown=1000:1000 . .
RUN chmod +x entrypoint.sh

RUN yarn --non-interactive --no-progress --no-lockfile && \
  yarn cache clean
