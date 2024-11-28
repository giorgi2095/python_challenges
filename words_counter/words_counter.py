def main():
    file_name = input("File name: ")
    file_path = f"words_counter/{file_name}"
    if file_path:
        file_content = open(file_path, "r")
        words = file_content.read().split(" ")
        print(f"In the file are {len(words)} words.")
    else:
        print("File not found.")

if __name__ == '__main__':
    main()