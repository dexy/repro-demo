FROM                    ubuntu:latest
MAINTAINER              Ana Nelson <ana@ananelson.com>

### "configure-apt"
RUN echo "APT::Get::Assume-Yes true;" >> /etc/apt/apt.conf.d/80custom; \
    echo "APT::Get::Quiet true;" >> /etc/apt/apt.conf.d/80custom; \
    apt-get update

### "utils"
RUN apt-get install \
        build-essential \
        curl \
        sudo \
        adduser

### "nice-things"
RUN apt-get install \
        ack-grep \
        git \ 
        rsync \
        strace \ 
        tree \ 
        unzip \
        vim \ 
        wget

### "python"
RUN apt-get install \
        python \
        python-dev \
        python-pip

### "scipy"
RUN apt-get install \
        python-scipy \
        python-matplotlib

### "latex"
RUN apt-get install \
        texlive \
        texlive-latex-extra

### "python-packages"
RUN pip install --pre \
        pygments \
        xlwt

### "dexy"
RUN pip install \
        dexy

### "create-user"
RUN useradd -m repro; \
    echo "repro:password" | chpasswd; \
    sudo echo "repro ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/docker; \
    chmod 0440 /etc/sudoers.d/docker

### "activate-user"
ENV HOME /home/repro
USER repro
WORKDIR /home/repro
