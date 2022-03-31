from distutils.file_util import write_file


word_list = []
correct_letters = {}
with open(r'Documents/words.txt', 'r') as f:
    w_file = f.readlines()
    for x in w_file:
        word_list.append(x.replace("\n",""))
        
        

best_word = "React, Adieu, Later, Tears, Alone, Arise, Sauce, Anime, Roast"
print("Suggested Words: "+best_word)

while True:
    agian = 1
    while agian == 1:
        letter = input("Enter one correct letter and position ('store' Ex-o3): ")
        if len(letter) == 2:
            correct_letters[letter[0]] = int(letter[1])
        agian = int(input("Enter another letter? Press 1: "))
    wrong = input("Enter wrong letters('store' Ex-stre): ")
    
    temp = []
    for y in word_list:
        for l in wrong:
            if l in y:
                if(y not in temp):
                    temp.append(y)
                
        for key, val in correct_letters.items():
            if key not in y[val-1]:
                if(y not in temp):
                    temp.append(y)
    for x in temp:
        word_list.remove(x)       
    print(word_list)

    con = input("Enter 1 to continue: ")
    if con != '1':
        break
