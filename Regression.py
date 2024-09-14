# import numpy as np
# ! Modelnya masih lambat, buat aku di masa depan kalau bisa tolong perbaiki agar lebih cepat (sama apa kabar, semangat terus yah)

class Regression:
    intercept = 0
    coef = 1

    def __init__(self, xParam, yParam) -> None:
        isValid = data_check(xParam, yParam)
        
        if not isValid:
            raise Exception("Data length must be the same!")
        
        self.x_datas = xParam
        self.y_datas = yParam

        self.gradient_descent()
        self.__calculateR()
    
    def normalLinearFunction(self, x, intercept = 0, coef = 1):
        return coef * x + intercept
    
    def predict(self, x):
        result = self.normalLinearFunction(x, self.intercept, self.coef)
        return result
    
    def SSR(self, actualDatas, predictedDatas):
        ssr = 0
        for i in range(len(actualDatas)):
            ssr += (predictedDatas[i] - actualDatas[i])**2
        
        return ssr
    
    def SSA(self, actualDatas):
        ssa = 0
        avg = average(actualDatas)
        for i in range(len(actualDatas)):
            ssa += (avg - actualDatas[i])**2
        
        return ssa
    
    def gradient_descent(self):
        IS_INTERCEPT_TRAINING_DONE = False
        IS_COEF_TRAINING_DONE = False

        DATA_LENGTH = len(self.x_datas)
        isContinue = True
        while isContinue:
            
            intercept_gradient = 0
            if(not IS_INTERCEPT_TRAINING_DONE):
                all_interceptSlopes = []
                for i in range(DATA_LENGTH):
                    x = self.x_datas[i]
                    actual = self.y_datas[i]
                    predict = self.normalLinearFunction(x, intercept = self.intercept, coef = self.coef)
                    all_interceptSlopes.append(-2 * (actual - predict) )
                
                intercept_gradient = (1 / (2 * DATA_LENGTH)) * (sum(all_interceptSlopes))
                
                intercept_step_size = intercept_gradient * 0.1
                self.intercept -= intercept_step_size
            
                if abs(intercept_step_size) < 0.01:
                    IS_INTERCEPT_TRAINING_DONE = True

            coef_gradient = 0
            if(not IS_COEF_TRAINING_DONE):
                slopes = []
                for i in range(DATA_LENGTH):
                    x = self.x_datas[i]
                    actual = self.y_datas[i]
                    predict = self.normalLinearFunction(x, intercept = self.intercept, coef = self.coef)
                    slopes.append(-2 * x * (actual - predict))
                
                coef_gradient = (1 / (2 * DATA_LENGTH)) * (sum(slopes))
                
                coef_step_size = coef_gradient * 0.01
                self.coef -= coef_step_size
            
                if abs(coef_step_size) < 0.01:
                    IS_COEF_TRAINING_DONE = True
            
            isContinue = not (IS_INTERCEPT_TRAINING_DONE and IS_COEF_TRAINING_DONE)
    
    def __calculateR(self):
        predict = []

        for x in self.x_datas:
            predict.append(self.normalLinearFunction(x, self.intercept, self.coef))
        
        self.R_SQUARED = 1 - (self.SSR(self.y_datas, predict) / self.SSA(self.y_datas))

def data_check(xDatas, yDatas) -> bool:
    lenX = len(xDatas)
    lenY = len(yDatas)
    
    return lenX == lenY

def sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    
    return sum

def average(array):
    result = sum(array) / len(array)
    
    return result
