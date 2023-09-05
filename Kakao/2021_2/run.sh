#!/bin/bash

INIT_TOKEN="2c23abb3bfc8f8269b90fafa2bc6dd72"
BASE_URL="https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

MATCH_SKILL=10000
WAIT_WEIGHT=2

python other_solution.py --problem 1 --init-token $INIT_TOKEN --base-url $BASE_URL --match-skill 20000 --wait-weight 3
#python other_solution.py --problem 2 --init-token $INIT_TOKEN --base-url $BASE_URL --match-skill 10000 --wait-weight 4