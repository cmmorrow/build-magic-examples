# docker_app

Builds a Docker image in a virtual machine.

This example assumes you have Vagrant installed.

## Explanation

This example uses the Vagrant runner and the Alpine Linux Vagrant Box, as defined in the Vagrantfile. The docker and curl packages are installed and Docker is started. Next, the Docker image is built from the Dockerfile.

The Dockerfile is available in the virtual machine by setting the working directory and bind directory to /app. By doing this, the Vagrantfile is updated on the fly to include `config.vm.synced_folder ".", "/app"` which syncs the current directory on the host machine with the /app directory in the virtual machine.

Next, the Docker image is run and curl is used to call the web service running the Docker container. If the response from the container is what's expected by the test, it passes and we know the image for our web service was built correctly. The image is then tagged and pushed to an image repository on AWS.
