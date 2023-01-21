# COMP-5800-Yidong-Huang and Devansh-Mody
This dataset contains hate speech sentences in English. It has 451709 sentences in total. 371452 of these are hate speech, and 80250 are non-hate speech. 

The dataset is organized into folders as follows:

0_RawData contains data collected from different sources to assemble a dataset of hate speech sentences.

1_ContractionProfanitiesEnglish contains commonly used contractions and a list of profanities used in the English language.

2_PreprocessedData contains the final_preprocessed_data_yidong_devansh.csv file with sentences generated by the following process:
1. Removing multiple spaces, hyperlinks, user mentions, emojis, and emoticons converted to text, and removed new line characters;
2. After all these characters were removed, the contractions found in the text were expanded. Grammatical errors were corrected using the word mover's distance between sentences generated from contraction with multiple possibilities using the Google News Word2Vectors [https://code.google.com/archive/p/word2vec/] and the opensource Gensim mode [https://radimrehurek.com/gensim/models/word2vec.html];
3. Removing date and time values;
4. Removing accented numbers and characters (e.g., ^ea, or ^12);
5. The remaining numbers are converted to words;
6. Removing ampersands from the beginning of words;
7. Removing the following characters (_"\-;%()|+&=*%.,!?:#$@[]/) from the text;
8. Generating an intermediate file preprocessed_data_yidong_devansh.csv;
9. Replacing misspelled profanities from the text with correctly spelled versions based on the Profanities.csv file;
10. Generating the final_preprocessed_data_yidong_devansh.csv.

3_DataAugmentationAndBERTVocab
Final_Y_D_data.csv was used to generate the YD_aug_data_balanced.csv file by downsampling the class with more samples.

4_PretrainedBERT Contains the custom BERT tokenizer vocabulary and configuration.

5_TrainValidationFolds Contains the training data and validation folds for a 5-Fold CrossValidation scheme.

6_MissclassifiedBERT2DataFolds Contains sentences that were misclassified by the HS-Bert Model and their true labels

7_BILSTM-model1 Contains the Keras embedding layer for the BILSTM-model1 network.

8_BILSTM-model2 Contains the word embeddings for the BILSTM-model2 network.

9_TFIDF Contains the TF-IDF vectors for the logistic regression and decision tree models.

10_GabAndRedditComparison contains the training and test files for comparison with the authors from [Jing Qian, Anna Bethke, Yinyin Liu, Elizabeth Belding, and William Yang Wang, "A Benchmark Dataset for Learning to Intervene in Online Hate Speech", arXiv:1909.04251v1 [cs.CL] 10 Sep 2019.].

–

The curated dataset is a combination of the following data sources:

* https://huggingface.co/datasets/5roop/FRENK-hate-hr
* https://huggingface.co/datasets/viewer/?dataset=hatespeech18
* https://data.mendeley.com/datasets/jf4pzyvnpj/1
* https://www.chatcoder.com/data.html
* https://www.kaggle.com/mrmorj/hate-speech-and-offensive-language-dataset
* https://www.kaggle.com/usharengaraju/dynamically-generated-hate-speech-dataset
* https://www.kaggle.com/arkhoshghalb/twitter-sentiment-analysis-hatred-speech
* https://www.kaggle.com/surekharamireddy/malignant-comment-classification
* https://www.kaggle.com/munkialbright/classified-tweets
* https://hasocfire.github.io/hasoc/2019/dataset.html
* https://github.com/cardiffnlp/tweeteval
* https://github.com/tazeek/BullyDetect
* https://www.kaggle.com/c/detecting-insults-in-social-commentary/data
* https://github.com/t-davidson/hate-speech-and-offensive-language
* https://github.com/HKUST-KnowComp/MLMA hate speech/blob/master/hate speech mlma.zip
* https://www.kaggle.com/vkrahul/twitter-hate-speech
* https://www.kaggle.com/pandeyakshive97/hate-speech-dataset
* https://www.kaggle.com/eldrich/hate-speech-offensive-tweets-by-davidson-et-al

The following sources were used for the expansion of contractions found in the text:

* https://en.wikipedia.org/wiki/Wikipedia:List\_of\_English\_contractions
* https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python
* https://github.com/kootenpv/contractions/tree/master/contractions/data
* https://7esl.com/contractions-list/
* https://www.eslbuzz.com/popular-contractions/
* https://www.netlingo.com/acronyms.php
* https://grammar.yourdictionary.com/slang/texting-slang.html
* https://www.noslang.com/dictionary/
