from typing import Dict, List
from functools import reduce


def part_1():
    rules_dict = {"red": 12, "green": 13, "blue": 14}

    def handle_valid(grab_dict: dict):
        return all(
            [rules_dict.get(color) >= number for (color, number) in grab_dict.items()]
        )

    def handle_grab(grab: str):
        ball_data = grab.split(", ")
        return {
            number_color.split(" ")[1]: int(number_color.split(" ")[0])
            for number_color in ball_data
        }

    def handle_line(line: str):
        game_id, game = line.split(": ")
        game_id_formatted = int(game_id.split(" ")[1])

        grabs = game.split("; ")
        grabs_formatted = [handle_grab(grab) for grab in grabs]
        is_game_valid = all([handle_valid(grab_dict) for grab_dict in grabs_formatted])

        # print(game_id_formatted, grabs_formatted, is_game_valid)
        return game_id_formatted if is_game_valid else 0

    data = open("02.txt").read().splitlines()
    answer_1 = [handle_line(line) for line in data]
    print(sum(answer_1))


def part_2():
    def get_min_set(grabs: List[Dict]):
        number_dict = {}
        for grab in grabs:
            for color, number in grab.items():
                if not number_dict.get(color) or number_dict.get(color) < number:
                    number_dict[color] = number
        return number_dict

    def handle_grab(grab: str):
        ball_data = grab.split(", ")
        return {
            number_color.split(" ")[1]: int(number_color.split(" ")[0])
            for number_color in ball_data
        }

    def handle_line(line: str):
        game_id, game = line.split(": ")
        game_id_formatted = int(game_id.split(" ")[1])

        grabs = game.split("; ")
        grabs_formatted = [handle_grab(grab) for grab in grabs]

        min_grab_set = get_min_set(grabs_formatted)
        power_of_set = reduce(lambda x, y: x * y, min_grab_set.values())

        # print(game_id_formatted, grabs_formatted)
        # print(min_grab_set, power_of_set)
        return power_of_set

    data = open("02.txt").read().splitlines()
    answer_2 = [handle_line(line) for line in data]

    print(sum(answer_2))


part_1()
part_2()
