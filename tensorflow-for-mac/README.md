### Install

```bash
conda env create -f tensorflow-apple-metal-conda.yml -n tensorflow
conda activate tensorflow
```

### Activating New Environment
```bash
conda activate tensorflow
```

### Register your Environment
```bash
python -m ipykernel install --user --name tensorflow --display-name "Python 3.9 (tensorflow)"
```

### Testing your Environment
Open `check_env.ipynb` and run the first cell

```python
# What version of Python do you have?
import sys

import tensorflow.keras
import pandas as pd
import sklearn as sk
import tensorflow as tf
import platform

print(f"Python Platform: {platform.platform()}")
print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"Scikit-Learn {sk.__version__}")
gpu = len(tf.config.list_physical_devices('GPU'))>0
print("GPU is", "available" if gpu else "NOT AVAILABLE")
```