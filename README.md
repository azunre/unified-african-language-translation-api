# Unified African Language Translation API
This repo provides a wrapper to combine the GhanaNLP and Lesan African language translation APIs to expand the language coverage

Currently, the combined languages thus covered are "Amharic", "Tigrinya", "Twi", "Ga", "Ewe", "Yoruba", "Dagbani", "Kikuyu", "Gurune", "Luo" and "Kimeru". This corresponds to the language codes "am", "ti", "tw", "gaa","ee", "yo", "dag", "ki", "gur", "luo" and "mer" (respectively)

To install and use the wrapper through the included gradio interface:

1. `pip install gradio`
2. Modify `config_template.cfg` with lesan and ghananlp API keys (obtain these from https://lesan.ai/ and https://translation.ghananlp.org respectively)
3. Rename `config_template.cfg` as `config.cfg`
4. Run the UI as `gradio gradio_UI.py`. It will be available on 127.0.0.1:8080 locally, or via the unique public link printed on the terminal on the web.
