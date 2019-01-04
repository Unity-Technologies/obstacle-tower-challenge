from obstacle_tower_env import ObstacleTowerEnv
import sys

def run_episode(env, first_observation):
    """
    Runs a single episode
    and expects that env.reset has been done before calling
    this function.
    """
    obs = first_observation
    done = False
    reward = 0.0

    while not done:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
    return reward

def run_evaluation(env):
    """
    Runs an arbitrary number of episodes during evaluation
    """
    while True :
        obs = env.reset()
        if not obs:
            """
                The evaluator returns observation==False after it has run
                the required number of episodes. If it returns a valid
                observation on an `env.reset` call, then the evaluator expects
                to run another episode.
            """
            break
        run_episode(env, obs)

if __name__ == '__main__':
    environment_filename = \
        sys.argv[1] if len(sys.argv) > 1 else './ObstacleTower/obstacletower'

    env = ObstacleTowerEnv(environment_filename)
    if env.is_grading():
        run_evaluation(env)
    else:
        while True:
            first_observation = env.reset()
            episode_reward = run_episode(env, first_observation)
            print("Episode reward: " + str(episode_reward))

    env.close()
