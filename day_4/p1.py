pts = 0
with open("in.txt", "r") as file:
    for line in file:
        line = line.strip()
        card_num, nums = line.split(':')
        winning_nums, my_nums = [x.strip().split() for x in nums.split("|")]
        print(card_num, winning_nums, my_nums)
        curr_pts = 0

        for num in my_nums:
            print(num)
            if num in winning_nums:

                curr_pts = curr_pts*2 if curr_pts != 0 else 1


        pts += curr_pts

print(pts)
