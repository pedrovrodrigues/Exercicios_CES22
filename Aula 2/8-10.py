def reverse(str):
    str_rev = ""
    n = len(str)
    for i in range(n):
        str_rev += str[n-1-i]
    return str_rev

def is_palindrome(str):
    return str == reverse(str)

print(reverse("happy"))
print(reverse("Python"))
print(reverse(""))
print(reverse("a"))
print(is_palindrome("abba"))
print(is_palindrome("abab"))
print(is_palindrome("tenet"))
print(is_palindrome("banana"))
print(is_palindrome("straw warts"))
print(is_palindrome("a"))
print(is_palindrome(""))