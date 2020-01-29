import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

def choose_number(max_number):
    
    c = random.randint(1, max_number)
    return c


print('Greetings!')
play_again = ''
best_count = sys.maxsize            
last_color = ''
trophy = 0
while (play_again != 'n' and play_again != 'no'):
    count = 0
    number = 0
    k = 0
    while(k==0):
      try:
        num = int(input("\nWhat would you like the maximum number to be?"))
        k = 1
      except ValueError:
        print("\nThat's not a number.")
        k = 0
    match_number = choose_number(num)
    while (number != match_number):
        k = 0
        while(k == 0):
          try:
            number = int(input("\nWhat do you think the number is?"))
            k = 1
            count+=1
          except ValueError:
            print("\nThat's not a number.")
            k = 0
            
        if (number == match_number):
            print('Correct!')
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    print('\nYou guessed it in {} tries!'.format(count))
    print('\nAnd that is out of a range of {} possibilities.'.format(num))
    if ((count > num)):
        trophy = 0
        print('\nYou got the secret best trophy! \nAnd by best, I mean it is so bad that all of your other trophies are gone now. \nSorry. \nIf you wanted trophies you should have actually tried to guess the number.')
    elif ((num/count > 8) and trophy < 4):
        trophy = 4
        print('\nYou earned the platinum trophy! That is the best one! You will not be able to earn more trophies.')
    elif ((num/count > 6) and trophy < 3):
        trophy = 3
        print('\nYou earned the gold trophy! There is still a better one out there..')
    elif ((num/count > 4) and trophy < 2):
        trophy = 2
        print("\nYou earned a silver trophy! Not the worst.")
    elif ((num/count > 2) and trophy < 1):
        trophy = 1
        print("\nYou earned a bronze trophy! At least you earned one.")
    else:
        print("\nYou didn't earn a trophy. Maybe you just did horribly, or maybe you already had the best one! Who knows?")



    if (count < best_count):
        print('This was your best guess so far! But are you happy with your trophy?')
        
        best_count = count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

print('Thanks for playing! I hope you liked your final trophy.')