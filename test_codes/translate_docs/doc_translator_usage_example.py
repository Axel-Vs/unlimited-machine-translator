# This script translates the text in a Word document (.docx) file using the unlimited_machine_translator package and the deep_translator package. 

import os
from unlimited_machine_translator.translator import read_word_document, save_text_to_docx, machine_translator_doc
from deep_translator import GoogleTranslator
        
                             
# ------------------------------------- Input information --------------------------------------
# Data info
data_path = os.path.join(os.getcwd(), 'test_codes', 'translate_docs')
data_name = 'Importancia_pipelines.docx'         # Document to be translated (must be in a doc file)
# Translate specs
target_language = 'en'                           
source_language = 'auto'                         
Translator = GoogleTranslator                    
# Output information
output_name = target_language.upper() + '_' + data_name  # Storing name


# ---------------------------------- Dataset read -----------------------------------------------
text = read_word_document(data_path, data_name)


# ----------------------------- Translate the text ----------------------------------------------  
translated_text = machine_translator_doc(text, target_language, source_language, Translator, data_path)
print(translated_text[:100], '...\n')


# --------------------------- Store everything in one output file -------------------------------
save_text_to_docx(data_path, translated_text, output_name)