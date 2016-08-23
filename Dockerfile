FROM ddidier/sphinx-doc:latest

MAINTAINER DevOps-ProfessionalServices-UK@rackspace.com

# Our parent Dockerfile sets the user to 'sphinx-doc', so we must `sudo` in this file

RUN sudo apt-get update

RUN DEBIAN_FRONTEND=noninteractive sudo apt-get install -y --no-install-recommends \
    python-pip python-dev build-essential g++ \
    libcairo2-dev libjpeg62-turbo-dev libpango1.0-dev libgif-dev \
    texlive texlive-latex-recommended texlive-latex-extra texlive-pstricks \
    texlive-fonts-recommended texlive-fonts-extra \
    fonts-dejavu fonts-liberation ttf-mscorefonts-installer \
    && sudo apt-get autoremove -y \
    && sudo rm -rf /var/cache/* \
    && sudo rm -rf /var/lib/apt/lists/*

ENV DOC_DIR /doc

COPY requirements.txt $DOC_DIR/requirements.txt
RUN sudo pip install -r $DOC_DIR/requirements.txt
