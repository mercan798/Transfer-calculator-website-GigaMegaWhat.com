import gradio as gr
from config import ADSENSE_CLIENT, ADSENSE_SLOT

def tb_transfer(data_tb, link_mbit):
    try:
        if data_tb is None or link_mbit is None: 
            return " Alanlar boş olmamalı !"
        if data_tb < 0:
            return " Veri miktarı pozitif olmalı!"
        if link_mbit <= 0:
            return " Link kapasitesi 0 dan küçük olamaz!!"
        
        bit_cal = data_tb * (8 * 1024**4)
        band_width = link_mbit * 1_000_000
        sec = bit_cal / band_width
        real_sec = int(sec)
        day = real_sec // 86400
        rem = real_sec % 86400
        hour = rem // 3600
        rem = rem % 3600
        min = rem // 60
        seconds = rem % 60
        
        return f" {day} GÜN , {hour} SAAT , {min} DAKİKA , {seconds} SANİYE"
    except Exception as a:
        return f"HATA:{a}"

with gr.Blocks() as demo:
    gr.HTML(
        f"""<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}"
             crossorigin="anonymous"></script>
        <!-- veri_trans_banner -->
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="{ADSENSE_CLIENT}"
             data-ad-slot="{ADSENSE_SLOT}"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push();
        </script>
        """
    )
    
    with gr.Row():
        with gr.Column(scale=3):
            data_tb = gr.Number(label=" Hesaplanıcak Data (TB)", elem_id="data-input")
            link_mbit = gr.Number(label="Link Hızı(Mbit)", elem_id="link-input")
            qbutton = gr.Button("Hesap ", elem_id="calc-button")
        with gr.Column(scale=0):
            output = gr.Textbox(label="Forman biçimi test sonucu", elem_id="result-output")
    
    qbutton.click(tb_transfer, inputs=[data_tb, link_mbit], outputs=output)

demo.launch(
    share=True,
    css="footer {visibility: hidden !important;}"
)