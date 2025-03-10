# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of Chiri's footnotes on

## Chironnup yaieyukar, “Towa towa to” 狐が自ら歌った謡「トワトワト」

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
Translate the following text from Japanese to Chinese. The original text is footnote. Keep the original meanings. For the text which are not in Japanese, keep the original form. Display in Traditional Chinese.

(1) isoeonkami.iso は海幸,eonkami は......を謝す事.
鯨が岸で打ち上げられるのは,海の大神様が人間に下さる為に御自分で持って来て,岸へ打ち上げて下さるものだと信じて,その時は必ず重立った人が盛装して沖の方をむいて礼拝をします.
(2) ononno.これは海に山に猟に出た人が何か獲物を持って帰って来た時にそれを迎える人が口々に言う言葉です.
(3) uniwente......大水害のあと,火災のあと,火山の破裂のあと,その他種々な天災のあったあとなどに,または人が熊に喰われたり,海や川に落ちたり,その他なにによらず変った事で負傷したり,死んだりした場合に行う儀式の事.
その時は槍や刀のさきを互いに突き合せながらお悔みの言葉を交します.一つの村に罹災者が出来ると,近所の村々から沢山の代表者がその村に集ってその儀式を行いますが,一人と一人でも致します.
(4) hokokse......uniwente の時,また大へんな変り事が出来た時に神様に救いを求める時の男の叫び声.フオホホーイと,これは男に限ります.
(5) ashur は変った話,ek は来る.
......村から遠い所に旅に出た人が病気したとか死んだとかした時にその所からその人の故郷へ使者がその変事を知らせに来るとか,外の村で誰々が死にましたとか,何々の変った事がありましたとかと村へ人が知らせに来る事を云います.
その使者を ashurkorkur(変った話を持つ人)と云います.
ashurkorkur は村の近くへ来た時に先ず大声をあげて hokokse(フオホホーイ)をします.すると,それをききつけた村人は,やはり大声で叫びながら村はずれまで出迎えてその変り事をききます.
(6) uchishkar......泣き合う.これは女の挨拶,長く別れていて久しぶりで会った時,近親の者が死んだ時,誰かがなにか大変な危険にあって,やっと免れた時などに,女どうしで手を取り合ったり,頭や肩を抱き合ったりして泣く事.
(7) matrimimse(女の叫び声)......何か急変の場合または uniwente の場合,男は hokokse(フオホホーイ)と太い声を出しますが,女はほそくホーイと叫びます.
女の声は男の声よりも高く強くひびくので神々の耳にも先にはいると云います.それで急な変事が起った時には,男でも女の様にほそい声を出して,二声三声叫びます.
(8) peutanke......rimimse と同じ意ですが,これは普通よく用いられる言葉で,rimimse の方は少し難かしい言葉になっています.
```

### Output
```
好的，以下是日文文獻的翻譯，將日文翻譯成繁體中文，其餘文字保持不變。

(1) isoeonkami.iso 是海幸,eonkami 是......謝罪之意。
鯨魚擱淺在岸邊，是因為海神大人為了賜予人類，親自帶來並推上岸的，人們深信不疑，此時一定會由德高望重的人盛裝打扮，面向大海的方向進行禮拜。
(2) ononno. 這是出海或上山打獵的人，帶著獵物歸來時，迎接的人們異口同聲說出的話語。
(3) uniwente......大水災、火災、火山爆發等各種天災之後，或是有人被熊吃掉、落入海或河中，以及其他任何因變故而受傷或死亡的情況下所舉行的儀式。
屆時，人們會互相用槍或刀尖抵住對方，同時交換慰問之詞。一個村莊若有災民，鄰近村莊會派出許多代表聚集到該村莊舉行儀式，即使只有一個人也會舉行。
(4) hokokse......uniwente 時，或發生重大變故時，向神明祈求救助時男性的呼喊聲。フオホホーイ，僅限男性。
(5) ashur 是變故的消息,ek 是到來。
......從村莊遠方出外旅行的人，生病或死亡時，由該地派遣使者將變故告知其故鄉，或是從其他村莊有人來告知某某人過世了，或發生了某某變故等等，人們將這種情況稱為 ashur。
該使者被稱為 ashurkorkur（帶有變故消息的人）。
ashurkorkur 在靠近村莊時，首先會大聲呼喊 hokokse（フオホホーイ）。聽到呼喊聲的村民，也會大聲呼喊，並到村莊邊緣迎接，詢問變故的消息。
(6) uchishkar......互相哭泣。這是女性的寒暄方式，久別重逢時、近親過世時、有人遭遇重大危險好不容易脫險時等等，女性之間會手牽著手，或互相擁抱頭部或肩膀哭泣。
(7) matrimimse（女性的呼喊聲）......發生緊急情況或 uniwente 的情況時，男性會發出粗獷的 hokokse（フオホホーイ）聲，女性則會發出細微的ホーイ聲。
據說女性的聲音比男性的聲音更高亢響亮，因此能先傳入神明的耳中。因此，發生緊急變故時，即使是男性也會像女性一樣發出細微的聲音，呼喊兩三聲。
(8) peutanke......與 rimimse 相同的意思，但這是普通常用的詞彙，rimimse 則稍微是比較難的詞彙。

```