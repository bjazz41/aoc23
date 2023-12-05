file = open('input.txt', 'r')
lines = file.readlines()
point_totals = []

for line in lines:
    print(line)

    card_number, card_details = line.split(':')
    card_number = card_number.strip()
    winning_numbers, my_numbers = card_details.split('|')
    winning_numbers = [num.strip() for num in winning_numbers.split() if len(num.strip())>0]
    my_numbers = [num.strip() for num in my_numbers.split() if len(num.strip())>0]

    winners = [value for value in my_numbers if value in winning_numbers]

    cnt_winners = len(winners)
    points = pow(2, cnt_winners-1) if cnt_winners > 0 else 0
    point_totals.append(points)


    print(card_number)
    print('winning numbers', winning_numbers)
    print('my numbers', my_numbers)
    print('winners:', winners)
    print('points: ', points)

print("Total points: ", sum(point_totals))
