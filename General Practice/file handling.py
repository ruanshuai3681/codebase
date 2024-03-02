with open("helloruanshuai.txt","w") as file:
    file.write("this is first line")

with open("hello.txt", "r") as file:
    content=file.read()
    print("file content:", content)

