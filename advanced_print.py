def adv_print(*args, **kwargs):
    if len(args) == 1:
        start = args[0]
    else:
        if len(args) == 2:
            start = args[0]
            max_line = args[1]
        elif len(args) == 3:
            start = args[0]
            max_line = args[1]
            in_file = args[2]
        else:
            pass
    sum_words = 0
    str_list = start.split()
    for word in str_list:
        sum_words += len(word) + 1
        if sum_words > max_line:
            print()
            sum_words = 0
        print(word, end=' ')
    if in_file == True:
        sum_words = 0
        with open('result.txt', 'w') as f:
            for word in str_list:
                sum_words += len(word) + 1
                if sum_words > max_line:
                    f.write('\n')
                    sum_words = 0
                f.write(word + ' ')