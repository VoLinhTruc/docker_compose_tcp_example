FROM ghcr.io/volinhtruc/bico_ubuntu:22.04_0.0.0

ENV DOCKER_GID=999

# ENV http_proxy=http://$MY_PROXY_IP:$MY_PROXY_PORT
# ENV https_proxy=http://$MY_PROXY_IP:$MY_PROXY_PORT

# Copy and set up entrypoint script (relative to .devcontainer/)
COPY entrypoint.sh /entrypoint.sh
RUN sudo chmod +x /entrypoint.sh

CMD ["/entrypoint.sh", "bash"]