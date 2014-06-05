set -e
docker build -t repro/dexy .
docker run -t -i \
    -v `pwd`/content:/home/repro/ \
    repro/dexy /bin/bash
