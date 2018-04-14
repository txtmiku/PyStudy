def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def removmark(text):
    mark = (',','.','?',' ')
    nomark =''
    for char in text:
        if char in mark:
            continue 
        else:
            nomark += char.upper()
    return nomark


something = removmark(input("Enter text:"))
print(something)
if is_palindrome(something):
    print("Yes,it is a palindrome")
else:
    print("No,it is not a palindrome")