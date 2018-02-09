# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:51:34 2017

@author: krish
"""

import math
import nltk
import csv
from nltk import FreqDist

names = [] #list to hold names of the speakers
people = {}#dictionary to hold sentences of each speaker
people_bigrams = {}#dictionary to hold bigrams of each speaker
words = {}#dictionary to hold words of each speaker
bigram_words = {}#dictionary to hold bigrams of each speaker
word_count = {}#dictionary of word count of each speaker
bigram_word_count = {}#dictionary of bigram word count of each speaker
doc_count = {}#dictionary of doc/sentence count of each speaker
prior_count = {}#dictionary of prior count of each speaker

#function to calculate length of unique vocabulary               
def vocab_length():
  all_words=[]
  for array in words.values():
    for word in array:
      all_words.append(word)
  length=len(list(set(all_words)))
  return length

#function to calculate prior count value of each speaker
def prior_calc():
  for name in names:
    prior_count.setdefault(name,0)
    prior_count[name]=doc_count[name]/(sum(doc_count.values()))
  return prior_count

#naive bayes implementation using words as features
def naive_bayes():
  file = open('train','r')
  
  for line in file:
    if nltk.word_tokenize(line)[0] not in names:
      names.append(nltk.word_tokenize(line)[0])
    line=line.split(' ')
    #removing special characters,spaces and newlines
    line=[''.join(c for c in s if c not in [',','.','?',':',';','!']) for s in line]
    line=[s for s in line if s!='' and s!='\n']
  
  #storing sentences of each speaker in a dictionary
    if(line[0] not in people):
      people.setdefault(line[0],[])
    people[line[0]].append(line[1:])
  
  probabilities_train={}
  word_prob={}
  
  #claculating word and doc counts
  for name in names:
    temp1=[]
    temp2=[]
    word_count.setdefault(name,0)
    words.setdefault(name,[])
    doc_count.setdefault(name,0)
    for array in people.get(name):
      temp2.append(array)
      for word in array:
        temp1.append(word)
        words[name].append(word)
    word_count[name]=len(temp1)
    doc_count[name]=len(temp2)
    
  
  prior_count=prior_calc()
  prob_count=0
  
  V=vocab_length()
  
  #claculating probability values of each word for each speaker using naive bayes formula
  for name in names:
    probabilities_train.setdefault(name,{})
    word_prob={}
    for word in list(set(words[name])):
      a=words[name].count(word)+0.2 #calculating count of each word spoken by the speaker
      b=word_count[name]+(V*0.2)#calculating total number of words spoken by each speaker alog with length of unique vocab count for all users
      prob_count=a/b
      word_prob[word]=prob_count#storing prob count for each word
    word_prob[' ']=1/(word_count[name]+(V*0.2))#prob of a word not spoken by a speaker
    probabilities_train[name]=word_prob#assigning entire dictionary to a key (dictionary of dictionary)    
                       
  #storing most common 20 words for each speaker to plot graphs in R
  f=open("prob_values.csv","w")
  f.write("Classes,Top 20 Words,Word probabilities\n")
  for name in names:
    fd= FreqDist(words[name])
    for k,v in fd.most_common(20):
      temp=name+","+k+","+str(v)+"\n"
      f.write(temp)

  #classfying each sentence in test set
  probabilities_test={}
  for name in names:
    probabilities_test.setdefault(name,[])
    file = open('test','r')
    for line in file: 
      #splitting lines into lists,removing special characters,spaces and new lines
      line=line.split(' ')
      line=[''.join(c for c in s if c not in [',','.','?',':',';']) for s in line]
      line=[s for s in line if s!='' and s!='\n']
      temp=[]
      for test_word in line[1:]: 
        #fetching probability of word if its present in training set
        if(test_word in probabilities_train.get(name)):
          temp.append(math.log(probabilities_train.get(name)[test_word]))
          #if not present in training
        else:
          temp.append(math.log(probabilities_train.get(name)[' ']))
      #adding prob values of each word present in a line
      a=(sum(temp)+math.log(prior_count[name]))
      probabilities_test[name].append(a)
  
  #calculating the max probablility of each line and storing the speaker of that line
  sentence_speaker = ''
  predicted_speakers = []
  for i in range(400):
    highest = probabilities_test.get('sanders')[i] #randomly assigning a value initially
    for k, v in probabilities_test.items():
      if v[i]>=highest:
        highest = v[i]
        sentence_speaker = k
    predicted_speakers.append(sentence_speaker) #store  predicted speakers into a array
    
  #calculating accuracy percentile by checking if predicted speakers match the starting name in test file and printing it                             
  total_test_doc_count = 0
  correct_prediction_count = 0
  file = open('test','r')
  for line in file:
    line=line.split(' ')
    if(line[0] == predicted_speakers[total_test_doc_count]):
      correct_prediction_count += 1
    total_test_doc_count += 1
        
  print("Accuracy of Naive Bayes is ", ((correct_prediction_count/total_test_doc_count)*100),"%")
  
def binarized_naive_bayes():
  file = open('train','r')

  #storing names into a array and removing whitespaces, newlines and special characters
  for line in file:
    if nltk.word_tokenize(line)[0] not in names:
      names.append(nltk.word_tokenize(line)[0])
    line=line.split(' ')
    line=[''.join(c for c in s if c not in [',','.','?',':',';','!']) for s in line]
    line=[s for s in line if s!='' and s!='\n']
  
    if(line[0] not in people):
      people.setdefault(line[0],[])
    people[line[0]].append(line[1:])
  
  probabilities_train={}
  word_prob={}
  
  #calculating and storing doc and word count for each speaker
  for name in names:
    temp1=[]
    temp2=[]
    word_count.setdefault(name,0)
    words.setdefault(name,[])
    doc_count.setdefault(name,0)
    for array in people.get(name):
      temp2.append(array)
      for word in list(set(array)):
        temp1.append(word)
        words[name].append(word)
    word_count[name]=len(temp1)
    doc_count[name]=len(temp2)
    
  prior_count=prior_calc()
  V=vocab_length()
  prob_count=0
  
  #claculating probability values of each word for each speaker using naive bayes formula
  for name in names:
    probabilities_train.setdefault(name,{})
    word_prob={}
    for word in list(set(words[name])):#each word appearing exactly once in a sentence spoken by a speaker as dictated in binarized naive bayes
      a=words[name].count(word)+0.2#calculating count of each word spoken by the speaker
      b=word_count[name]+(V*0.2)#calculating total number of words spoken by each speaker alog with length of unique vocab count for all users
      prob_count=a/b
      word_prob[word]=prob_count#storing probability value for each word
    word_prob[' ']=1/(word_count[name]+(V*0.2))#if word not present in training set
    probabilities_train[name]=word_prob               
  
  #calculating log probabilities of each words present in test case
  probabilities_test={}
  for name in names:
    probabilities_test.setdefault(name,[])
    file = open('test','r')
    for line in file: 
      #tokenizing, removing whitespaces, special characters and new lines in test
      line=line.split(' ')
      line=[''.join(c for c in s if c not in [',','.','?',':',';']) for s in line]
      line=[s for s in line if s!='' and s!='\n']
      temp=[]
      for test_word in line[1:]:   
        #fetching probability values if test word is present in training
        if(test_word in probabilities_train.get(name)):
          temp.append(math.log(probabilities_train.get(name)[test_word]))
        else:
          #if word is not present in training
          temp.append(math.log(probabilities_train.get(name)[' ']))
      #summing up prob values of each word until a end of sentence is reached
      a=(sum(temp)+math.log(prior_count[name]))
      probabilities_test[name].append(a)
      
  #storing predicted speaker values into a list    
  sentence_speaker = ''
  predicted_speakers = []
  for i in range(400):
    highest = probabilities_test.get('sanders')[i]#randomly initialising highest to a value
    for k, v in probabilities_test.items():
      if v[i]>=highest:
        highest = v[i]
        sentence_speaker = k
    predicted_speakers.append(sentence_speaker)
    
  #calculating accuracy percentile 
  total_test_doc_count = 0
  correct_prediction_count = 0
  file = open('test','r')
  for line in file:
    line=line.split(' ')
    if(line[0] == predicted_speakers[total_test_doc_count]):
      correct_prediction_count += 1
    total_test_doc_count += 1
        
  print("Accuracy of Binarized Naive Bayes is ", ((correct_prediction_count/total_test_doc_count)*100),"%")

def bigrams_naive_bayes():
  names = []#list to hold names of speakers
  people = {}#dict to hold sentences of each speaker
  people_bigrams = {}#dict to hold bigrams of sentences
  words = {}#dict holding words of speakers
  bigram_words = {}
  word_count = {}#dict holding word counts of speakers
  bigram_word_count = {}
  doc_count = {}#dict holding doc count
  prior_count = {}#dict holding prior count of speakers
  file = open('train', 'r')
  
  #removing special characters, whitespaces and new line
  for line in file:
      if nltk.word_tokenize(line)[0] not in names:
          names.append(nltk.word_tokenize(line)[0])
      line = line.split(' ')
      line = [''.join(c for c in s if c not in [',', '.', '?', ':', ';', '!']) for s in line]
      line = [s for s in line if s != '' and s != '\n']
      
      #contstructing dict to hold sentences of speakers
      if (line[0] not in people):
          people.setdefault(line[0], [])
          people_bigrams.setdefault(line[0], [])
      people[line[0]].append(line[1:])
      people_bigrams[line[0]].append(nltk.bigrams(line[1:]))
  
  probabilities_train = {}
  word_prob = {}
  
  #calculating doc,word and bigram count
  for name in names:
      temp1 = []
      temp2 = []
      temp3 = []
      word_count.setdefault(name, 0)
      words.setdefault(name, [])
      bigram_words.setdefault(name, [])
      doc_count.setdefault(name, 0)
      for array, array2 in zip(people.get(name), people_bigrams.get(name)):
          temp2.append(array)
          for word in array:
              temp1.append(word)
              words[name].append(word)
          for bigram in array2:
              temp3.append(bigram)
              bigram_words[name].append(bigram)
      word_count[name] = len(temp1)
      bigram_word_count[name] = len(temp3)
      doc_count[name] = len(temp2)
  
  #prior calculation
  for name in names:
      prior_count.setdefault(name, 0)
      prior_count[name] = doc_count[name] / (sum(doc_count.values()))
  
  all_words = []
  for array in words.values():
      for word in array:
          all_words.append(word)

  V = len(list(set(all_words)))
  
  prob_count = 0
  
  #constructing probabilities of training set
  for name in names:
      probabilities_train.setdefault(name, {})
      word_prob = {}
      for word in list(set(bigram_words[name])):
          a = bigram_words[name].count(word) + 0.2
          b = words[name].count(word[0]) + (V * 0.2)
          prob_count = a / b
          word_prob[word] = prob_count
      word_prob[' '] = 0.2 / (bigram_word_count[name] + (V * 0.2))
      probabilities_train[name] = word_prob
  
  #predicting speakers based on bigrams of sentences
  probabilities_test = {}
  for name in names:
      probabilities_test.setdefault(name, [])
      file = open('test', 'r')
      for line in file:
          line = line.split(' ')
          line = [''.join(c for c in s if c not in [',', '.', '?', ':', ';']) for s in line]
          line = [s for s in line if s != '' and s != '\n']
          bigram_line = nltk.bigrams(line[1:])
          temp = []
  
          for test_bigram in bigram_line:
              if (test_bigram in probabilities_train.get(name)):
                  temp.append(math.log(probabilities_train.get(name)[test_bigram]))
              else:
                  temp.append(math.log(probabilities_train.get(name)[' ']))
                  #summing up probabilities of test words and adding lof of prior count
          a = (sum(temp) + math.log(prior_count[name]))
          probabilities_test[name].append(a)
  
  #storing predicted speakers of each sentence/document into an array
  sentence_speaker = ''
  predicted_speakers = []
  for i in range(400):
      highest = probabilities_test.get('sanders')[i]
      for k, v in probabilities_test.items():
          if v[i] >= highest:
              highest = v[i]
              sentence_speaker = k
      predicted_speakers.append(sentence_speaker)
  
  #calculating accuracy percentile
  total_test_doc_count = 0
  correct_prediction_count = 0
  file = open('test', 'r')
  for line in file:
      line = line.split(' ')
      if (line[0] == predicted_speakers[total_test_doc_count]):
          correct_prediction_count += 1
      total_test_doc_count += 1
  
  print("Accuracy of Naive Bayes using Bigrams as features ", ((correct_prediction_count / total_test_doc_count) * 100),"%")

naive_bayes()
binarized_naive_bayes()
bigrams_naive_bayes()

  
