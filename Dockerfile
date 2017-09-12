FROM keyi/python2-mcr2017a-rpi-isl

COPY STMBv1_0/ ./STMBv1_0
COPY example.py ./
COPY setup.py ./

RUN python-scipy