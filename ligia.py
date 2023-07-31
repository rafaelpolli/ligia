# -*- coding: latin-1 -*-
import pandas as pd
from transformers import *
from pypdf import PdfReader

# nlp = pipeline(
#     'question-answering', 
#     model='mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es',
#     tokenizer=(
#         'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es',  
#         {"use_fast": False}
#     ))

# nlp = pipeline(
#     'question-answering', 
#     model='mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es')

# nlp = pipeline(
#     'question-answering', 
#     model='mrm8488/longformer-base-4096-spanish-finetuned-squad')

# nlp = pipeline(
#     'question-answering', 
#     model='inigopm/beto-base-spanish-squades2')

# nlp = pipeline(
#     'question-answering', 
#     model='PlanTL-GOB-ES/roberta-base-bne-sqac')

# nlp = pipeline(
#     'question-answering', 
#     model='PlanTL-GOB-ES/roberta-large-bne-sqac')



def consulta(assunto = 'todo', question = ''):
    data=''
    question = question

    modelos = ['mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es',
           'mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es',
           'mrm8488/longformer-base-4096-spanish-finetuned-squad',
           'inigopm/beto-base-spanish-squades2',
           'PlanTL-GOB-ES/roberta-base-bne-sqac',
           'PlanTL-GOB-ES/roberta-large-bne-sqac']
    x = 0


    if (assunto == 'todo'):
        #open text file in read mode
        text_file = open("volar.txt", "r", encoding='utf8')    
        #read whole file to a string
        data = text_file.read()
        #close file
        text_file.close()

    if (assunto == 'volar'):
        #open text file in read mode
        text_file = open("volar.txt", "r", encoding='utf8')
        #read whole file to a string
        data = text_file.read() 
        #close file
        text_file.close()
    

    context = data
    
    
    reader = PdfReader("RNRCSF.pdf")
    text = ""
    for page in reader.pages:
       text += page.extract_text() + "\n"

    context = text[:10000]

    df = pd.DataFrame()

    for i in modelos:       
        nlp = pipeline(
            'question-answering', 
            model=i
        )
        
        answer = nlp(
            {
                'question': question,
                'context': context
            }
        )
        print(x)
        answer['model'] = x
        x = x + 1
        df = pd.concat([df, pd.DataFrame(answer.values(), answer.keys()).T])

    return df.sort_values('score', ascending = False).to_html()   




    # answer = nlp(    
    #         {
    #             'question': question,
    #             'context': context
    #         })['answer']
    
    # return answer