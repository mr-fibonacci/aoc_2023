import re


def format_line(line: str):
    card_id, numbers = re.split(":\s+", line)
    card_id_formatted = int(card_id.split()[1])
    winning_numbers, elf_numbers = numbers.split(" | ")
    winning_numbers_formatted = {
        number: int(number) for number in winning_numbers.split()
    }
    elf_numbers_formatted = {number: int(number) for number in elf_numbers.split()}

    elf_winning_numbers = (
        winning_numbers_formatted.keys() & elf_numbers_formatted.keys()
    )
    return [elf_winning_numbers, card_id_formatted]


def part1():
    data = open("04.txt").read().splitlines()

    def handle_line(line: str):
        elf_winning_numbers, card_id_formatted = format_line(line)
        return pow(2, len(elf_winning_numbers) - 1) if len(elf_winning_numbers) else 0

    answer = sum([handle_line(line) for line in data])
    print(answer)
    return answer


def part2():
    data = open("04.txt").read().splitlines()

    cards_winning_numbers = {}
    for line in data:
        elf_winning_numbers, card_id_formatted = format_line(line)
        cards_winning_numbers[card_id_formatted] = len(elf_winning_numbers)

    card_duplicates = {i + 1: 0 for i in range(len(data))}
    stack = [i + 1 for i in range(len(data))]
    while stack:
        number = stack.pop()
        card_duplicates[number] += 1
        for i in range(cards_winning_numbers.get(number) or 0):
            stack.append(number + i + 1)

    answer = sum(card_duplicates.values())
    print(answer)
    return answer


part1()
part2()
