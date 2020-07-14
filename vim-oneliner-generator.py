import sys


termlist = {
        " ":    "<Space>",
        "\n":   "<Enter>",
        "\t":   "<Tab>",
        "\"":   "\\\"",
        "\\":   "\\\\",
        }

print(termlist)

def find_all(input_string: str, substring: str):
    indices = []
    i = 0
    while(i != -1):
        index = input_string.find(substring, i+1)
        #print(input_string)
        #print(index)
        indices.append([index, substring])
        i = index
    return indices


with open("input.txt", "r") as input:
    print("Input recived:")
    input_content = str(input.read())
    registry = []
    for each_item in termlist:
        print("Instances of "+str(each_item)+" found:")
        instances = find_all(input_content, each_item)
        print(instances)
        registry.append(instances)
    print("\n\n\nChanges needed:")
    print(registry[0])
    for each_item in registry:

