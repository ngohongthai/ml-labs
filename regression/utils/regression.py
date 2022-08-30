import pandas as pd

def rss(y_true, y_pred):
    """
    Calculate the Residual Sum of Squares (RSS)
    """
    return ((y_true - y_pred) ** 2).sum()

def rss_of_model(model, x, y_true):
    """
    Calculate the RSS of the model
    """
    y_pred = model.predict(x)
    return rss(y_true, y_pred)

def polynomial_dataframe(feature, degree):
    """
    Generate a dataframe of polynomial terms given a feature and degree
    """
    poly_data = pd.DataFrame()
    # đặt poly_data['power_1'] bằng với đặc trưng đã truyền vào
    poly_data['power_1'] = feature
    if degree > 1:
        for power in range(2, degree+1): 
            # Tạo ra một biến tên là 'power_x' với x là bậc của các biến
            name = 'power_' + str(power)
            poly_data[name] = feature ** power
    return poly_data
