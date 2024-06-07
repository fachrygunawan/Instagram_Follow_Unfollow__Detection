import re

def remove_date_formats(text):
    date_pattern = r'[A-Z][a-z]{2} \d{1,2}, \d{4}, \d{1,2}:\d{2} [AP]M'

    cleaned_text = re.sub(date_pattern, '', text)

    return cleaned_text

def print_difference_between_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    only_in_list1 = set1 - set2
    only_in_list2 = set2 - set1

    if only_in_list1:
        print("User that you didn't followed back: (Count:", len(only_in_list1), "):")
        print("\n".join(only_in_list1))
    else:
        print("user that dont followed you back.")

    if only_in_list2:
        print("\nUser that didn't followed you back: (Count:", len(only_in_list2), "):")
        print("\n".join(only_in_list2))
    else:
        print("There are no users that dont followed you back.")

# Take input for follower
list1 = []
print("Enter the names of your follower:")
while True:
    name = input().strip()
    if name.lower() == 'done':
        break
    # Remove date formats from input
    name = remove_date_formats(name)
    list1.append(name)

# Take input for followeing
list2 = []
print("\nEnter the names of your following:")
while True:
    name = input().strip()
    if name.lower() == 'done':
        break
    # Remove date formats from input
    name = remove_date_formats(name)
    list2.append(name)

print("\nDifferences between the two lists:")
print_difference_between_lists(list1, list2)
