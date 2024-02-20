contents = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing",
    "do eiusmod tempor incididunt ut labore",
    "ullamco laboris nisi ut aliquip ex ea c",
]


file_names = ["test01.txt", "test02.txt", "test03.txt"]

# for i in range(len(file_name)):
#     file = open(f"1_Beginner_Project/to-do/test-env/files/{file_name[i]}", "w")
#     file.writelines(contents[i])
#     file.close()


for content, file_name in enumerate(zip(contents, file_names)):
    # file = open(f"1_Beginner_Project/to-do/test-env/files/{file_name}", "w")
    # file.writelines(content)
    # file.close()
    print(content, file_name)
