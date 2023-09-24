def find_most_common_bit(pos, data):
    return '1' if sum(int(d[pos]) for d in data) >= (len(data) / 2.0) else '0'


def get_with_given_bit(bit, pos, data):
    return [d for d in data if d[pos] == bit]


with open('input') as f:
    digits = [line.strip() for line in f]

    current_dataset = digits
    for curren_bit_pos in range(len(digits[0])):
        current_dataset = get_with_given_bit(
            find_most_common_bit(curren_bit_pos, data=current_dataset),
            curren_bit_pos,
            current_dataset
        )
        if len(current_dataset) == 1:
            break

    ox_gen = int(current_dataset[0], base=2)

    current_dataset = digits
    for curren_bit_pos in range(len(digits[0])):
        current_dataset = get_with_given_bit(
            str(1 - int(find_most_common_bit(curren_bit_pos, data=current_dataset))),
            curren_bit_pos,
            current_dataset
        )
        if len(current_dataset) == 1:
            break

    co = int(current_dataset[0], base=2)

    print(ox_gen * co)


