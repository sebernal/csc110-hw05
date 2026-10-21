"""
Name: (Sophia Bernal)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """Gets a single uppercase letter from A to C """
    # remove the default return and add your code
    #Start loop
    while True:
        #Get user input
        letter = input("Give me a single uppercase letter: ")
        #Check length of string
        str_length = len(letter)
        #If the string is not 1 letter print error
        if str_length!= 1:
            print("Error: it needs to be a single character.")
            continue
        #Check if letter is A, B, or C
        if letter =='A' or letter=='B' or letter=='C':
            return letter
        #If letter is not A, B, or C print error 
        else:
            print("Error: You provided the wrong character.")
            continue 

def get_digit():
    """ Gets a single digit within the range 1 to 3 """
    # remove the default return and add your code
    while True:
    #Gets a number 
        digit = input("Give an single number character: ")
    #Check if input is a digit
        digit_check = digit.isdigit()
    #Check length of digit
        digit_length = len(digit) 
    #If input is not a digit, print error
        if digit_check == False:
            print("Error: your input should be only digits.")
            continue
    #If not single digit, print error
        if digit_length!=1:
            print("Error: a single digit needs to be in [1,3].")
            continue
    #If digit is in range, return digit 
        if  digit =='1' or digit=='2' or digit=='3':
            return digit
    #If digit is not in range, print error
        else:
            print("Error: a single digit needs to be in [1,3].")
            continue
        
def check_pattern(letter, digit, lst):
    """Searches list of strings for a letter-number pair that appears in order """
    # remove the default pass and add your code
    print("Strings with the pattern:")
    #Start outer loop, go through each string in the list
    for st in lst:
    #Inner loop, go through each character in the string
    #Use enumerate to pair the character with it's index
        for i, ch in enumerate(st):
            index_let = i
            character = ch
    #Check if the character is the letter 
            if character == letter:
    #Go through each character in the string
    #Use enumerate again to pair each element with it's index
                for i, num in enumerate(st):
                    index_num = i
                    number = num
    #Check if number is the digit
                    if number == str(digit):
    #If the letter's index is less than the number's index, print the string 
                        if index_let < index_num:
                            print(st, end=" ")
    #Once the string is printed, leave the inner loop
                            break
                        print()
            else:
                continue
                        
        
#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
#Start loop
    while True:
#Save the letter returned in function get_letter in user_let
        user_let = get_letter()
#Save the digit returned in get_digit in user_num
        user_num = get_digit()
#Call function with the neccessary arguments
        check_pattern(user_let, user_num, st_list)
#Ask user if they want to try again
        yes_no = input("Try Again?(y/n):")
#If user does not want to try again, stop loop
        if yes_no != 'y':
            break
            
    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()