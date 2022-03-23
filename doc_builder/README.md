# doc_builder

Builds API documentation for an OpenAPI schema.

This example assumes you have Docker installed.

## Explanation

The build process for the documentation is split into five stages:

* prep
* fetch
* convert
* build
* cleanup

To ensure the build pipeline runs on any machine, each stage is run in a Docker container. The prep stage builds the images that will be used by the fetch, convert, and build stages.

The fetch stage downloads the petstore OpenAPI schema that will be used by this example and pretty prints it to the file petstore3.json with jq.

The convert step uses the widdershins npm package convert the petstore3.json file to markdown that can be consumed by slate.

The build stage uses the slate Ruby package to generate the documentation. Slate uses middleman to build the docs is picky about filesystem structure, so the working directory needs to be set as the directory with Slate's boilerplate code. The name of the markdown file also needs to be changed to index.html.md. The build docs are then extracted and exposed to the file system on the host machine through the bind directory /app.

Finally, the cleanup step remove the Docker images created for each stage so as to not take up extra disk space and provide clean images each time.

Notice how most of the heavy lifting is shifted to the Dockerfiles associated with each step. This encapsulates the setup and applications needed for each stage in the Dockerfile, and the build_docs.yaml Config File only contains the commands needed for building the docs. This also has the advantage that if wget, jq, widdershins, and slate are installed on the host machine, the Config File can be easily modified to use the local command runner without having to modify the executed commands.
