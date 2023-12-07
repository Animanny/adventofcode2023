card_count = {num: 0 for num in range(1, 208)}

with open("in.txt", "r") as file:
    for line in file:
        line = line.strip()
        card_num, nums = line.split(':')
        card_num = int(card_num.split()[-1])
        winning_nums, my_nums = [x.strip().split() for x in nums.split("|")]
        card_count[card_num] += 1
        matching_cards = 0

        for num in my_nums:
            if num in winning_nums:

                matching_cards += 1

        print(matching_cards)

        for i in range(card_num + 1, card_num + 1 + matching_cards):

            card_count[i] += card_count[card_num]



print(sum(card_count.values()))
