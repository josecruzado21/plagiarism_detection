#argparse allows to define parameters to use in our custom model
import argparse
#joblib permits to save the model artifacts after training
import joblib
import os
import pandas as pd

from sklearn.svm import SVC

#Because the SageMaker imports your training script, you should put your training code in a main guard (if __name__=='__main__':) if you are using the same script to host your model, so that SageMaker does not inadvertently run your training code at the wrong point in execution.
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    
    #hyperparameters that the client has to sent when calling the model
    parser.add_argument('--kernel',type=str,default='linear')
    
    #Data, model and output directories
    
    #filesystem path to write output artifacts to. Output artifacts may include checkpoints, graphs, and other files to save, not including model artifacts.
    parser.add_argument('--output-data-dir',type=str,default=os.environ.get('SM_OUTPUT_DATA_DIR'))
    
    #the path to the directory to write model artifacts to. These artifacts are uploaded to S3 for model hosting.
    parser.add_argument('--model-dir',type=str,default=os.environ.get('SM_MODEL_DIR'))
    
    #directory containing data in train and test channel
    parser.add_argument('--train',type=str,default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--test',type=str,default=os.environ.get('SM_CHANNEL_TEST'))
    
    #keep only the known parameters and ignore any extra parameter included
    args,_=parser.parse_known_args()
    
    # Read in csv training file
    training_dir = args.train
    train_data = pd.read_csv(os.path.join(training_dir, "train.csv"), header=None, names=None)
    train_y = train_data.iloc[:,0]
    train_x = train_data.iloc[:,1:]
    
    clf=SVC(kernel=args.kernel)
    clf.fit(train_x,train_y)
    
    #to train the model and save it to the model directory
    joblib.dump(clf,os.path.join(args.model_dir, "model.joblib"))
                        

def model_fn(model_dir):
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf