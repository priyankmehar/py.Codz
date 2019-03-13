# Packages
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.base import BaseEstimator

# Read Impute Source file
SrcImpute = pd.read_csv('D:\GitHUB\Imputer\SourceImpute.csv')

SrcImpute.head()
SrcImpute.dtypes

8# Percentage of missing values in the source
SrcImpute_NaN = (SrcImpute.isnull().sum()/SrcImpute.shape[0])*100
columns = SrcImpute.columns
missing_value_SrcImpute = pd.DataFrame({'column_name': columns,'percent_missing': SrcImpute_NaN})
print(missing_value_SrcImpute)

#Custom Impute function 

 class MehImputer(BaseEstimator, TransformerMixin):
    def __init__(self, strategy='mean',filler='NA'):
       self.strategy = strategy
       self.fill = filler

    def fit(self, X, y=None):
       if self.strategy in ['mean','median']:
           if not all(X.dtypes == np.number):
               raise ValueError('dtypes mismatch np.number dtype is \
                                 required for '+ self.strategy)
       if self.strategy == 'mean':
           self.fill = X.mean()
       elif self.strategy == 'median':
           self.fill = X.median()
       elif self.strategy == 'mode':
           self.fill = X.mode().iloc[0]
       elif self.strategy == 'fill':
           if type(self.fill) is list and type(X) is pd.DataFrame:
               self.fill = dict([(cname, v) for cname,v in zip(X.columns, self.fill)])
       return self

    def transform(self, X, y=None):
       return X.fillna(self.fill)
 
    
ModeOut = MehImputer(strategy='mode').fit_transform(SrcImpute)
ModeOut.count()
ModeOut.head()
