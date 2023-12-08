with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input

hands = []
for line in inputt:
    line = line.replace("\n", "")
    hand = line.split(" ")[0]
    bid = line.split(" ")[1]

    cards = []
    value = 0
    p = 100_000_000_000_000_000
    for char in hand:
        if char.isnumeric():
            value += p * int(char)
        elif char == "T":
            value += p * 10
        elif char == "J":
            value += p * 11
        elif char == "Q":
            value += p * 12
        elif char == "K":
            value += p * 13
        elif char == "A":
            value += p * 14
        p /= 100
        if char in [value for (value, num) in cards]:
            for i in range(len(cards)):
                if cards[i][0] == char:
                    cards[i][1] += 1
        else:
            cards.append([char, 1])

    if len(cards) == 1:
        print("Is Five of a kind")
        value += 900_000_000_000_000_000_000_000
    elif len(cards) == 2 and (cards[0][1] == 4 or cards[1][1] == 4):
        print("Its Four of a kind")
        value += 800_000_000_000_000_000_000_000
    elif len(cards) == 2:
        print("It's full house")
        value += 700_000_000_000_000_000_000_000
    elif len(cards) == 3 and (cards[0][1] == 3 or cards[1][1] == 3 or cards[2][1] == 3):
        print("It's Three of a kind")
        value += 600_000_000_000_000_000_000_000
    elif len(cards) == 3:
        print("It's two pair")
        value += 500_000_000_000_000_000_000_000
    elif len(cards) == 4:
        print("It's one pair")
        value += 400_000_000_000_000_000_000_000
    else:
        print("It's high cart")
        value += 300_000_000_000_000_000_000_000
    hands.append((value, hand, bid))

hands.sort()
print(hands)

result = 0
for i in range(len(hands)):
    result += int(hands[i][2]) * (i + 1)

print(result)
print("----- PART 2 -----")

def replaceJ(input, i, result):
    if i == len(input):
        result.append(input)
        return

    if input[i] == 'J':
        for rep in 'AKQT98765432':
            replaceJ(input[:i] + rep + input[i+1:], i+1, result)
        return
    replaceJ(input, i+1, result)


def calc_value(cards):
    if len(cards) == 1:
        return 900_000_000_000_000_000_000_000
    elif len(cards) == 2 and (cards[0][1] == 4 or cards[1][1] == 4):
        return 800_000_000_000_000_000_000_000
    elif len(cards) == 2:
        return 700_000_000_000_000_000_000_000
    elif len(cards) == 3 and (cards[0][1] == 3 or cards[1][1] == 3 or cards[2][1] == 3):
        return 600_000_000_000_000_000_000_000
    elif len(cards) == 3:
        return 500_000_000_000_000_000_000_000
    elif len(cards) == 4:
        return 400_000_000_000_000_000_000_000
    else:
        return 300_000_000_000_000_000_000_000

hands = []
for line in inputt:
    line = line.replace("\n", "")
    hand = line.split(" ")[0]
    bid = line.split(" ")[1]

    cards_value = 0
    p = 100_000_000_000_000_000
    for char in hand:
        if char.isnumeric():
            cards_value += p * int(char)
        elif char == "T":
            cards_value += p * 10
        elif char == "J":
            cards_value += p * 1
        elif char == "Q":
            cards_value += p * 12
        elif char == "K":
            cards_value += p * 13
        elif char == "A":
            cards_value += p * 14
        p /= 100

    combi = []
    replaceJ(hand, 0, combi)
    best = 0
    for comb in combi:
        cards = []
        for char in comb:
            if char in [value for (value, num) in cards]:
                for i in range(len(cards)):
                    if cards[i][0] == char:
                        cards[i][1] += 1
            else:
                cards.append([char, 1])
        value = calc_value(cards)
        if value > best:
            best = value
    hands.append((best + cards_value, hand, bid))

hands.sort()
print(hands)

result = 0
for i in range(len(hands)):
    result += int(hands[i][2]) * (i + 1)

print(result)
