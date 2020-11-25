FROM continuumio/anaconda3

# update conda packages
RUN conda update --yes --all

# install requirements
ADD ./.devcontainer/conda-requirements.txt /tmp/
RUN conda install --force-reinstall --yes --file /tmp/conda-requirements.txt
