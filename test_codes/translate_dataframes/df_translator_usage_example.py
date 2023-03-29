# This script translates the text of dataframe (.csv) file using the unlimited_machine_translator package and the deep_translator package. 

import os
import pandas as pd
from unlimited_machine_translator.translator import machine_translator_df, store_translation
from deep_translator import GoogleTranslator


# ------------------------------------ Input information -----------------------------------------
data_path = os.path.join(os.getcwd(), 'test_codes', 'translate_dataframes')
data_set_name = 'sample_data_project_names.csv'  # Data with the column to be translated (must be in a csv file)
# Translate specs
target_language = 'es'                           
source_language = 'auto'
column_name = 'Project_Name'                     # Column to be translated
Translator = GoogleTranslator                    
# Output information
output_name = target_language.upper() + '_' + data_set_name   # Storing name


# ----------------------------------- Dataset read ------------------------------------------------
data_set = pd.read_csv(os.path.join(data_path, data_set_name))


# ----------------------------------- Translation -------------------------------------------------
df_translated = machine_translator_df(data_set, column_name, target_language, source_language, Translator, data_path)
print(df_translated.head())


# --------------------------- Store everything in one output file ---------------------------------
store_translation(df_translated, data_path, output_name)
