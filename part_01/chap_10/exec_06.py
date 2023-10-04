# while True:
#     try:
#         first_number = input('Input the first number: ')
#         if first_number == 'q':
#             break
#         first_number = int(first_number)
#         second_number = input('Input the second number: ')
#         if second_number == 'q':
#             break
#         second_number = int(second_number)
#         print(
#             f"{first_number} + {second_number} = {first_number + second_number}")
#     except ValueError:
#         print("请输入数字！")

def print_file(filename):
    try:
        with open(filename) as f:
            print(f.read().rstrip())
    except FileNotFoundError:
        # print(f'{filename} Not Found!')
        pass


print_file('cats.txt')
print_file('dogs.txt')


def count_file_word(filename, word):
    try:
        with open(filename, encoding='UTF-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f'{filename} Not Found!')
    else:
        count_word(word, content)


def count_word(word, content):
    count = content.lower().count(word)
    print(f'{word} 出现了 {count} 次')

    count = content.lower().replace(',', '').replace('.', '').split().count(word)
    print(f'{word} 出现了 {count} 次（list count）')

    word_list = content.lower().replace(',', '').replace('.', '').split()
    count = 0
    for w in word_list:
        if w == word:
            count = count + 1

    print(f'{word} 出现了 {count} 次（split()）')



count_file_word('pg71570.txt', 'be')
