# Plagiarism Detection

The purpose of this project is to train (and test) and algorithm for plagiarism detection based on the dataset created by [Clough and Stevenson (2011)](https://link.springer.com/article/10.1007/s10579-009-9112-1).

Clough and Stevenson constructed a corpus consisting of answers in which plagiarism was simulated. The main benefit of this dataset is the inclusion of 4 different types of plagiarism: Near copy, Light revision, Heavy revision, Non-plagiarised. 

The creation of this datased tackled the persistent problem in the plagiarism detection literature of null access to genuine examples of plagiarised work.

## Background

Plagiarism is an increasing problem for education institutions.  There exist some tools to help in its detection; however, testing its effectiveness is a challenge when there is no access to reliable data.

The task of building tools to detect plagiarised work is not straightforward due to the problems of obtaining real examples of plagiarised text. As stated by Clough and Stevenson (2011), the main problems that hamper obtaining reliable plagiarism labelled data are:
* Plagiarised text is not intended to be identified and plagiarists are unlikely to admit their act.

* If a plagiarised text is detected, because of legally and ethics issues, it may not be freely available.

## The Dataset

The dataset used in this project is a modified version of the one create by Paul Clough and Mark Stevenson. The complete description of the data generation process is described in their [research article](https://link.springer.com/article/10.1007/s10579-009-9112-1) (Clough, P., Stevenson, M. Developing a corpus of plagiarised short answers, 2011)

## Description of the dataset

<li> The dataset contains several txt files whose characteristics are summarized in the file_information.csv file. </li>
<li> The data file is composed of 100 text documents, out of which 5 contain the answers of the original source. Therefore, the participants contributed with 95 anwers, divided in 5 tasks and 5 plagiarism methods. </li>
<li> The <b>File</b> column in the file_information.csv file contains the name of the txt file. </li>
<li> The <b>Task</b> column contains one of the five learning task (A-E) that each txt answers. </li>
<li> The <b>Category</b> column indicates if the participant was asked to use a Near copy (cut), Light revision (light), Heavy revision (heavy) or Non-plagiarised (non) method to answer the question. This column also contains the 'orig' category to reference the original texts on which participants based their answers</li>

>For more details in the above mentioned points, please refer to the research document (pages 9-12)

## Similarity Features

Two measures of similarity will be used as features to predict plagiarism: containment and largest common subsequence.

### Containment

Containment is a measure of text similarity proposed by Andrei Broder in his paper "On the resemblance and containment of documents".
The containment of two documents A and B is a number between 0 and 1 that contains the proportion of A's unique n-grams that are also in B.

Formally, containment is:

</br>
<p align="center">
<img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\inline&space;C_n(A,B)=\frac{|S(A,n)\:\cap\:S(B,n)|}{|S(A,n)|}" title="\inline C_n(A,B)=\frac{|S(A,n)\:\cap\:S(B,n)|}{|S(A,n)|}" />
</p>

Where <img src="https://latex.codecogs.com/png.image?\dpi{100}&space;\inline&space;S(A,n)" title="\inline S(A,n)" /> and <img src="https://latex.codecogs.com/png.image?\dpi{100}&space;\inline&space;S(B,n)" title="\inline S(B,n)" /> represent the set of n-grams for document A and B respectively.

The numerator is the intersection of unique n-grams between documents A and B. The denominator equals the number of unique n-grams in document A.


### Longest Common Subsequence (LCS)

LCS between two strings is the longest subsequence that is common to both strings. To be considered a subsequence, the words should not necessarily be in consecutive order.


## Deployment in AWS

The final model is trained and deployed in Amazon Sagemaker