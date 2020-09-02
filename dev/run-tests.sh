#!/bin/sh

DC="docker-compose -f dev/docker-compose.dev.yml"

$DC up --build --detach
$DC exec -T backend dev/wait.sh writer 9011
$DC exec -T backend dev/wait.sh reader 9010
$DC exec -T backend pytest --cov
$DC down --volumes
