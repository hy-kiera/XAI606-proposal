# Melting Pot 2.0 Challenge

This Melting Pot 2.0 Challenge is for advancing research in multi-agent reinforcement learning (MARL). The goal of this challenge is to demonstrate cooperative intelligence in complex environments.

Please read `README.md` for the project proposal related to the XAI606: Applications and Practice in Neural Networks course.

Please contact my email `hayeong_lee@korea.ac.kr` if you have any questions.

## Tasks
The challenge involves developting innovative MARL solutions that focus on achieving objectives through teamwork, teaching, negotiation, and sanctioning undesirable behaviors. The provided scenarios are specifically designed to encourage cooperation, coordination, reciprocity, and other prosocial behaviors.


### Substrates
This project will focus on the following four substrates:
- allelopathic_harvest__open
- clean_up
- prisoners_dilemma_in_the_matrix__arena
- territory__rooms

#### Observation and Action
The agents have a partial observability window of 11 $\times$ 11 sprites (8 $\times$ 8 pixels), offset so they see more infront than behind them. The agent sees 9 rows in front of itself, 1 row behind, and 5 columns to either side. Thus in RGB pixels, the size of each observation is 88 $\times$ 88 $\times$ 3.

Movement actions are forward, backward, strafe left, strafe right, turn left, and turn right.

```
from meltingpot import substrate

env_name = 'clean_up'
conf = substrate.get_config(env_name)
env = substrate.build(env_name, roles=conf.default_player_roles)

print(env.observation_spec())
print(env.action_spec())
```

### Scenarios
Below are the evaluation scenarios for each substrate:
| Substrate | Evaluation Scenario |
| --- | --- |
| allelopathic_harvest__open | sc1 |
| clean_up | sc1 |
| prisoners_dilemma_in_the_matrix__arena | sc0 |
| territory__rooms | sc0 |

For example, to set up a scenario:
```
from meltingpot import scenario

name = "clean_up_0" # substrate: clean_up, scenario: sc0
factory = scenario.get_factory(name)

with factory.build() as env:
    # TODO: Implement policy logic
```

For further details, please refer to the [Melting Pot Github](https://github.com/google-deepmind/meltingpot/tree/main) and [Melting Pot 2.0 Tech Report](https://arxiv.org/abs/2211.13746).

## Evaluation Metric
Policies will be evaluated based on accumulated rewards from the environment across five episodes, with three different seeds (0, 1, 2) used for each evaluation scenario.