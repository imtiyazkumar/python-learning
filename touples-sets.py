# They are like lists (sequence of objects) but they are immutable i.e. once they have been
# defined we cannot change them.
# Parenthesis in tuples are optional.


marks = (95, 98, 97, 97)
#marks[0] = 98
print(marks.count(97))
print(marks.index(97))

# Sets

# Sets are a collection of all unique elements.
# Indexing is not supported in sets.

marks = {98, 97, 95, 95}
print(marks)
for score in marks:
    print(score)
