file_path="output.txt"
with open(file_path,'a') as file:
    file.write("\n This is an additionalline:")
    print("Content appended to:",file_path)
