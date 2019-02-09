# Obstacle Tower Challenge Starter Kit

This repository provides instructions for how to submit to the [Obstacle Tower Challenge](https://unity3d.com/otc).

Your goal in the Obstacle Tower is to have your agent traverse the floors of a procedurally generated tower and 
climb to the highest level possible.  Each level is progressively more difficult, and you'll be tested against a 
towers generated with random seeds your agent hasn't seen before and thus will need to generalize from the 100 
provided tower seeds.


## Local Setup for Training

Before submitting to the challenge, you will want to train an agent to advance through the Obstacle Tower.

The first step is to clone this repository:

```
git clone git@github.com:Unity-Technologies/obstacle-tower-challenge.git
```

Next, install the following dependencies:

* **Python dependencies**
```
pip install -r requirements.txt
```
* **Obstacle Tower** Download the link for your OS [here](https://github.com/Unity-Technologies/obstacle-tower-env#download-the-environment) 
  and unzip in the `obstacle-tower-challenge` folder from the cloned repository.

Finally, you can run the environment using the included agent (in `run.py`) with random actions:

```
python run.py
```

**Note:** Your Obstacle Tower build must be located at `./ObstacleTower/obstacletower.XYZ` from the base of the 
cloned repository, where `XYZ` represents the appropriate file extension for your operating system's Obstacle Tower 
build.

### Next steps

Once you've set up your environment, you'll need to train your agent.  We've provided a [guide for using Google's Dopamine
library](https://github.com/Unity-Technologies/obstacle-tower-env/blob/master/examples/gcp_training.md) to train an agent on Google Cloud Platform.


## Testing Challenge Evaluation

Before making your challenge submission, you may want to test your agent using a similar environment to the one used for the official challenge evaluation. Your agent and the Obstacle Tower environment will be run in separate Docker containers which can communicate over the local network.

### Dependencies

* **Docker** See instructions [here](https://docs.docker.com/install/)
* **aicrowd-repo2docker** 
```
pip install aicrowd-repo2docker
# or
pip install -r requirements.txt
```
* **Obstacle Tower** (same as above in "Local Setup for Training") Download the link for your OS [here](https://github.com/Unity-Technologies/obstacle-tower-env#download-the-environment) 
  and unzip in the `obstacle-tower-challenge` folder from the cloned repository.

### Build the Docker image

We've provided a build script that uses `aicrowd-repo2docker` to build an image `obstacle_tower_challenge:latest` from your repository:
```
./build.sh
```

### Run Docker image

Now that you've built a Docker image with your agent script and the Obstacle Tower environment binary, you can run both the agent and 
the environment within a separate container:
```
# Start the container running your agent script.
docker run \
  --env OTC_EVALUATION_ENABLED=true \
  --network=host \
  -it obstacle_tower_challenge:latest ./run.sh

# In another terminal window, execute the environment.
docker run \
  --env OTC_EVALUATION_ENABLED=true \
  --env OTC_DEMO_EVALUATION=true \
  --network=host \
  -it obstacle_tower_challenge:latest ./env.sh
```

The environment script should output the evaluation state as it advances:
```json
{"state":"PENDING","floor_number_avg":0.0,"reward_avg":-1.0,"episodes":[],"last_update":"2019-02-09T00:17:15Z"}
{"state":"IN_PROGRESS","floor_number_avg":0.0,"reward_avg":-1.0,"episodes":[{"state":"IN_PROGRESS","seed":101,"floor_number":0,"reward":0.0,"step_count":0}],"last_update":"2019-02-09T00:17:16Z"}
...
```

