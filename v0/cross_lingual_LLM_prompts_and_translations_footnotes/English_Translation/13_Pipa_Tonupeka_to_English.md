# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Pipa yaieyukar, “Tonupeka ranran” 沼貝が自ら歌った謡「トヌペカ ランラン」

## This is translated from Chinese translation.

### Model
gemini-2.0-flash-001

### Setting
```
generate_content_config = types.GenerateContentConfig(
    temperature = 0,
    top_p = 0,
    max_output_tokens = 8192,
    response_modalities = ["TEXT"],
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    system_instruction=[types.Part.from_text(text=si_text1)],
  )
```

### System prompt
```
You are a professional translator. You know Japanese, English and Chinese. You can translate Japanese into either Chinese or English.
```

### Prompt
```
Translate the following text from Chinese to English. The original text is translation from Japanese which is a footnotes of Ainu chants. 
Keep the original meaning. Use modern and simple English.
If a term cannot be translated, keep the original language.

(1) kinatantuka......蒲草束。蒲草編織成類似蓆子的鋪墊物,但如果直接編織乾燥的蒲草是不行的,所以要稍微弄濕後再使用。這個故事裡提到的,大概也是為了這個原因,女人才把蒲草帶到河邊。

(2) i-okapushpa. 人們非常忌諱說出已故父母或親戚的名字,或者平常談論他們的事情,這被稱為 i-okapushpa。此外,從旁挖掘別人隱藏的事情,並告訴大家,或者說出那個人難以啟齒的、過去的行為等等,也被稱為 i-okapushpa。

(3) nimakitara......露出獠牙。指的是狗。山裡的獵人在狩獵時會帶著狗,因為被狗露出牙齒攻擊是最可怕的,所以用這樣的名字來稱呼狗,表示恐懼。

```

### Output
```
(1) kinatantuka......A bundle of cattails. Cattails are woven into a mat-like bedding. However, dry cattails cannot be woven directly, so they need to be slightly moistened before use. In this story, the woman probably brought the cattails to the river for this reason.

(2) i-okapushpa. People highly avoid saying the names of deceased parents or relatives, or even talking about them in general. This is called i-okapushpa. In addition, digging up someone's hidden secrets and telling everyone, or revealing their embarrassing past actions, is also called i-okapushpa.

(3) nimakitara......Baring fangs. This refers to dogs. Hunters in the mountains bring dogs when hunting. Being attacked by a dog baring its teeth is the most terrifying thing, so dogs are called by this name to express fear.
```
