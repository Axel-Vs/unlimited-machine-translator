# This script translates the text in a Word document (.docx) file using the unlimited_machine_translator package and the deep_translator package. 

import os
from unlimited_machine_translator.translator import read_word_document, save_text_to_docx, machine_translator_doc
from deep_translator import GoogleTranslator
                             
# Input information
root = os.getcwd()                               # working directory
data_name = 'Importancia_pipelines.docx'      # data with the column to be translated (must be in a csv file)
# Translate specs
target_language = 'en'                           # target language
Translator = GoogleTranslator                    # Available translators: GoogleTranslator, MicrosoftTranslator, PonsTranslator, LingueeTranslator, MyMemoryTranslator, 
                                                 #                        YandexTranslator, PapagoTranslator, DeeplTranslator, QcriTranslator,
# Output information
output_name = target_language.upper() + '_' + data_name


# ---------------------------------- Dataset read -----------------------------------------------
text = read_word_document(root, data_name)

# ----------------------------- Translate the text ----------------------------------------------  
translated_text = machine_translator_doc(target_language, root, text, data_name, Translator)
print(translated_text[:100], '...\n')

# --------------------------- Store everything in one output file -------------------------------
save_text_to_docx(root, translated_text, output_name)