#machine learning and linear regression

from Model import Prediction
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def make_prediction(inputs: list[float], outputs: list[float], input_value: float, plot: bool = False) -> Prediction:
    if len(inputs) != len(outputs):
        raise Exception('Length of "inputs" and "output"s must match!')


    #creata data frame
    df = pd.DataFrame({'inputs': inputs, 'outputs': outputs})

    #reshaping data using numpy (X: inputs, y: outputs)
    X = np.array(df['inputs']).reshape(-1,1)
    y = np.array(df['outputs']).reshape(-1, 1)

    #split the data in to training data to test out model
    train_X, test_X, train_y, test_y = train_test_split(X,y,random_state=0, test_size=0.2)

    #randomize the model and test it

    model = LinearRegression()
    model.fit(train_X, train_y)

    #Prediction
    y_prediction = model.predict([[input_value]])
    y_line = model.predict(X)

    #Testing for accuracy
    y_test_prediction = model.predict(test_X)

    #Plot
    if plot:
        display_plot(inputs=X, outputs=y, y_line=y_line)


    return Prediction(value=y_prediction[0][0],
                      r2_score=r2_score(test_y,y_test_prediction),
                      slope=model.coef_[0][0],
                      intercept=model.intercept_[0],
                      mean_absolute_error=mean_absolute_error(test_y,y_test_prediction))


def display_plot(inputs: list[float], outputs: list[float], y_line):
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel('inputs')
    plt.ylabel('outputs')
    plt.plot(inputs, y_line, color='r')
    plt.show()




def main() -> None:
    years: list[int] = [1,2,3,4,5,6,7,8,9,10]
    earning: list[int] = [1000,2000,800,959,3000,4500,5000,5490,6000,7500]
    my_input: int = 20
    prediction: Prediction = make_prediction(years,earning,my_input, plot=False)
    print(f'Input: {my_input}')
    print(prediction)
    print("Year 30", prediction.slope * 30)
    print("Year 40", prediction.slope * 40)

if __name__ == '__main__':
    main()