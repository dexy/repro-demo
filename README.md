Run the `run-docker.sh` script to build and launch a Docker container with all dependencies.

Then run `cd ~ && ./run-dexy.sh` within the container to build all docs.

If you have squid-deb-proxy set up, uncomment the line in Dockerfile which enables package caching.

You only need [Docker](https://www.docker.io/) installed + a working internet
connection, everything else will be downloaded and installed in the container.
