from sklearn.model_selection import train_test_split

from sklearn.metrics import (mean_absolute_error,mean_squared_error,
                            mean_squared_log_error,median_absolute_error)

from typing import Dict
import pandas as pd

model_dict:Dict={}
metrics_dict={
    "mae":mean_absolute_error,
    "mse":mean_squared_error,
    "rmse":lambda y_act,y_pred:mean_squared_error(y_act,y_pred)**0.5,
    "maae":median_absolute_error
}

def feature_importance(trained_models,kind="linear"):
    df=pd.DataFrame()
    for k,v in trained_models.items():
        if hasattr(v,'feature_importances_'):
            print(f"Tree based Features-{k}")
            df[k]=v.feature_importances_
        if hasattr(v,'coef_'):
            print(f'linear models coefficients-{k}')
            df[k]=v.coef_
    # if kind=="linear":
    #     for k,v in model_dict.items():
    #         df[k]=v.coeff_
    # if kind=="tree":
    #     for k,v in model_dict.items():
    #         df[k]=v.feature_importance
    return df
    

def evaluate(trained_model_dict,data_dict,metrics_dict:Dict=metrics_dict):
    res_metrics={}
    for name,model in trained_model_dict.items():
        y_pred=model.predict(data_dict['X_test'])
        one_model_metric={}
        for m_name,metric in metrics_dict.items():
            one_model_metric[m_name]=metric(data_dict['y_test'],y_pred)
        res_metrics[name]=one_model_metric
    return res_metrics

def train(model_dict,data_dict):
    trained_model_dict={}
    for name,model in model_dict.items():
        print(f"training ..{name}")
        trained_model_dict[name]=model().fit(data_dict['X_train'],data_dict['y_train'])
    return trained_model_dict





