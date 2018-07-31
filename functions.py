#!-*- coding: utf8 -*-
import json
import re
import csv

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def GravaArquivoLegivel(arquivo_texto):
    saida = open('limpos_teste_ml.csv', 'w')
    saida2 = open('palavras.csv', 'w')
    saida2.writelines('frase;sentimento')
    for linha in arquivo_texto:
        try:                        #linha['user']['screen_name']     linha['id_str']
            saida.writelines('\n' + linha['user']['screen_name'] + ';' + linha['text'].replace('\n', ' ').replace(';', ' '))
            saida2.writelines('\n' +linha['text'].replace('\n', ' ').replace(';', ' ') + ';' + '')
        except:
            continue
    saida.close()
    saida2.close()

def GravaBancos(arquivo_texto):
    saida = open('D:/Projetos/python/trabThais/Bancos.csv', 'w')
    saida.writelines('nome;quantidade')
    tweets_data = []
    tweets_file = open(arquivo_texto, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    Itau = {'Contagem': 0}
    Santander = {'Contagem': 0}
    Bradesco = {'Contagem': 0}
    BancoBrasil = {'Contagem': 0}
    Caixa = {'Contagem': 0}
    Indeterminado = {'Contagem': 0}

    for tweet in tweets_data:
        if 'text' in tweet:
            if word_in_text('Itaú', tweet['text']):
                Itau['Contagem'] += 1
            elif word_in_text('Itau', tweet['text']):
                Itau['Contagem'] += 1
            elif word_in_text('Santander', tweet['text']):
                Santander['Contagem'] += 1
            elif word_in_text('Bradesco', tweet['text']):
                Bradesco['Contagem'] += 1
            elif word_in_text('Banco do Brasil', tweet['text']):
                BancoBrasil['Contagem'] += 1
            elif word_in_text('Caixa', tweet['text']):
                Caixa['Contagem'] += 1
            else:
                Indeterminado['Contagem'] += 1
                continue

    saida.writelines('\n' + 'Itau;' + str(Itau['Contagem']))
    saida.writelines('\n' + 'Santander;' + str(Santander['Contagem']))
    saida.writelines('\n' + 'Bradesco;' + str(Bradesco['Contagem']))
    saida.writelines('\n' + 'Banco Brasil;' + str(BancoBrasil['Contagem']))
    saida.writelines('\n' + 'Caixa;' + str(Caixa['Contagem']))
    saida.writelines('\n' + 'Indeterminado;' + str(Indeterminado['Contagem']))
    saida.close()