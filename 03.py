import itertools, re


def part1():
    data = open("03.txt").read().splitlines()
    Y_LEN = len(data)
    X_LEN = len(data[0])

    def get_ys(y: int):
        return y if y > 0 else 0

    def get_ye(y: int):
        return y if y < Y_LEN else Y_LEN - 1

    def get_xs(x: int):
        return x if x > 0 else 0

    def get_xe(x: int):
        return x if x < X_LEN else X_LEN

    def get_top(y: int, xs: int, xe: int):
        return data[get_ys(y - 1)][get_xs(xs - 1) : get_xe(xe + 1)]

    def get_mid(y: int, xs: int, xe: int):
        return data[y][get_xs(xs - 1) : get_xe(xe + 1)]

    def get_bottom(y: int, xs: int, xe: int):
        return data[get_ye(y + 1)][get_xs(xs - 1) : get_xe(xe + 1)]

    def get_box_strings(y: int, xs: int, xe: int):
        return get_top(y, xs, xe) + get_mid(y, xs, xe) + get_bottom(y, xs, xe)

    def box_includes_symbol(box_string: str):
        symbols = {
            "=": 54,
            "-": 39,
            "*": 364,
            "/": 34,
            "+": 42,
            "$": 46,
            "&": 42,
            "%": 49,
            "#": 47,
            "@": 37,
        }

        regex_string = "\\" + "|\\".join(symbols.keys())
        return bool(re.search(regex_string, box_string))

    part_numbers = []
    for y, line in enumerate(data):
        matches = re.finditer("\d+", line)

        for a_match in matches:
            xs, xe = a_match.span()
            for box_string in get_box_strings(y, xs, xe):
                is_part_number = box_includes_symbol(box_string)
                if is_part_number:
                    part_numbers.append(int(a_match.group()))

    print(sum(part_numbers))


part1()


