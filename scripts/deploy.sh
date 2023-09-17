#!/bin/bash

remote_server="catri.us"
remote_user="ec2-user"
remote_directory="/home/ec2-user/catrius_blog_2"

commands=()
commands+=("cd '$remote_directory'")
commands+=("git pull")
commands+=("poetry install")
commands+=("poetry run python manage.py migrate")
commands+=("sudo systemctl restart gunicorn")
commands+=("echo done")

for command in "${commands[@]}"; do
  joined_commands+=" $command &&"
done

joined_commands=${joined_commands%&&}

ssh_command="ssh '$remote_user@$remote_server'"
eval "$ssh_command '$joined_commands'"
