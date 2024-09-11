def alphabet_war(fight):
    left_powers = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_powers = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    
    
    fight_list = list(fight)
    for i in range(len(fight_list)):
        if fight_list[i] == 't':
            if i > 0 and fight_list[i-1] in right_powers:
                fight_list[i-1] = convert_to_friendly(fight_list[i-1], 'left')
            if i < len(fight_list) - 1 and fight_list[i+1] in right_powers:
                fight_list[i+1] = convert_to_friendly(fight_list[i+1], 'left')
        elif fight_list[i] == 'j':
            if i > 0 and fight_list[i-1] in left_powers:
                fight_list[i-1] = convert_to_friendly(fight_list[i-1], 'right')
            if i < len(fight_list) - 1 and fight_list[i+1] in left_powers:
                fight_list[i+1] = convert_to_friendly(fight_list[i+1], 'right')
    
   
    left_score = sum(left_powers.get(letter, 0) for letter in fight_list)
    right_score = sum(right_powers.get(letter, 0) for letter in fight_list)
    
    
    if left_score > right_score:
        return "Left side wins!"
    elif right_score > left_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"

def convert_to_friendly(letter, side):

    conversion_map = {
        'left': {'m': 'w', 'q': 'p', 'd': 'b', 'z': 's'},
        'right': {'w': 'm', 'p': 'q', 'b': 'd', 's': 'z'}
    }
    return conversion_map[side][letter]

print(alphabet_war("z")) 
print(alphabet_war("tz")) 
