"""Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""
units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
         'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
         'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
        'ninety']
units_length = ''.join(units)
teens_length = ''.join(teens)
twenty_to_ninetynine = ''
for t in tens:
    for u in units:
        twenty_to_ninetynine += t + u
first99 = units_length + teens_length + twenty_to_ninetynine
total = len(first99)*10
for u in units[1:]:
    total += 100 * (len(u) + len('hundred')) + 99 * len('and')
total += len('onethousand')
print total