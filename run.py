from obstacle_tower_env import ObstacleTowerEnv
import sys

def run_episode(env):
    env.reset()
    done = False
    reward = 0.0

    while not done:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
    return reward


if __name__ == '__main__':
    environment_filename = \
        sys.argv[1] if len(sys.argv) > 1 else './ObstacleTower/obstacletower'

    env = ObstacleTowerEnv(environment_filename)
    if env.is_grading():
        score = run_episode(env)
    else:
        while True:
            reward = run_episode(env)
            print("Episode reward: " + str(reward))

    env.close()

