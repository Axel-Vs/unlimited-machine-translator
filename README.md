# Unlimited Machine Translator

[![Latest Release](https://img.shields.io/pypi/v/unlimited_machine_translator.svg?style=flat-square&labelColor=black&color=blue)](https://pypi.org/project/unlimited_machine_translator/)
[![License](https://img.shields.io/pypi/l/unlimited_machine_translator.svg?style=flat-square&labelColor=black&color=blue)](https://github.com/Axel-Vs/unlimited_machine_translator/blob/main/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/unlimited_machine_translator.svg?style=flat-square&labelColor=black&color=blue)](https://pypi.org/project/unlimited_machine_translator/)
[![Powered by deep-translator](https://img.shields.io/badge/Powered%20by-deep--translator-black?style=flat-square&labelColor=black&color=blue)](https://pypi.org/project/deep-translator/)


Translate all your data frame and doc files without restrictions! The Unlimited Machine Translator is a Python package that makes it easy to translate large datasets using Google Translate API. Powered by [`deep-translator`](https://pypi.org/project/deep-translator/). The unlimited_machine_translation package offers automatic language detection and removes translation limits by processing data in batches.


## Installation

To install the Unlimited Machine Translator, run the following command:

```bash
pip install git+https://github.com/Axel-Vs/unlimited_machine_translator.git
```

## Features

- Translate entire data frames with ease
- Supports multiple translation APIs
- Handles API limitations and restrictions by translating data in batches
- Automatic language detection
- Easily extendable to support new translation services


## Usage

After installing the package, you can use it in your Python scripts or Jupyter notebooks like this:

```python
import pandas as pd
from unlimited_machine_translator.translator import machine_translator_df

# Load your dataset
data = pd.read_csv("your_dataset.csv")

# Translate the desired column
translated_data = machine_translator_df(data, source_language="en", target_language="es", column_name="text_column")

# Save the translated data
translated_data.to_csv("translated_dataset.csv", index=False)
```

For more examples check the folder "test_codes"

## Supported Translation APIs
Currently, the Unlimited Machine Translator primarily supports Google Translate API. In the future, it will be extended to support other translation services, such as:

- DeepL Translator
- Microsoft Translator
- Yandex.Translate

To use a different translation service, you can easily extend the package by implementing a new translator class that inherits from the base Translator class.


## Contributions
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the https://github.com/Axel-Vs/unlimited_machine_translator.



## License
This project is licensed under the MIT License. For more information, see the LICENSE file.