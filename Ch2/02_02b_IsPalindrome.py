import collections
import string

# function to normalise the string - remove punctuation and white space, make lowercase
def getLetters(text):
    # Print the string in question
    print(f"String to test: {text}")
    # Remove whitespace and make lowercase
    text = text.replace(" ", "").lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def isPalindrome(text):
    # Use lowercase to avoid issues with capitalisation
    # Strip and remove punctuation so we can use sentences
    text = getLetters(text)

    # Make the string into a deque (automatically splits into constituent letters)
    text = collections.deque(text)

    # while the deque is at least 2 characters long
    # check whether the first and last items are the same
    while len(text) > 1:
        # If they're not, return False
        if text.pop() != text.popleft():
            return False
        else:
            pass
    # If the while loop finished, then the word was a palindrome
    return True


def main():
    #add code here
    # Simple True case - all lower case, no spaces or punctuation
    print(isPalindrome("tacocat"))
    
    # Simple False case
    print(isPalindrome("Grains"))

    # More compicated True case - Uppercase letter
    print(isPalindrome("Hannah"))

    # Complex True case - Capitals, spaces, punctuation
    print(isPalindrome("Do geese see God?"))

if __name__ == "__main__":
    main()