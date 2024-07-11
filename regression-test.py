import numpy as np
import matplotlib.pyplot as plt

intercept = 0
coef = 1

x_datas = np.array([13.3, 35.5, 1.1, 22.2, 8.5, 13.3, 38.5, 15.2, 24, 13, 13.2, 6.5, 27.5, 12.9, 8, 4.9, 3.1, 10.3, 1.1, 13.7])
y_datas = np.array([6.4, 24.9, 26.6, 38, 21.6, 36.9, 27.6, 44.1, 49, 43.1, 32.7, 60.4, 58.1, 43.7, 40.2, 49.1, 13.6, 0, 56.2, 16.4])

def linearFunction(x, intercept = 0, coef = 1):
    return coef * x + intercept

plt.scatter(x_datas, y_datas)

IS_INTERCEPT_TRAINING_DONE = False
IS_COEF_TRAINING_DONE = False

isContinue = True
while isContinue:
    y_predict = []
    for x in x_datas:
        y_predict.append(linearFunction(x, intercept, coef))

    # all_costs = []
    # for i in range(len(y_datas)):
    #     all_costs.append((y_datas[i] - y_predict[i])**2)

    # loss = np.sum(all_costs)

    sum_of_slope = 0
    if(not IS_INTERCEPT_TRAINING_DONE):
        all_interceptSlopes = []
        for i in range(len(y_datas)):
            all_interceptSlopes.append(-2*(y_datas[i] - y_predict[i]))
        
        sum_of_slope = np.sum(all_interceptSlopes)
        
        intercept_step_size = sum_of_slope * 0.01
        intercept -= intercept_step_size
    
        if abs(intercept_step_size) < 0.01:
            IS_INTERCEPT_TRAINING_DONE = True

    sum_of_coefSlope = 0
    if(not IS_COEF_TRAINING_DONE):
        slopes = []
        for x in range(len(x_datas)):
            slopes.append(-2 * x_datas[x] * (y_datas[x] - y_predict[x]))
        
        sum_of_coefSlope = np.sum(slopes)
        
        coef_step_size = sum_of_coefSlope * 0.0001
        coef -= coef_step_size
    
        if abs(coef_step_size) < 0.01:
            IS_COEF_TRAINING_DONE = True
    
    isContinue = not (IS_INTERCEPT_TRAINING_DONE and IS_COEF_TRAINING_DONE)

print(f'Intercept: {intercept}')
print(f'Coef: {coef}')
plt.plot(x_datas, linearFunction(x_datas, intercept, coef), 'r')
plt.xlabel("House Age (year)")
plt.ylabel("House Price/unit area")
plt.show()