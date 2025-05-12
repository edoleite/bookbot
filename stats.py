def count_words(text):
    word_count = len(text.split())
    return word_count

def count_chars(text):
    char_count_dict = {}
    lowered_text = text.lower()
    char_list = list(lowered_text)
    
    for char in char_list:        
        if char not in char_count_dict:
            char_count_dict[char] = 1        
        else:
            char_count_dict[char] += 1

    return char_count_dict

def sort_dictionary(raw_dict):    
    
    list_of_dicts = [{"char": k, "num": v} for k, v in raw_dict.items()]
    
    return sorted(list_of_dicts, key=lambda x: x["num"], reverse=True)




