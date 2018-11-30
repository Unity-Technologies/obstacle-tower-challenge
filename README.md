# Obstacle Tower Challenge Starter Kit

## Setup

* **Docker** https://www.docker.com/products/docker-desktop
* **repo2docker**

```
pip install crowdai-repo2docker
```

## Build Docker image

```
./build.sh
```

## Run Docker image

```
# Start the docker image, which will run Jupyter notebook
docker run --name obstacle_tower -it obstacle_tower_challenge:latest

# In another terminal window, execute the run.
docker exec -it obstacle_tower ./run.sh
```

## Local Run

```
./run.sh
```
