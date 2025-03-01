# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Chironnup yaieyukar, “Towa towa to” 狐が自ら歌った謡「トワトワト」

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
Translate the following text from English to Chinese. The original text is translation from Japanese which is footnotes of Ainu chant. 
Keep the original meaning. Use modern Chinese. Display in Traditional Chinese. Only allow Chinese and English characters.
If a term cannot be translated, keep the original language.

1.  isoeonkami.iso refers to the sea, eonkami refers to the act of apologizing for something.
It is believed that when a whale washes ashore, the Great God of the Sea brings it himself to give to humans, and washes it ashore. At that time, important people dress up formally and worship facing the sea.

2.  ononno. This is a word that people say repeatedly when someone returns from hunting in the mountains or at sea with some game.

3.  uniwente...... A ritual performed after a major flood, fire, volcanic eruption, or other natural disasters, or when someone is eaten by a bear, falls into the sea or river, or is injured or dies due to any unusual event.
At that time, they exchange words of condolence while pointing the tips of spears and swords at each other. When a disaster victim appears in one village, many representatives from neighboring villages gather in that village to perform the ritual, but it can also be done between two people.

4.  hokokse...... A man's cry to ask for help from the gods during uniwente or when a terrible event has occurred. "Hohho-i," and this is limited to men.

5.  ashur means unusual news, ek means to come.
......When someone who has traveled far from the village becomes ill or dies, a messenger comes from that place to the person's hometown to report the unusual event, or when someone comes to the village to report that someone has died in another village, or that something unusual has happened.
That messenger is called ashurkorkur (person with unusual news).
When ashurkorkur comes near the village, he first shouts loudly hokokse (Hohho-i). Then, the villagers who hear it also shout loudly and go out to the edge of the village to greet him and hear the unusual news.

6.  uchishkar...... Crying together. This is a woman's greeting, when they meet after a long separation, when a close relative has died, or when someone has been in great danger and has finally escaped, women hold hands or hug each other's heads or shoulders and cry.

7.  matrimimse (woman's cry)...... In case of a sudden change or in the case of uniwente, men make a loud voice of hokokse (Hohho-i), but women shout in a thin voice, "Ho-i."
It is said that women's voices are higher and stronger than men's voices, so they reach the ears of the gods first. Therefore, when a sudden event occurs, even men make a thin voice like women and shout two or three times.

8.  peutanke...... Has the same meaning as rimimse, but this is a commonly used word, while rimimse is a slightly difficult word.

```

### Output
```
1. isoeonkami.iso 指的是海洋，eonkami 指的是為某事道歉的行為。
人們相信，當鯨魚被沖上岸時，是海神親自將其帶給人類，並將其沖上岸。屆時，重要人物會正式著裝，面向大海祭拜。

2. ononno. 這是一個當有人從山裡或海上帶著獵物回來時，人們會重複說的詞語。

3. uniwente...... 在發生重大洪水、火災、火山爆發或其他自然災害之後，或者當有人被熊吃掉、掉入海或河流中，或因任何不尋常的事件而受傷或死亡時，所舉行的儀式。
屆時，他們會互相指向矛和劍的尖端，同時交換慰問之詞。當一個村莊出現災難受害者時，許多來自鄰近村莊的代表會聚集在該村莊舉行儀式，但也可以在兩個人之間進行。

4. hokokse...... 男人在 uniwente 期間或發生可怕事件時，向神靈尋求幫助的呼喊。「Hohho-i」，這僅限於男性。

5. ashur 意思是不同尋常的消息，ek 意思是到來。
......當有人遠離村莊生病或死亡時，會從那個地方派一個信使到這個人的家鄉，報告這個不尋常的事件，或者當有人來到村莊報告有人在另一個村莊死亡，或者發生了什麼不尋常的事情。
那個信使被稱為 ashurkorkur（帶有不尋常消息的人）。
當 ashurkorkur 靠近村莊時，他首先大聲喊叫 hokokse (Hohho-i)。然後，聽到它的村民也大聲喊叫，走到村莊的邊緣迎接他，並聽取不尋常的消息。

6. uchishkar...... 一起哭泣。這是女性的問候語，當她們在長期分離後相遇，當一個近親去世，或者當有人處於極大的危險之中並最終逃脫時，女性會手牽手或互相擁抱頭部或肩膀並哭泣。

7. matrimimse (女人的哭聲)...... 在發生突發變化或 uniwente 的情況下，男人會發出很大的 hokokse (Hohho-i) 聲音，但女人會用細細的聲音喊「Ho-i」。
據說女性的聲音比男性的聲音更高更強，所以她們的聲音首先傳到神靈的耳朵裡。因此，當發生突發事件時，即使是男人也會像女人一樣發出細細的聲音，並喊叫兩三聲。

8. peutanke...... 與 rimimse 具有相同的含義，但這是一個常用的詞，而 rimimse 是一個稍微難懂的詞。
```
