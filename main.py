from module import test

aa = test.break_words('I am liqiang 1 2 3 4')
print(aa)
for i in aa:
    print(i)

print(test.sort_words('acdb'))

test.print_first_word(['j', 'a', 'ug', 'ea'])
print(test.sort_sentence('Takes in a full sentence and returns the sorted words.'))
test.print_first_and_last('Prints the first and last words of the sentence.')
test.print_first_and_last_sorted("Sorts the words then prints the first and last one.")
