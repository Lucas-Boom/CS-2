import string
import matplotlib.pyplot as plt
import numpy as np

'''
Author: Lucas Boom 
Date: 2/18/26
Description: Analyzes two shakespearean plays and finds the top 10 words while filtering out unnecessary words
List of completed functions: julius_caesar, the_tempest
Log: 1.0
'''
def julius_caesar(fname):

    #fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()

    counts = dict() #creates a dictionary
    for line in fhand: #for loop
        line = line.rstrip() #deletes extra/trailing spaces at the end of words
        # First two parameters are empty strings
        line = line.translate(line.maketrans("", "", string.punctuation)) #removes punctuation
        line = line.lower() #converts everything to lowercase
        words = line.split() #splits the string(text) using spaces as seperators so can assign values to each word
        for word in words: #for loop
            if word in ['and', 'the', 'that', 'this', 'how', 'then', 'an', 'to', 'i', 'about', 'with', 'in', 'am', 'when', 'so', 'who', 'his', 'at', 'be', 'one', 'from', 'or', 'we', 'can', 'out', 'other', 'by', 'had', 'but', 'some', 'of', 'a', 'not', 'is', 'you', 'it', 'he', 'me', 'my', 'for', 'him', 'will', 'have', 'as', 'do', 'your', 'what', 'shall', 'thou', 'all', 'are', 'no', 'our', 'if', 'on', 'come', 'did', 'o', 'good', 'know', 'let', 'was', 'well', 'they', 'now', 'us', 'their', 'them', 'thy', 'thee', 'here', 'upon', 'there', 'which', 'would', 'go', 'why', 'than', 'should', 'yet', 'men', 'speak', 'these', 'like', 'cinna']:  #filters out these words
                pass
            else:
                if word not in counts: #set the filtered words out with the number of 1, regardless of how many times it showed up
                    counts[word] = 1
                else: 
                    counts[word] += 1 #if not in filtered words list, add 1
    sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)) #sorts the words by frequency
        
    #top_15 = list(sorted_dict.items())[:15]


    #newdict = ", ".join(f"{k}: {v}" for k, v in top_15)

    #print (newdict)
    
    data = []
    labels = []

    for key, value in sorted_dict.items():
        if value > 38: #filters out any words that show up less than 41 times

            labels.append(key)
            data.append(value)
    plt.pie(data, labels = labels) #creates a graph
    plt.title("Most Words Used in Julius Caesar")
    plt.show() 



def the_tempest(fname):

    #fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()

    counts = dict() #creates a dictionary
    for line in fhand: #for loop
        line = line.rstrip() #deletes extra/trailing spaces at the end of words
        # First two parameters are empty strings
        line = line.translate(line.maketrans("", "", string.punctuation)) #removes punctuation
        line = line.lower() #converts everything to lowercase
        words = line.split() #splits the string(text) using spaces as seperators so can assign values to each word
        for word in words: #for loop
            if word in ['and', 'the', 'that', 'this', 'how', 'then', 'an', 'to', 'i', 'about', 'with', 'in', 'am', 'when', 'so', 'who', 'his', 'at', 'be', 'one', 'from', 'or', 'we', 'can', 'out', 'other', 'by', 'had', 'but', 'some', 'of', 'a', 'not', 'is', 'you', 'it', 'he', 'me', 'my', 'for', 'him', 'will', 'have', 'as', 'do', 'your', 'what', 'shall', 'thou', 'all', 'are', 'no', 'our', 'if', 'on', 'come', 'did', 'o', 'good', 'know', 'let', 'was', 'well', 'they', 'now', 'us', 'their', 'them', 'thy', 'thee', 'here', 'upon', 'there', 'which', 'would', 'go', 'why', 'than', 'should', 'yet']:  #filters out these words
                pass
            else:
                if word not in counts: #set the filtered words out with the number of 1, regardless of how many times it showed up
                    counts[word] = 1
                else: 
                    counts[word] += 1 #if not in filtered words list, add 1
    sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)) #sorts the words by frequency
    #top_15 = list(sorted_dict.items())[:15]


    #newdict = ", ".join(f"{k}: {v}" for k, v in top_15)

    #print (newdict)
    
    data = []
    labels = []

    print(sorted_dict)

    for key, value in sorted_dict.items():
        if value > 30: #filters out any words that show up less than 30 times

            labels.append(key)
            data.append(value)
    plt.pie(data, labels = labels) #creates a graph
    plt.title("Most Words Used in The Tempest")
    plt.show()
    

def main():

    while True:
        option = input('''What would you like to do? 
                       1. Julius Ceasar 
                       2. The Tempest''') #allows user to pick option of play wanting to analyze
        
        if option == "1":
            julius_caesar("Julius_Caesar.txt")
        elif option == "2":
            the_tempest("The_Tempest.txt")
        else:
            print("Invalid option, try again.")
   
main()
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   

    
