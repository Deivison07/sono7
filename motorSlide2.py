#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
coisas = []
def legenda(opc):
        global coisas
    
        dicionario = {}
        dicionario['nao ha legenda']='nao ha legenda'
        coisa = []

        try:
            
            arq = open(opc, 'r', encoding='utf-8')    
            texto = arq.readlines()
        
            for linha in texto:
                s = linha
                if s != '\n':
                    coisa.append(linha)
                    
            arq = open(opc, 'w', encoding='utf-8')    
            arq.writelines(coisa)
            arq.close()

            dicionario = {}
            milesimos = []
            indice = 0
            arq = open(opc,'r', encoding='utf-8')
            texto = arq.readlines()
            items = len(texto)
            '''
                primeiro parametro do range()
                modificando o primeiro parametro para zero (0) lista-se a numeração
                modificando o primeiro parametro para zero (1) lista-se os tempos
                modificando o primeiro parametro para zero (2) lista-se os textos
            '''
            for linha in range(1,items,3):
            
                s = (texto[linha])
    
                ''' fatiando a string que contem os tempos de cada frase '''
                item=s.split(' --> ')
    
                ''' subtraindo o tempo de finalização pelo tempo de iniciação para saber
                qual é a duração de cada frase
                '''
                temp = (item[0])
                '''
                transformando o bloco do tipo (tempo) para string
                '''
                bloco = str(temp)
                '''
                fatiando o bloco para manipular os minutos e segundos
                '''
                fatia = bloco.split(':')
                horas = int(fatia[0])
                minutos = int(fatia[1])
                sep = fatia[2].split(',')
        
                seg = int(sep[0])
                mile = int(sep[1])
        
                minu =(minutos + horas*60)
                segun = (minu*60 + seg)
                milesimos.append((mile + (segun*1000)))
                
            xx = []
        
            for linha in range(2,items,3):
                
        
                    s = (texto[linha])
                    dicionario[s]=milesimos[indice]
                    indice = indice+1
                    xx.append(s)
                    
            coisas = xx
            
              
            return(dicionario)
        
        except Exception:
            pass
            
