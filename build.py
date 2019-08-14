import docker

client = docker.from_env()

client.images.build(path=".",tag="ggbr12/php-apache-dev:1.0.1")
client.images.push(repository="ggbr12/php-apache-dev", tag="1.0.1")