FROM debian:buster-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion && \
    apt-get clean

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh -O /tmp/anaconda-installer.sh
#COPY .devcontainer/Anaconda3-2020.11-Linux-x86_64.sh /tmp/

RUN cp /tmp/Anaconda3-2020.11-Linux-x86_64.sh /tmp/anaconda-installer.sh && \
    /bin/bash /tmp/anaconda-installer.sh -b -p /opt/conda && \
    rm /tmp/anaconda-installer.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

CMD [ "conda init" ]

# update conda packages
RUN conda update --yes --all

# install requirements
ADD ./.devcontainer/conda-requirements.txt /tmp/
RUN conda install --force-reinstall --yes --file /tmp/conda-requirements.txt
