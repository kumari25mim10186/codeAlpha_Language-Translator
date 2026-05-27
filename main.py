import streamlit as st
from translate import Translator

#Language mapping
Language_mapping = dict(english="en", french="fr", spanish="es", Italian="it", German="de", Chinese="zh", Japanase="jp",
                        Portuguese="pt", Hindi="hi", Bengali="bn")

#streamlit app title
st.title("Language Translator")

#user input for text and language selection
text_to_translate = st.text_area("Enter text to translate:")
target_language = st.selectbox(
  "Enter target language:",  list(Language_mapping.keys()))

# Translate Button
if st.button("translate"):
    if text_to_translate :
        target_language = Language_mapping[target_language]
        try:
            #Initialize the translator with the target language
            translator = Translator(to_lang=target_language)
            # perform the translation
            translated_text = translator.translate(text_to_translate)
            # Display the translated text
            st.write("**translated text:**", translated_text)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter text to translate")



