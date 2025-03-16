
# result = ["".join(x if x == y else ' ' for x in x_axis) for y in y_axis]

# is equivalent to:
# result = []
# for y in y_axis:
#    row = ''
#    for x in x_axis:
#        if x == y:
#            row += x
#        else:
#            row += ' '
#    result.append(row)
# return result