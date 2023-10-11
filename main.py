with open("books/frankenstein.txt") as f:
    
    file_contents = f.read()  
    words = file_contents.split()
    word_count = len(words)


    
    
    def count_letter_text():
        dict_num = {}    
        for word in words:
            lower_word = word.lower()
            for letter in lower_word:
                if letter.isalpha():
                    if letter in dict_num:
                        dict_num[letter] += 1
                    else: 
                        dict_num[letter] = 1
        dict_num = dict(sorted(dict_num.items()))
        return dict_num
    dict_num = count_letter_text()
    
    def present_dic():
        print(f"--- Begin report of {f.name}")
        print(f"{word_count} words found in the document\n")
        for dict_item in dict_num:
            dict_value = dict_num[dict_item]

            print(f"The '{dict_item}' character was found {dict_value} times")
        print("End Report")
    present_dic()
            

            