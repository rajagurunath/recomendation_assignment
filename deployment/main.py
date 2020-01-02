"""
FastAPI app to serve prediction -async

Ref:
    - https://grega.xyz/2019/07/fastapi-and-celery/
    - https://fastapi.tiangolo.com/project-generation
"""

from fastapi import FastAPI, BackgroundTasks
# from worker.celery_app import celery_app
import joblib
import pandas as pd 
from catboost import Pool
from typing import Dict
app = FastAPI()

catboost_model=joblib.load("../catboost_model.pkl")
cat_columns=['x1var_cat', 'x2var_cat', 'x9var_cat', 'x12var_cat']
# def celery_on_message(body):
#     print(body)

# def background_on_message(task):
#     """
#     This Background task has to be prediction Service
#     """
#     print(task.get(on_message=celery_on_message, propagate=False))


@app.post("/prediction")
async def prediction(feats:Dict):
    """
    {
	"x1var_cat": 1.0,
	"x2var_cat": 2.0,
	"x3var_cont": 15.9,
	"x4var_cont": 1.3043,
	"x5var_cont": 1.13,
	"x6var_cont": 15.0787,
	"x7var_cont": 0.0,
	"x8var_cont": 0.0,
	"x9var_cat": 0.0,
	"x10var_cont": 0.5479,
	"x11var_cont": 0.0,
	"x12var_cat": 0.0,
	"x13var_cont": 0.0,
	"x14var_cont": 1.53,
	"x15var_cont": 0.0
    }
    """
    # task = celery_app.send_task(
    #     "worker.celery_worker.test_celery", args=[word])
    # print(task)
    # background_task.add_task(background_on_message, task)
    print(feats)
    df=pd.DataFrame(feats,index=range(len(feats)))
    test_pool = Pool(data=df.iloc[:1,:], cat_features=cat_columns)
    contest_predictions = catboost_model.predict(test_pool)
    

    return {"prediction":contest_predictions.tolist()[0]}

@app.post("/feedback")
def feedback_about_price_recommendation():
    """
    feedback_about_price_recommendation

    """
    return {"msg":"feedback received"}

@app.post("/explanation")
def explanation_why_model_predicts_particular_price():
    """
    Gives explanation why model predicts particular price
    """
    return {"msg":"explanation received"}


@app.post("/confidence_about_price")
def confidence_about_price_recommendation():
    """

    """
    return {"msg":"confidence_about_price received"}