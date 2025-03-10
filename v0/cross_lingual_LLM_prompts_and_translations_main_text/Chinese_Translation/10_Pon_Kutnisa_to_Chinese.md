# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Pon Okikirmui yaieyukar, “Kutnisa kutunkutun” 小オキキリムイが自ら歌った謡「クツニサ クトンクトン」

## This is translated from English translation.

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
Translate the following text from English to Chinese. The original text is translation from Japanese which is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original meaning. Use modern Chinese. Display in Traditional Chinese. Only allow Chinese and English characters.
If a term cannot be translated, keep the original language.

This is the song sung by Little Okikirmui himself:
"Kutunisa Kutonkuton"

Kutunisa Kutonkuton,
One day, I went to play near the source of the river.
There, I saw a little man,
Bending over, hammering stakes to build a walnut weir.
When he saw me, he said,
"Who are you? My nephew, please help me."
I looked and saw it was a walnut weir.
Walnut water, muddy water,
Flowed, and the salmon,
Hated the walnut water and cried as they returned.
I was enraged,
I snatched the mallet from the little man,
And struck him in the center of his back with a *pon* sound.
I broke the little man's back and killed him,
And kicked him down to hell.
I shook his walnut stake,
It seemed to reach beyond the six hells.
Then, I put all the strength in my back, all the strength in my body,
And broke the stake from its base,
And kicked it down to hell.
Clear wind, clear water,
Flowed from the source, and the salmon,
Who had cried as they returned,
Regained their spirit in the clear wind and clear water,
And frolicked and laughed as they played,
Splashing as they swam upstream.
Seeing this, I was relieved,
And returned along the stream.
So told Little Okikirmui.
```

### Output
```
這是小Okikirmui親自吟唱的歌：
「Kutunisa Kutonkuton」

Kutunisa Kutonkuton，
某日，我前往河源嬉戲。
在那裡，我看見一個小矮人，
彎著腰，敲打木樁，建造胡桃木堰。
他看見我，便說道：
「你是誰？我的姪子，請你幫幫我。」
我仔細一看，原來是胡桃木堰。
胡桃木水，混濁的水，
流淌著，鮭魚們，
厭惡胡桃木水，哭泣著返回。
我怒火中燒，
我從小矮人手中奪過木槌，
砰的一聲，擊中他的背脊中央。
我打斷了小矮人的背，殺了他，
並將他踢下地獄。
我搖晃他的胡桃木樁，
它似乎延伸到了六層地獄之外。
然後，我將全身的力氣，背部的力量，
全部集中起來，將木樁從根部折斷，
並將它踢下地獄。
清風，清水，
從源頭流淌而出，鮭魚們，
原本哭泣著返回的牠們，
在清風和清水中恢復了精神，
嬉戲玩耍，歡笑著，
拍打著水花，逆流而上。
看到這一幕，我感到欣慰，
便沿著溪流返回。
小Okikirmui如此講述。
```
