def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    question = 'Why did th chicken cross th street?'
    answers = ['To impress a chick', 'To save its neck', 'To get to the other side', 'Why not?']
    correct_answer = 3
    user_answer = 0
    counter = 1
    print(question)
    while counter < len(answers):
        print('{}. {}'.format(counter, answers[counter - 1]))
        counter += 1

    while user_answer != correct_answer:
        user_answer = int(input())
        if user_answer != correct_answer:
            print('Please, try again')
        else:
            print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
