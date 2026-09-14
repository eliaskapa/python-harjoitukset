
numbers = []

while True:
    input_number = input("Anna luku: ")
    if input_number == "":
        break
        #lopeta kysely
    #lisätään syötetty luku listalle
    numbers.append(int(input_number))

numbers.sort(reverse=True)
print(numbers[0:5])

# for-lauseella viisi ensimmäistä alkiota
for num in range(5):
    print(numbers[num])