cd .devcontainer
# Run the new compose (containers are not created before)
docker compose -f ./.devcontainer/docker-compose.yml -p tcp up

# Run the exist compose
docker compose start && docker compose logs -f# docker_compose_tcp_example
