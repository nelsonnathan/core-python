"""Restaurant rating lister."""


# put your code here
add_score = open('scores.txt', 'a')

restaurant_sub = input('What restuarant are you reviewing? ')
review_sub = input('Out of 5, how do you rate it? ')
formatted_sub = restaurant_sub + ':' + review_sub

add_score.write('\n')
add_score.write(formatted_sub)
add_score.close()

scores = open('scores.txt', 'r')

scores_list = [line.rstrip().split(':') for line in scores]

dict_scores = {each[0]:each[1] for each in scores_list}

tuple_scores = dict_scores.items()
sorted_tuples = sorted(tuple_scores)

for eatery in sorted_tuples:
    print(f'{eatery[0]} is rated at {eatery[1]}.')

scores.close()
