def text_read():
    with open('1.txt', 'rt', encoding='utf-8') as file1, open('2.txt', 'rt', encoding='utf-8') as file2, open('3.txt', 'rt', encoding='utf-8') as file3:
        cont1 = file1.readlines()
        cont2 = file2.readlines()
        cont3 = file3.readlines()
        text1 = {'name' : '1.txt', 'content' : cont1, 'size' : len(cont1)}
        text2 = {'name' : '2.txt', 'content' : cont2, 'size' : len(cont2)}
        text3 = {'name' : '3.txt', 'content' : cont3, 'size' : len(cont3)}
        texts = [text1, text2, text3]
        poryadok = sorted(texts, key=lambda text: text['size'])
    return poryadok

def text_rec():
    with open('Rec_text.txt', 'wt') as out:
        poryadok = text_read()
        for text in poryadok:
            out.write(f"{text['name']}\n")
            out.write(f"{str(text['size'])}\n")
            out.writelines(f"{''.join(text['content'])}\n")
    print('Запись выполнена успешно')

text_rec()