# translates Chinese to English with the NLLB model

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, NllbTokenizer

zh_txt = open('canopy_valid.zh', encoding='utf-8').read().split('\n')
src_text = []
for line in zh_txt[200:324]:
	src_text.append(line)


tokenizer = NllbTokenizer.from_pretrained(
    "facebook/nllb-200-distilled-600M", src_lang="zho_Hans", tgt_lang="eng_Latn"
)
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")

inputs = tokenizer(src_text, return_tensors="pt", padding=True)
translated = model.generate(
    **inputs, forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"], max_length=30
)
for t in translated:
	print(tokenizer.decode(t, skip_special_tokens=True))