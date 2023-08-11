# -*- coding: latin-1 -*-
import pandas as pd
from transformers import *
from pypdf import PdfReader




def consulta(assunto = 'todo', question = '', nlp = None):
    data=''
    question = question




    if (assunto == 'todo'):
        #open text file in read mode
        text_file = open("chavo.txt", "r", encoding='utf8')    
        #read whole file to a string
        data = text_file.read()
        #close file
        text_file.close()

    if (assunto == 'chavo'):
        #open text file in read mode
        text_file = open("chavo.txt", "r", encoding='utf8')
        #read whole file to a string
        data = text_file.read() 
        #close file
        text_file.close()
    

    context = data
    
    
    answer = nlp(
            {
                'question': question,
                'context': context
            }
        )

    return answer['answer']   




    # answer = nlp(    
    #         {
    #             'question': question,
    #             'context': context
    #         })['answer']
    
    # return answer