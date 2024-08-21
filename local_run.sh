#!/bin/bash
docker build . -t marcelormergulhao/simple_echo_app:latest
docker run -p5000:5000 --env my_env=my_value marcelormergulhao/simple_echo_app:latest