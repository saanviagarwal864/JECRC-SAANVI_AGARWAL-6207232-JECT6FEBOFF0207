'''
Word Frequency Counter
'''
class Solution:
    def word_frequency(self, sentence):
        words=sentence.split()
        dict={}

        for i in words:
            if i in dict:
                dict[i]=dict[i]+1
            else:
                dict[i]=1
                
        return dict            
        