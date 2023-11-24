# TODO решите задачу
import json

FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)

    score_values = [item["score"] for item in json_data]
    weight_values = [item["weight"] for item in json_data]
    product_of_values = [score * weight for score, weight in zip(score_values, weight_values)]
    return round(sum(product_of_values), 3)


print(task())
