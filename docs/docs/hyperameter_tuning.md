## Hyperameter Tunning


- We settled with the Catboost model for good Quality prediction and low latency prediction


This is the table of hyperparameters and their performance metric

|    |   ('number', '') | ('state', '')       |   ('value', '') | ('datetime_start', '')     | ('datetime_complete', '')   |   ('params', 'bagging_temperature') | ('params', 'boosting_type')   | ('params', 'bootstrap_type')   |   ('params', 'depth') |   ('params', 'learning_rate') | ('params', 'objective')   |   ('params', 'subsample') |   ('system_attrs', '_number') | ('system_attrs', 'fail_reason')                                                                                                                            |
|---:|-----------------:|:--------------------|----------------:|:---------------------------|:----------------------------|------------------------------------:|:------------------------------|:-------------------------------|----------------------:|------------------------------:|:--------------------------|--------------------------:|------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 |                0 | TrialState.FAIL     |        nan      | 2020-01-02 20:21:11.863237 | 2020-01-02 20:21:12.418973  |                           nan       | nan                           | nan                            |                     6 |                   nan         | RMSE                      |                nan        |                             0 | Setting status of trial#0 as TrialState.FAIL because of the following error: TypeError('suggest_uniform() takes 4 positional arguments but 8 were given',) |
|  1 |                1 | TrialState.FAIL     |        nan      | 2020-01-02 20:21:38.181381 | 2020-01-02 20:21:38.818264  |                           nan       | nan                           | nan                            |                     7 |                   nan         | MAE                       |                nan        |                             1 | Setting status of trial#1 as TrialState.FAIL because of the following error: TypeError('suggest_uniform() takes 4 positional arguments but 6 were given',) |
|  2 |                2 | TrialState.FAIL     |        nan      | 2020-01-02 20:22:14.453568 | 2020-01-02 20:22:15.072724  |                           nan       | nan                           | nan                            |                     2 |                   nan         | RMSE                      |                nan        |                             2 | Setting status of trial#2 as TrialState.FAIL because of the following error: TypeError('suggest_uniform() takes 4 positional arguments but 5 were given',) |
|  3 |                3 | TrialState.COMPLETE |         42.7238 | 2020-01-02 20:22:23.798479 | 2020-01-02 20:22:39.130715  |                           nan       | Plain                         | MVS                            |                    11 |                     0.489043  | MAE                       |                nan        |                             3 | nan                                                                                                                                                        |
|  4 |                4 | TrialState.COMPLETE |         50.5916 | 2020-01-02 20:22:39.215907 | 2020-01-02 20:22:42.882038  |                           nan       | Plain                         | Bernoulli                      |                     5 |                     0.529281  | RMSE                      |                  0.607423 |                             4 | nan                                                                                                                                                        |
|  5 |                5 | TrialState.COMPLETE |         42.5857 | 2020-01-02 20:22:42.963390 | 2020-01-02 20:23:43.219132  |                           nan       | Plain                         | Bernoulli                      |                     3 |                     0.683597  | MAE                       |                  0.374904 |                             5 | nan                                                                                                                                                        |
|  6 |                6 | TrialState.COMPLETE |         46.9529 | 2020-01-02 20:23:43.311247 | 2020-01-02 20:24:41.338719  |                           nan       | Plain                         | MVS                            |                     1 |                     0.0137888 | MAE                       |                nan        |                             6 | nan                                                                                                                                                        |
|  7 |                7 | TrialState.COMPLETE |         44.549  | 2020-01-02 20:24:41.431578 | 2020-01-02 20:25:29.054821  |                             1.91368 | Ordered                       | Bayesian                       |                     1 |                     0.384213  | MAE                       |                nan        |                             7 | nan                                                                                                                                                        |
|  8 |                8 | TrialState.COMPLETE |         41.917  | 2020-01-02 20:25:29.147049 | 2020-01-02 20:26:22.714733  |                           nan       | Ordered                       | MVS                            |                     5 |                     0.226351  | MAE                       |                nan        |                             8 | nan                                                                                                                                                        |
|  9 |                9 | TrialState.COMPLETE |         50.1082 | 2020-01-02 20:26:22.825344 | 2020-01-02 20:26:34.244275  |                           nan       | Plain                         | MVS                            |                    12 |                     0.547259  | RMSE                      |                nan        |                             9 | nan                                                                                                                                                        |
| 10 |               10 | TrialState.COMPLETE |         52.9363 | 2020-01-02 20:26:34.396108 | 2020-01-02 20:26:37.911406  |                           nan       | Plain                         | Bernoulli                      |                     5 |                     0.603843  | RMSE                      |                  0.303779 |                            10 | nan                                                                                                                                                        |
| 11 |               11 | TrialState.COMPLETE |         51.0596 | 2020-01-02 20:26:38.002327 | 2020-01-02 20:26:46.647710  |                             8.14127 | Ordered                       | Bayesian                       |                     4 |                     0.754896  | RMSE                      |                nan        |                            11 | nan                                                                                                                                                        |
| 12 |               12 | TrialState.COMPLETE |         50.528  | 2020-01-02 20:26:46.733670 | 2020-01-02 20:26:51.632994  |                           nan       | Ordered                       | Bernoulli                      |                     4 |                     0.51049   | RMSE                      |                  0.546119 |                            12 | nan                                                                                                                                                        |
| 13 |               13 | TrialState.COMPLETE |         42.2105 | 2020-01-02 20:26:51.725349 | 2020-01-02 20:27:16.891392  |                           nan       | Ordered                       | MVS                            |                     9 |                     0.212695  | MAE                       |                nan        |                            13 | nan                                                                                                                                                        |
| 14 |               14 | TrialState.COMPLETE |         43.212  | 2020-01-02 20:27:16.980661 | 2020-01-02 20:27:50.826629  |                           nan       | Ordered                       | MVS                            |                     9 |                     0.209423  | MAE                       |                nan        |                            14 | nan                                                                                                                                                        |
| 15 |               15 | TrialState.COMPLETE |         42.605  | 2020-01-02 20:27:50.911060 | 2020-01-02 20:28:22.338762  |                           nan       | Ordered                       | MVS                            |                     8 |                     0.171057  | MAE                       |                nan        |                            15 | nan                                                                                                                                                        |
| 16 |               16 | TrialState.COMPLETE |         42.9026 | 2020-01-02 20:28:22.445095 | 2020-01-02 20:28:46.446403  |                           nan       | Ordered                       | MVS                            |                     8 |                     0.29398   | MAE                       |                nan        |                            16 | nan                                                                                                                                                        |
| 17 |               17 | TrialState.COMPLETE |         42.9598 | 2020-01-02 20:28:46.558330 | 2020-01-02 20:30:10.208094  |                           nan       | Ordered                       | MVS                            |                    10 |                     0.0427293 | MAE                       |                nan        |                            17 | nan                                                                                                                                                        |




### Apart from the above Optimization, we did some tunning in the modeling phase (using catboost model)