cd .devcontainer
docker compose -f ./.devcontainer/docker-compose.yml -p tcp up

docker compose start && docker compose logs -f# docker_compose_tcp_example
