set -e
docker build -t repro/dexy .
docker run -t -i repro/dexy /bin/bash
