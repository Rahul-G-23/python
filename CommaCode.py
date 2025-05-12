def comma_code(input_list):
    if not input_list:
        return ""
    elif len(input_list) == 1:
        return str(input_list[0])
    else:
        first_part = ', '.join(map(str, input_list[:-1]))
        
        last_part = 'and ' + str(input_list[-1])
        return f"{first_part}, {last_part}"

print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O')
spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))

empty_list = []
print(comma_code(empty_list))

single_item_list = ['hello']
print(comma_code(single_item_list))

numbers_list = [1, 2, 3, 4]
print(comma_code(numbers_list))
