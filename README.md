# Unlimited Machine Translator
[![Latest Release](https://img.shields.io/pypi/v/unlimited_machine_translator.svg?style=flat-square&labelColor=black&color=blue)](https://pypi.org/project/unlimited_machine_translator/)
[![License](https://img.shields.io/pypi/l/unlimited_machine_translator.svg?style=flat-square&labelColor=black&color=yellow)](https://github.com/Axel-Vs/unlimited_machine_translator/blob/main/LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/unlimited_machine_translator.svg?style=flat-square&labelColor=black&color=orange)](https://pypi.org/project/unlimited_machine_translator/)
[![Powered by deep-translator](https://img.shields.io/badge/Powered%20by-deep--translator-black?style=flat-square&labelColor=blue&color=orange)](https://pypi.org/project/deep-translator/)
[![Status](https://img.shields.io/pypi/status/unlimited_machine_translator.svg?style=flat-square&labelColor=black&color=green)](https://pypi.org/project/unlimited_machine_translator/)
[![Downloads](https://static.pepy.tech/personalized-badge/unlimited-machine-translator?period=total&units=international_system&left_color=black&right_color=%23006400&left_text=Downloads)](https://pepy.tech/project/unlimited-machine-translator)


Introducing the Unlimited Machine Translator, a Python package that enables you to translate all your data frames and doc files without restrictions, and with no API key required! This powerful tool is designed for translating large datasets using the Google Translate API and is powered by the deep-translator library. The unlimited_machine_translation package offers automatic language detection, ensuring accurate translations for your content. Additionally, it removes translation limits by processing data in batches, making it an ideal solution for handling extensive data sets.


## Installation
To install the Unlimited Machine Translator, run the following commands

1. Install from PyPI:
```bash
pip install unlimited-machine-translator
```

2. Install the development version directly from the GitHub repository:
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


### Data Frame Translation Example
```python
import os
import pandas as pd
from deep_translator import GoogleTranslator
from unlimited_machine_translator.translator import machine_translator_df

# Load your dataset
data = pd.read_csv("your_dataset.csv")

# Translate the desired column
translated_data = machine_translator_df(data_set=data, column_name="text_column", target_language="en", 
                                        source_language='auto', Translator=GoogleTranslator, 
                                        current_wd=os.getcwd())

# Save the translated data
translated_data.to_csv("translated_dataset.csv", index=False)
```

### Document Translation Example
```python
import os
from deep_translator import GoogleTranslator
from unlimited_machine_translator.translator import (
    read_word_document,
    machine_translator_doc,
    save_text_to_docx
)

# Load your text
text = read_word_document(os.getcwd(), "your_book.docx")

# Translate the information
translated_text = machine_translator_doc(text, target_language='es', source_language='auto', 
                                         Translator=GoogleTranslator, current_wd=os.getcwd())

# Store the translation
save_text_to_docx(os.getcwd(), translated_text, "translated_book.docx")
```

For additional examples and use cases, please refer to the "test_codes" directory in the repository.


## Supported Translation APIs
Currently, the Unlimited Machine Translator primarily supports Google Translate API. In the future, it will be extended to support other translation services, such as:

- DeepL Translator
- Microsoft Translator
- Yandex.Translate


## Contributions
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the https://github.com/Axel-Vs/unlimited_machine_translator.



## License
This project is licensed under the MIT License. For more information, see the LICENSE file.
