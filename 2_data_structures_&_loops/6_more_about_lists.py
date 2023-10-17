
threshold = 10
results = [12, 15, 14, 10, 40]

all_above_threshold = True
for value in results:
    if value < threshold:
        all_above_threshold = False

print(all_above_threshold)

is_above_threshold = [x > threshold for x in results]
print(is_above_threshold)
print(any(is_above_threshold))  # czy jakakolwiek wartość w is_above_threshold wynosi True
print(all(is_above_threshold))  # czy wszystie wartości w is_above_threshold wynoszą True
