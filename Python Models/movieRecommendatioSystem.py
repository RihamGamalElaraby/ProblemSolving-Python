################################# 

#movie recommendation system 


import pandas as pd

Movies = {
    "SpiderMan" : [3.5 , 5.0 , 4.0] ,
    "James bond" : [2.0 , 3.5 , 4.5 ],
    "Titanic" : [5.0 , 3.5 , 1.0],
    }

ratings = pd.DataFrame(Movies)
print (ratings)

new_ratings = pd.Series([1.0 , 5.0 , 4.0])
recommendation = ratings.corrwith(new_ratings)
print(recommendation)


recommendation = pd.DataFrame(recommendation, columns=['Correnation'])
recommendation =  recommendation.sort_values(by='Correnation' , ascending = False)
print(recommendation)