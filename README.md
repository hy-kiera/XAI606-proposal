# Melting Pot 2.0 Challenge

This Melting Pot 2.0 Challenge is for advancing research in multi-agent reinforcement learning (MARL). The goal of this challenge is to demonstrate cooperative intelligence in complex environments.

Please read `README.md` for the project proposal related to the XAI606: Applications and Practice in Neural Networks course.

## Tasks
The challenge involves developting innovative MARL solutions that focus on achieving objectives through teamwork, teaching, negotiation, and sanctioning undesirable behaviors. The provided scenarios are specifically designed to encourage cooperation, coordination, reciprocity, and other prosocial behaviors.


### Substrates
This project will focus on the following four substrates:
- allelopathic_harvest__open
- clean_up
- prisoners_dilemma_in_the_matrix__arena
- territory__rooms

### Scenarios
Below are the training and evaluation scenarios for each substrate:
| Substrate | Training Scenario | Evaluation Scenario |
| --- | --- | --- |
| allelopathic_harvest__open | sc1 | sc2 |
| clean_up | sc0 | sc1 |
| prisoners_dilemma_in_the_matrix__arena | sc0 | sc1 |
| territory__rooms | sc0 | sc1 |

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
