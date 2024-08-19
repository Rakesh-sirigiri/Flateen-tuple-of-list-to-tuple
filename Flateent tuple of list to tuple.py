test_tuple = ([4,1], [6,8,7,9], [2])
print("The original tuple:" + str(test_tuple))
res = tuple(sum(test_tuple, []))
print("The flattened tuple: " + str(res))
