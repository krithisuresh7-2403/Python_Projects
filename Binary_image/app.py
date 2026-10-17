def read_binary():
    with open("sample_image.jpg", "rb") as file:
        content = file.read()
        copy_image(content)
        
def copy_image(content):
    with open("copy_image.jpg", "ab") as file:
        file.write(content)
        
# def read_content():
#     with open("copy_image.jpg", "r") as file:
#         content_r = file.read()
#         print(content_r)
        
if __name__ == "__main__":
    read_binary()
