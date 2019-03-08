from obstacle_tower_env import ObstacleTowerEnv
import sys
import argparse

def run_episode(env):
    done = False
    episode_reward = 0.0
    
    while not done:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        episode_reward += reward
        
    return episode_reward

def run_evaluation(env):
    while not env.done_grading():
        run_episode(env)
        env.reset()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('environment_filename', default='./ObstacleTower/obstacletower', nargs='?')
    parser.add_argument('--docker_training', action='store_true')
    parser.set_defaults(docker_training=False)
    args = parser.parse_args()

    env = ObstacleTowerEnv(args.environment_filename, docker_training=args.docker_training)
    if env.is_grading():
        episode_reward = run_evaluation(env)
    else:
        while True:
            episode_reward = run_episode(env)
            print("Episode reward: " + str(episode_reward))
            env.reset()

    env.close()

