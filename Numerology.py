text  = ["\nYour Numerology Number is 1.\nNumber 1 indicates pillar shape and reflects independence and strength.",
         "\nYour Numerology Number is 2.\nNumber 2 plays a supportive role in their life. They are sentimental, lazy, and can easily get depressed.",
         "\nYour Numerology Number is 3.\nNumber 3 is the most imaginative of all numbers and is reflected in its open and inviting shape, ready to embrace anyone in this world.",
         "\nYour Numerology Number is 4.\nNumber 4 is square-shaped and down to earth. It is fixed on the ground and acts as a rock of support for all other numbers.",
         "\nYour Numerology Number is 5.\nNumber 5 is open in front and back. It is the most dynamic of all the numbers.",
         "\nYour Numerology Number is 6.\nNumber 6 is the most loving and surviving of all numbers, magnetic, youthful, gentle, soft-spoken, romantic, luxury-loving, artistic, and possessors of refined taste.",
         "\nYour Numerology Number is 7.\nNumber 7 is a thinker and a saint. It is creative, unconventional & moody. It is the most spiritual of all numbers.",
         "\nYour Numerology Number is 8.\nNumber 8 represents the balance between the spiritual and material world. The symbol of 8 reflects heaven and earth in the two circles stacked on top of each other.",
         "\nYour Numerology Number is 9.\nNumber 9 completes the circle. Like 6, it is a loving number, but where 6 loves the family, friends and the community, 9 gives its love to the world; it is the humanitarian number. Thus, considered to be a lucky number."
         ]

def reduce(n):
    t = 0
    while n > 0:
        t += n % 10
        n //= 10
    return t

n = int(input("Enter your birth date (DDMMyYYY without separating) : "))

while n > 9:
    n = reduce(n)

print(text[n-1])