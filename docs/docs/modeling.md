## Modeling 
- What are the Common price amount always happening for the given list of variables(x-var)? 
    - This is useful to get a intiution 
    - This can be used in final stage of modeling (we can tweak the model output , to get desired output at the last)
- Feature Selection using trained models
- Build Different Algorithms to predict the price
    - Linear, Lasso,Ridge
    - Xgboost,Catboost,LightGBM
    - Pytorch model (if needed)
	- Baseline model performance metrics
- Measure the model performance using 
    - Mean Absolute Error
    - Mean Squared Error
    - RMSE
- Benchmark Leaderboard of models using Different Hyperparameters
    - For above metrics(Error function in the test set)
    - Also for Prediction Time
	
- Confidence Interval Calculation 
    - Random Forest Confidence Intervals (using different Decision Trees)
    - Gradient Boosting using Quantile Intervals
- Explanation for the prediction
    - Shap
    - Lime

## Developing Baseline Model

### we trained 7 Models with no hyperparameter tuning as our first baseline:
- Linear Regression
- Lasso Regression
- Ridge Regression
- RandomForest Regression
- GradientBoosting Regression (GBR)
- CatBoost GBR
- lightGBM GBR


### Baseline Score of the trained models

 |      |   linear_reg |      lasso |      ridge |         rf |        gbr |    cat_gbr |   light_gbr |
|:-----|-------------:|-----------:|-----------:|-----------:|-----------:|-----------:|------------:|
| maae |      23.9081 |    24.9784 |    23.9086 |    22.1    |    23.3951 |    22.6081 |     22.4571 |
| mae  |      52.7526 |    52.9087 |    52.7526 |    55.2584 |    49.892  |    49.4214 |     49.6741 |
| mse  |   21382.3    | 21457.7    | 21382.4    | 23178.5    | 20087.1    | 19066.8    |  19289.1    |
| rmse |     146.227  |   146.484  |   146.227  |   152.245  |   141.729  |   138.083  |    138.885  |
	
-	Among all the models catboost Regressor performed well on the test dataset

![baseline_benchmark](..\IMG\baseline_benchmark.JPG)


### As we took Catboost model for best prediction accuracy and low-latency predictions and started tuning the hyperparamater of the models

`The Training notebook of the catboost model was attached as html in the following link`

--









