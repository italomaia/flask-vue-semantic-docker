# What is this?

Setting up **docker** + **nginx** + **flask** + **vue** + **semantic** is hardly an easy task if you want to setup production and development environments. This is my attempt
in the matter. Notice that, some containers are not complete (ux)
because, well, vue does not have a non interactive install.

## Getting started

```bash
# make sure you have fabric3 installed
# make sure to read each folder readme
# make sure you have docker and docker-compose installed

# call setup to install dependencies
fab setup

# now you're ready to go
fab env:dev up  # docker-compose up in development mode
fab env:prd up  # docker-compose up in production mode
fab env:dev build  # docker-compose build in development mode
fab env:prd build  # docker-compose build in production mode
fab env:dev on:<service_name> run:"<command>"  # docker-compose run in development mode
fab env:prd on:<service_name> run:"<command>"  # docker-compose run in production mode
fab env:dev logs:name  # docker logs on container called <name>
fab env:prd logs:name  # docker logs on container called <name>
```

You'll also have to exclude `./src/styles` from your linting, to avoid
errors. Edit `webpack.base.conf.js` like this:

```
include: [resolve('src'), resolve('test')],  // this line already exists
exclude: [resolve('src/styles')],  // add this line below
```

I'll eventually bundle the above steps into the setup, but for now,
that is not the case.

## What is what?

* app -> flask application container
* server -> nginx container
* styles -> semantic-ui container
* ux -> vuejs application container

## Trouble?

As webpack is a every-changing beast, you might have to add the following
code **to make your development environment work**:

```
# in config/index.js
dev: {
  ...
  host: '0.0.0.0',  # change host bind to 0.0.0.0
  ...
}
```

If code change in **ux** doesn't trigger app reload, change the following:

```
# in ux/config/index.js
module.exports = {
  ...
  dev: {
    ...
    poll: true,  # set it to true
    ...
  }
  ...
}
```

## Changelog

**0.2.4**

* webpack dev server endpoints have changed. Updated, so nginx can route to them.
* version bump for docker base images (node's, actually)

**0.2.3**

* Added `on:<service>` task; it is used to pick which service your command is run against. Right now, only works with `run`.

**0.2.2**

* Added adminer for dev
* Added logs command to fabfile
* Added run command to fabfile (docker-compose run)
* Small fixes

**0.2.1**

* installed extensions are now properly loaded
* added basic "auth" app implementation (for authentication)
* added some sensitive defaults for sqlalchemy configuration

**0.2**

* update to flask app dependencies (+flask-jsglue +flask-marshmallow +flask-migrate +flask-security +flask-sqlalchemy)

**0.1**

* initial version (docker + flask + vuejs + semantic-ui)
