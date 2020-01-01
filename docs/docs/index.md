## POSHMARK -Assignment

### Regression Problem

#### Identify/predict/recommend the price for given set of items
*input* :

	x1-15

*output (target)* :

	y_var
	
## Data science Steps:
	- Data Clean 
	- Visualize the data
		- Ask Questions
	- Feature Selection based on visualization and try brute force also
	- Modeling:
		- Linear Regression
		- polynomial Regression
		- Gradient Boosting
		- Xgboost
		- Catboost
		- LightGBM
		- H20
		- Try Formula (if target was not fitted properly)


## Deployment :
	You can assume 5000 listings are being created in our platform every minute through our iphone 
	or android app or website.

	- Scalable solution 
		- should be Horizontally scalable
	- Use load Balancer
		- async
		- docker
		- RPC call
	- Use message Queue
		- KAFKA
		- Redis
		- celery
		
	
	- Store the output of the model and data in some Big data systems (HDFS, S3, HIVE)
	
	- should not have single point of failure
	- Analytics as to be done
	- Feedback based training
	- Batch analytics
	
## Explanation:
  ### Give explanation for your prediction if needed
  - lime
  - SHAP

## Give confidence interval also for the price
## Feedback:
	- Take Feedback about the price recommendation
	- Use this Feedback to improve/train the models

## Attach Rest API 
	-Docker Deployment scripts


	
	 