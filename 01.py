import regex

def part_1():
    def handle_line(line: str):
        matches = regex.findall("\d", line)
        first_digit = int(matches[0])
        last_digit = int(matches[-1])
        calculated_value = first_digit * 10 + last_digit
        
        return calculated_value

    data = open("01.txt").read().splitlines()
    answer1 = sum([handle_line(line) for line in data])
    print(answer1)

def part_2():
    def handle_line(line:str):
        word_to_digit = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
        }
        matches = regex.findall("(\d|one|two|three|four|five|six|seven|eight|nine)", line, overlapped=True)
        
        first_digit = int(word_to_digit.get(matches[0]) or matches[0])
        last_digit = int(word_to_digit.get(matches[-1]) or matches[-1])
        calculated_value = first_digit * 10 + last_digit
        
        return calculated_value

    data = open("01.txt").read().splitlines()
    answer2 = sum([handle_line(line) for line in data])
    print(answer2)

part_1()
part_2()