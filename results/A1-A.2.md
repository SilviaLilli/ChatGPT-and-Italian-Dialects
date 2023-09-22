# TEST A.1 RESULTS
## BLEU, TER and COMET score at default temperature (DT), low temperature (LT) and high temperature (HT) setting.


|              |       |  BLEU |       | TER   |       |       | COMET |       |       |
|--------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|              | DT    | LT    | HT    | DT    | LT    | HT    | DT    | LT    | HT    |
| Milanese     | 0.54  | 0.51  | 0.37  | 0.66  | 0.63  | 0.50  | 0.87  | 0.86  | 0.84  |
| Roman        | 0.71  | 0.66  | 0.39  | 0.78  | 0.77  | 0.55  | 0.92  | 0.92  | 0.85  |
| Sicilian     | 0.63  | 0.70  | 0.48  | 0.75  | 0.77  | 0.61  | 0.85  | 0.84  | 0.80  |


# TEST A.2 RESULTS

### Score range
0 = Misunderstanding of the text, resulting in an incorrect answer.  
1 = Partial comprehension of the text, resulting in a partially correct answer.  
2 = Good comprehension of the text, resulting in a correct answer.  
3 = Optimal comprehension of the text, resulting in a complete and correct answer.  


## Milanese

|               |  Before translation |  After translation  |
|---------------|---------------------|---------------------|
| Question 1    |          2          |          2          |
| Question 2    |          1          |          3          |
| Question 3    |          3          |          2          |
| Question 4    |          1          |          1          |
| Question 5    |          2          |          3          |
| **Total**         |          **9**          |          **11**          |


## Roman Dialect

|               |  Before translation |  After translation  |
|---------------|---------------------|---------------------|
| Question 1    |          2          |          3          |
| Question 2    |          1          |          2          |
| Question 3    |          2          |          3          |
| Question 4    |          2          |          2          |
| Question 5    |          2          |          3          |
| **Total**         |          **7**          |          **13**          |


## Sicilian

|               |  Before translation |  After translation  |
|---------------|---------------------|---------------------|
| Question 1    |          3          |          2          |
| Question 2    |          1          |          3          |
| Question 3    |          3          |          2          |
| Question 4    |          2          |          2          |
| Question 5    |          3          |          2          |
| **Total**         |          **12**          |          **11**          |


## Comparison


|               |  Before translation |  After translation  |
|---------------|---------------------|---------------------|
| Milanese      |           9         |          11         |
| Roman Dialect |           7         |          13         |
| Sicilian      |          12         |          11         |
