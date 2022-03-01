def pl_sentence(sentence):
    new_word = [f"{word}ay" if word[0] in 'aeiou' else f"{word[1:]}{word[0]}ay"
            for word in sentence.split()]
    return ' '.join(new_word)


def pl_sentence_bs(sentence):
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(output)



def nonsensical_sentence(text_file, line_start):
    count1 = 0
    count2 = 0
    with open(text_file, 'r') as tf:
        for line in tf.readlines():
            if count1 >= line_start:
                if len(line.split()) > 9:
                    print(line.split()[4], end=' ')
                    if count2 == 9:
                        break
                    count2 += 1
            count1 += 1


def string_transpose(frases):
    index = 0
    new_list= list()
    for n in range(len(frases)):
        nf = str()
        for frase in frases:
            if index < len(frase.split()):
                nf += f"{frase.split()[index]} "
        new_list.append(nf)
        index += 1
    for x in new_list:
        print(x.strip())


def read_logfile(logfile):
    with open(logfile, 'r') as lf:
        for line in lf.readlines():
            if "404" in line:
                print(line.strip().split()[0])


read_logfile("./access.log")

