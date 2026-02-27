from sklearn.linear_model import LinearRegression
import numpy as np

def predict_demand(data):
    model = LinearRegression()
    
    X = np.arange(len(data)).reshape(-1,1)
    y = data["demand"]
    
    model.fit(X,y)
    future = np.array([[len(data)+1]])
    
    return int(model.predict(future)[0])