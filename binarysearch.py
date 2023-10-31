def binary_search_difference_two(start, end):
    if start % 2 != 0:
        start += 1

    result = []
    while start <= end:
        result.append(start)
        start += 2

    return result

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = binary_search_difference_two(start, end)
print(result)
