# This script translates the text of dataframe (.csv) file using the unlimited_machine_translator package and the deep_translator package. 

import os
import pandas as pd
from unlimited_machine_translator.translator import machine_translator_df, merge_csvs, store_translation
from deep_translator import GoogleTranslator

# Input information
root = os.getcwd()                               # working directory
data_set_name = 'sample_data_project_names.csv'  # data with the column to be translated (must be in a csv file)
# Translate specs
target_language = 'en'                           # target language
column_name = 'Project_Name'                     # column to be translated
Translator = GoogleTranslator                    # Available translators: GoogleTranslator, MicrosoftTranslator, PonsTranslator, LingueeTranslator, MyMemoryTranslator, 
                                                 #                        YandexTranslator, PapagoTranslator, DeeplTranslator, QcriTranslator,
# Output information
output_name = target_language.upper() + '_' + data_set_name


# ---------------------------------- Dataset read -----------------------------------------------
data_set = pd.read_csv(os.path.join(root, data_set_name))

# -------------------- Translate datset by batches (stored in multiple .csv) ---------------------
stored_location = machine_translator_df(target_language, root, data_set, column_name, output_name, Translator)

# ----------------------------- Merge the translated .csv files -----------------------------------
df_merged_translation = merge_csvs(target_language, stored_location, data_set, column_name)
print(df_merged_translation.head())

# --------------------------- Store everything in one output file ---------------------------------
store_translation(df_merged_translation, root, output_name)
