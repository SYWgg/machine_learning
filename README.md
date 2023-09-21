# machine_learning
Navie Bayes, knn... 구현하기!



## 📂 iris_species
소개 : [iris_species 데이터](https://www.kaggle.com/datasets/uciml/iris?resource=download)를 KNN 알고리즘으로 K의 개수에 따른 분류 정확도를 구현

  step1. Euclidean distance로 각 data 하나씩과 나머지 data들 사이의 거리를 구한다.
  step2. 거리가 가장 가까운 K개의 클래스들을 구해 그 중 가장 많이 count된 클래스로 예측 분류한다.
  step3. 예측 분류한 값과 실제 값(species)를 비교해 K 개수에 따른 정확도를 측정한다.
  
