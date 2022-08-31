import seaborn as sns
from matplotlib import pyplot as plt


def compare_distributions(X, y, X_resample, y_resample, x_col, y_col, title):
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    ax0 = sns.scatterplot(ax=axes[0], x=x_col, y=y_col, hue=y, data=X)
    ax0.set_title('Original')
    ax1 = sns.scatterplot(ax=axes[1], x=x_col, y=y_col, hue=y_resample, data=X_resample)
    ax1.set_title('Resampled')
    fig.suptitle(title)
    