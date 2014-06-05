FROM       ubuntu:14.04
MAINTAINER Ana Nelson <ana@ananelson.com>

RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :
ENV DEBIAN_FRONTEND noninteractive

# Use squid deb proxy as per https://gist.github.com/dergachev/8441335
# Uncomment this line if squid-deb-proxy configured on host.
# RUN /sbin/ip route | awk '/default/ { print "Acquire::http::Proxy \"http://"$3":8000\";" }' > /etc/apt/apt.conf.d/30proxy

RUN apt-get update

# Install system utils.
RUN apt-get install -y build-essential
RUN apt-get install -y adduser
RUN apt-get install -y curl
RUN apt-get install -y sudo

# Install nice things to have.
RUN apt-get install -y ack-grep
RUN apt-get install -y strace
RUN apt-get install -y vim

# Install Python
RUN apt-get install -y python
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip

# Install Scipy (includes numpy) and Matplotlib
RUN apt-get install -y python-scipy
RUN apt-get install -y python-matplotlib

# Install LaTeX
RUN apt-get install -y texlive
RUN apt-get install -y --no-install-recommends texlive-latex-extra

RUN pip install dexy

# Create a user
RUN useradd -m -p $(perl -e'print crypt("foobarbaz", "aa")') repro
RUN adduser repro sudo

ENV HOME /home/repro

USER repro

ADD content/ /home/repro/
