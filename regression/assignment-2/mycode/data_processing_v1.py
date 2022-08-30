import pandas as pd
from feature_engine.encoding import OrdinalEncoder
from feature_engine.imputation import CategoricalImputer
from feature_engine.encoding import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from feature_engine.selection import DropDuplicateFeatures
from sklearn.ensemble import GradientBoostingRegressor
from feature_engine.selection import RecursiveFeatureElimination
from feature_engine.selection import RecursiveFeatureAddition
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import GridSearchCV

__version__ = 'v1'

class Data:
    def __init__(self, test_path, train_path):
        # read data
        self.test_data = pd.read_csv(test_path)
        self.train_data = pd.read_csv(train_path)
        # save ids of training set and test set
        self.train_ids = self.train_data['Id']
        self.test_ids = self.test_data['Id']
        
        # Ids is not nessessary for the training steps
        self.train_data.drop("Id", axis = 1, inplace = True)
        self.test_data.drop("Id", axis = 1, inplace = True)
        
        #save SalePrice of training set
        self.target_train = self.train_data.SalePrice.values
        self.train_data.drop(['SalePrice'], axis=1, inplace=True)
        # self.train_data = self.train_data.reset_index(drop=True)
        # self.test_data = self.test_data.reset_index(drop=True)
        
        
        
    def missing_data_info(self):
        print("Training set: Missing data info:")
        print(self.train_data.isnull().sum().sort_values(ascending=False))
        print("Test set: Missing data info:")
        print(self.test_data.isnull().sum().sort_values(ascending=False))
        
    def print_data_shape(self):
        print("Training set:")
        print(self.train_data.shape)
        print("Test set:")
        print(self.test_data.shape)
    
        
    
    def fill_na(self, features, value):
        for feature in features:
            self.train_data[feature] = self.train_data[feature].fillna(value)
            self.test_data[feature] = self.test_data[feature].fillna(value)
    
    def handle_missing_data(self):
        missing_cols_group1 = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 
                       'FireplaceQu', 'MSSubClass', 'GarageType', 
                       'GarageFinish', 'GarageQual', 'GarageCond']
        self.fill_na(missing_cols_group1, 'None')
        
        self.train_data["LotFrontage"] = self.train_data.groupby("Neighborhood")["LotFrontage"].transform(lambda x: x.fillna(x.median()))
        self.test_data["LotFrontage"] = self.test_data.groupby("Neighborhood")["LotFrontage"].transform(lambda x: x.fillna(x.median()))
        
        missing_cols_group3 = ['GarageYrBlt', 'GarageArea', 'GarageCars', 
                       'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 
                       'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath']
        self.fill_na(missing_cols_group3, 0)
        
        missing_cols_group4 = ['BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2']
        self.fill_na(missing_cols_group4, 'None')
        self.fill_na(['MasVnrType'], 'None')
        self.fill_na(['MasVnrArea'], 0)
        self.fill_na(['MSZoning'], self.train_data['MSZoning'].mode()[0])
        self.fill_na(['Functional'], "Typ")
        
        missing_cols_group5 = ['Electrical', 'KitchenQual', 'Exterior1st', 'Exterior2nd', 'SaleType', 'Utilities']
        imputer =CategoricalImputer(imputation_method='frequent', variables= missing_cols_group5)
        imputer.fit(self.train_data)
        self.train_data = imputer.transform(self.train_data)
        self.test_data = imputer.transform(self.test_data)
        
        
    def preprocessing_data(self):
        fake_nummeric_cols = ['MSSubClass', 'OverallQual', 'OverallCond', 'YrSold', 'MoSold']
        for col in fake_nummeric_cols:
            self.train_data[col] = self.train_data[col].astype(str)
            self.test_data[col] = self.test_data[col].astype(str)
        
        self.train_data['TotalSF'] = self.train_data['TotalBsmtSF'] + self.train_data['1stFlrSF'] + self.train_data['2ndFlrSF']
        self.test_data['TotalSF'] = self.test_data['TotalBsmtSF'] + self.test_data['1stFlrSF'] + self.test_data['2ndFlrSF']
        
        # get numerical columns before encoding
        number_cols = self.train_data.select_dtypes(include=['int64', 'float64']).columns
        
        # Label encoding
        labels_columns_0 = ['OverallQual', 'OverallCond', 'BsmtQual', 'BsmtCond', 
                            'ExterQual', 'ExterCond', 'HeatingQC', 'KitchenQual', 
                            'PoolQC', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 
                            'CentralAir', 'GarageFinish', 'Fence']
        
        ordinal_enc = OrdinalEncoder(encoding_method='arbitrary', variables= labels_columns_0)
        ordinal_enc.fit(self.train_data)
        self.train_data = ordinal_enc.transform(self.train_data)
        self.test_data = ordinal_enc.transform(self.test_data)
        
        # get categorical columns before one-hot encoding
        categorical_cols = self.train_data.select_dtypes(include=['object']).columns
        
        # One-hot encoding
        ohe_enc = OneHotEncoder(top_categories=None, variables=categorical_cols.to_list(),drop_last=False)
        ohe_enc.fit(self.train_data)
        self.train_data = ohe_enc.transform(self.train_data)
        self.test_data = ohe_enc.transform(self.test_data)
        
        # Scale numerical columns
        scaler = StandardScaler()
        scaler.fit(self.train_data[number_cols])
        self.train_data[number_cols] = scaler.transform(self.train_data[number_cols])
        self.test_data[number_cols] = scaler.transform(self.test_data[number_cols])
        
        
    def remove_duplicate_features(self):
        sel = DropDuplicateFeatures(variables=None, missing_values='raise')
        sel.fit(self.train_data)
        self.train_data = sel.transform(self.train_data)
        self.test_data = sel.transform(self.test_data)
        
    def select_features_by_recursive_feature_elimination(self):
        # Khởi tạo mô hình dùng để lựa chọn đặc trưng
        model = GradientBoostingRegressor(n_estimators=10, max_depth=4, random_state=0)

        # Thiết lập trình lựa chọn đặc trưng
        sel = RecursiveFeatureElimination(
            variables=None, # automatically evaluate all numerical variables
            estimator = model, # the ML model
            scoring = 'neg_mean_squared_error', # the metric we want to evalute
            threshold = 0.001, # the maximum performance drop allowed to remove a feature
            cv=3, # cross-validation
        )
        # Tiến hành khớp dữ liệu
        sel.fit(self.train_data, self.target_train)
        return sel.transform(self.train_data), sel.transform(self.test_data)
    
    def select_features_by_recursive_feature_addition(self):
        # Khởi tạo mô hình dùng để lựa chọn đặc trưng
        model = GradientBoostingRegressor(n_estimators=10, max_depth=4, random_state=0)

        # Thiết lập trình lựa chọn đặc trưng
        sel = RecursiveFeatureAddition(
            variables=None, # automatically evaluate all numerical variables
            estimator = model, # the ML model
            scoring = 'neg_mean_squared_error', # the metric we want to evalute
            threshold = 0.001, # the maximum performance drop allowed to remove a feature
            cv=3, # cross-validation
        )
        # Tiến hành khớp dữ liệu
        sel.fit(self.train_data, self.target_train)
        return sel.transform(self.train_data), sel.transform(self.test_data)
        
    
    def select_features_by_lasso(self):
        parameters = {'alpha':[0.01, 1, 10, 100]}
        model = Lasso(normalize=True)
        clf = GridSearchCV(model, parameters, scoring = 'neg_mean_squared_error')
        clf.fit(self.train_data, self.target_train)
        sel = SelectFromModel(Lasso(alpha = clf.best_params_['alpha']))
        sel.fit(self.train_data, self.target_train)
        selected_feat = self.train_data.columns[(sel.get_support())]
        return self.train_data[selected_feat], self.test_data[selected_feat]
        
    
    def run_processing(self):
        print("starting ... \n")
        print("handling missing data ... \n")
        self.handle_missing_data()
        print("preprocessing data... \n")
        self.preprocessing_data()
        print("removing duplicate features ... \n")
        self.remove_duplicate_features()