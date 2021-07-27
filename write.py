import json
def generate_question():
    # Squad Question
    result = []
    squad_data = json.loads(open('./train-v2.0.json').read())
    squad_data = squad_data['data']
    for data in squad_data:
        for elem in data['paragraphs']:
            qas, context = elem['qas'], elem['context']
            for q in qas:
                question = q['question']
                question = question.split()
                try:
                    if (question[0] == 'What' or question[0] == 'Who') and (question[1] == 'is' or question[1] == 'are') and question[2] == 'the':
                        temp = ' '.join(question[4:])
                        if temp: result.append(temp)
                except:
                    pass
                if question[0] == 'Where' or question[0] == 'When':
                    temp = ' '.join(question[1:])
                    if temp: result.append(temp)
    
    print('Squad', len(result))

    # wiki.answers.com
    # from os import listdir
    # from os.path import isfile, join
    # mypath = '../data/QA'
    # onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
    # for f in onlyfiles:
    #     try:
    #         data = json.loads(open(f).read())
    #         for d in data:
    #             question = d['Question']
    #             question = question.split()
    #             if len(question) > 20: continue
    #             try:
    #                 if (question[0] == 'What' or question[0] == 'Who') and (question[1] == 'is' or question[1] == 'are') and question[2] == 'the':
    #                     temp = ' '.join(question[4:])
    #                     if temp: result.append(temp)
    #             except:
    #                 pass
    #             if question[0] == 'Where' or question[0] == 'When':
    #                 temp = ' '.join(question[1:])
    #                 if temp: result.append(temp)
    #     except:
    #         pass
    # print('All', len(result))
    return result

fin = open('./output.txt', 'w')
questions = generate_question()
print('\n'.join(questions), file=fin)
fin.close()