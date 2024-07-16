import numpy as np

class Regression:
    intercept = 0
    coef = 1

    def __init__(self, xParam, yParam) -> None:
        self.x_datas = xParam
        self.y_datas = yParam

        self.gradient_descent()
        self.r_squared()
    
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
        avg = np.average(actualDatas)
        for i in range(len(actualDatas)):
            ssa += (avg - actualDatas[i])**2
        
        return ssa
    
    def gradient_descent(self):
        IS_INTERCEPT_TRAINING_DONE = False
        IS_COEF_TRAINING_DONE = False

        isContinue = True
        while isContinue:
            y_predict = []
            for x in self.x_datas:
                y_predict.append(self.normalLinearFunction(x, intercept = self.intercept, coef = self.coef))

            sum_of_slope = 0
            if(not IS_INTERCEPT_TRAINING_DONE):
                all_interceptSlopes = []
                for i in range(len(self.y_datas)):
                    all_interceptSlopes.append(-2*(self.y_datas[i] - y_predict[i]))
                
                sum_of_slope = np.sum(all_interceptSlopes)
                
                intercept_step_size = sum_of_slope * 0.01
                self.intercept -= intercept_step_size
            
                if abs(intercept_step_size) < 0.01:
                    IS_INTERCEPT_TRAINING_DONE = True

            sum_of_coefSlope = 0
            if(not IS_COEF_TRAINING_DONE):
                slopes = []
                for x in range(len(self.x_datas)):
                    slopes.append(-2 * self.x_datas[x] * (self.y_datas[x] - y_predict[x]))
                
                sum_of_coefSlope = np.sum(slopes)
                
                coef_step_size = sum_of_coefSlope * 0.0001
                self.coef -= coef_step_size
            
                if abs(coef_step_size) < 0.01:
                    IS_COEF_TRAINING_DONE = True
            
            isContinue = not (IS_INTERCEPT_TRAINING_DONE and IS_COEF_TRAINING_DONE)
    
    def r_squared(self):
        predict = []

        for x in self.x_datas:
            predict.append(self.normalLinearFunction(x, self.intercept, self.coef))
        
        self.R_SQUARED = 1 - (self.SSR(self.y_datas, predict) / self.SSA(self.y_datas))