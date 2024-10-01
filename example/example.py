import numpy as np
from meltingpot import substrate, scenario

import configs

def main():
    np.random.seed(configs.seed)
    
    # train
    env_name = configs.substrate_name
    env_config = substrate.get_config(env_name)
    env = substrate.build(env_name, roles=env_config.default_player_roles)
    action_dim = env.action_spec()[0].num_values
    num_agents = len(env.observation_spec())

    rewards = []
    env.reset()
    for t in range(configs.total_timesteps):
        # random policy
        actions = np.array([np.random.randint(action_dim) for _ in range(num_agents)])
        timestep = env.step(actions)
        rewards.append(np.mean(timestep.reward))

        if t % configs.log_interval == 0:
            print(f"Step {t} - average reward: {np.mean(rewards)}")

    # evaluate
    factory = scenario.get_factory(configs.scenario_name)
    eval_env = factory.build()
    num_focal_agents = np.sum(eval_env._is_focal)

    eval_env.reset()
    for epoch in range(configs.num_episodes):
        rewards = []
        for t in range(configs.rollout_len):
            # random policy
            actions = np.array([np.random.randint(action_dim) for _ in range(num_focal_agents)])
            timestep = env.step(actions)
            rewards.append(np.mean(timestep.reward))

        print(f"Epoch {epoch} - average reward: {np.mean(rewards)}")

if __name__ == "__main__":
    main()