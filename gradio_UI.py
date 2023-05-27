import gradio as gr
import configparser
import urllib.request, json

# specify languages
lesan_LANGS = ["Amharic", "Tigrinya"]
lesan_LANGS_codes = ["am", "ti"]
ghananlp_LANGS = ["Twi","Ga","Ewe","Yoruba","Dagbani","Kikuyu","Gurune","Luo","Kimeru"]
ghananlp_LANGS_codes = ["tw","gaa","ee","yo","dag","ki","gur","luo","mer"]

LANGS = ["English"]+lesan_LANGS+ghananlp_LANGS
LANGS_codes = ["en"]+lesan_LANGS_codes+ghananlp_LANGS_codes
LANGS_dict = {}

for el,code in zip(LANGS,LANGS_codes):
    LANGS_dict[el]=code

# get user configs
config = configparser.RawConfigParser()
config.read('config.cfg')
URLS_dict = dict(config.items('API_URLS'))
KEYS_dict = dict(config.items('API_KEYS'))

def translate(text, src_lang, tgt_lang):
    """
    Translate the text from source lang to target lang
    """
    if src_lang in lesan_LANGS or tgt_lang in lesan_LANGS:
        try:
            hdr ={
            # Request headers
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
            }
        
            # Request body - # 'tgt_lang': am, ti, or auto
            data = {'key': KEYS_dict["lesan"], 'text': text,
                    'src_lang': LANGS_dict[src_lang], 'tgt_lang': LANGS_dict[tgt_lang]}
            
            data = json.dumps(data)
            req = urllib.request.Request(URLS_dict["lesan"], headers=hdr, data = bytes(data.encode("utf-8")))
        
            req.get_method = lambda: 'POST'
            response = urllib.request.urlopen(req)
            #print(response.getcode())
            response_text = response.read()
            result = json.loads(response_text.decode())["tgt_text"]
        except Exception as e:
            print("EXCEPTION::LESAN::")
            print(e)
    if src_lang in ghananlp_LANGS or tgt_lang in ghananlp_LANGS:
        try:
            hdr ={
            # Request headers
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': KEYS_dict["ghananlp"],
            }
        
            # Request body
            data =  {
            "in": text,
            "lang": LANGS_dict[src_lang] + "-" + LANGS_dict[tgt_lang]
            }
            data = json.dumps(data)
            req = urllib.request.Request(URLS_dict["ghananlp"], headers=hdr, data = bytes(data.encode("utf-8")))
        
            req.get_method = lambda: 'POST'
            response = urllib.request.urlopen(req)
            #print(response.getcode())
            response_text = response.read()
            result = response_text.decode('utf-8').strip('"')
        except Exception as e:
            print("EXCEPTION::GHANANLP::")
            print(e)       
    print(result)
    return 

demo = gr.Interface(
    fn=translate,
    inputs=[
        gr.components.Textbox(label="Text"),
        gr.components.Dropdown(label="Source Language", choices=LANGS),
        gr.components.Dropdown(label="Target Language", choices=LANGS),
    ],
    outputs=["text"],
    examples=[["United, we will preserve our culture!", "English", "Twi"],
              ["United, we will preserve our culture!", "English", "Amharic"]],
    cache_examples=False,
    title="Translation Demo",
    description="GhanaNLP, Algorine, Lesan, DAIR, All Rights Reserved 2023"
)

demo.launch(share=True,server_port=8080)