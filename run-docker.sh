set -e
docker build -t dexy/simple-repro-demo .
docker run -t -i \
    -v `pwd`/content:/home/repro/content \
    dexy/simple-repro-demo /bin/bash
