# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of Chiri's footnotes on

## Kamuichikap kamui yaieyukar, “Shirokanipe ranran pishkan” 梟の神の自ら歌った謡「銀の滴しずく降る降るまわりに」

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
Translate the following text from Japanese to English. The original text is footnote. Keep the original meanings. For the text which are not in Japanese, keep the original form.

(1) 昔は男の子が少し大きくなると,小さい弓矢を作って与えます.子供はそれで樹木や鳥などを的に射て遊び,知らずしらずの中に弓矢の術に上達します.
ak......は弓術,shinot は遊戯,ponai は小矢.
(2) shiktumorke......眼つき.
人の素性を知ろうと思う時は,その眼を見ると一ばんよくわかると申しまして,少しキョロキョロしたりすると叱られます.
(3) achikara......「汚い」という意味.
(4) 鳥やけものが人に射落されるのは,人の作った矢が欲しいので,その矢を取るのだと言います.
(5) kotankorkamui......国または村を持つ神.
山には,nupurikorkamui......山を持つ神(熊)と nupuripakorkamui......山の東を持つ神(狼)などがあって,ふくろうは熊,狼の次におかれます.
kotankorkamui は山の神,山の東の神,の様に荒々しいあわて者ではありません.それでふだんは沈おち着いて,眼をつぶってばかりいて,よっぽど大変な事のある時でなければ眼を開かないと申します.
(6) eharkiso......左の座.
(7) eshiso......右の座.
家の央に囲炉裏いろりがあって,東側の※(「窗/心」、第3水準1-89-54)のある方が上座,上座から見て右が eshiso 左が harkiso.上座に坐るのは男子に限ります.お客様などで,家の主人よりも身分の卑しい人は上座につく事を遠慮します.右の座には主人夫婦がならんですわる事にきまっています.右座の次が左の座で,西側(戸口の方)の座が一ばん下座になっています.
(8) hayokpe 冑.
鳥でもけものでも山にいる時は,人間の目には見えないが,各々に人間の様な家があって,みんな人間と同じ姿で暮していて,人間の村へ出て来る時は冑を着けて出て来るのだと云います.そして鳥やけものの屍体は冑で本体は目には見えないけれども,屍体の耳と耳の間にいるのだと云います.
(9) otuipe......尻の切れた奴.
犬の尻尾の切れた様に短いのはあまり尊びません.
極くつまらない人間の事を wenpe......悪い奴,otuipe......尻尾の切れた奴と悪口をします.
(10) chikashnukar.神が大へん気に入った人間のある時,ちっとも思いがけない所へ,その人間に何か大きな幸を恵与すると,その人は ikashnukar an と云ってよろこびます.
(11) apehuchi......火の老女.火の神様は,家の中で最も尊い神様でおばあさんにきまっています.山の神や海の神,その他種々な神々がこのふくろうの様にお客様になって,家へ来た時は,この apehuchi が主になって,お客のお相手をして話をします.ただ kamuihuchi(神老女)と云ってもいい事になっています.
(12) neusar 語り合う事.
種々な世間話を語り合うのも neusar.普通 kamuiyukar(神謡)や uwepeker(昔譚)の様なものを neusar と云います.
(13) ashke a uk.ashke は指,手.a uk は取る.なにか祝いがあるとき人を招待する事を云います.
(14) kakkokhau......カッコウ鳥の声.
カッコウ鳥の声は,美しくハッキリと耳に響きますから,ハキハキとしてみんなによくわかるように物を云う人の事をカッコウ鳥の様だと申します.
(15) chisekorkamui......家を持つ神.
火の神が主婦で,家の神が主人の様なものです.男性で chisekorekashi......家を持つおじいさんとも申します.
(16) nusakorkamui......御幣棚を持つ神,老女.
御幣棚の神も女性にきまっています.何か変事の場合人間にあらわれる事がありますが,その時は蛇の形をかりてあらわれると云います.それで御幣棚の近所に,または東の方の窗の近所に,蛇が出て来たりすると,「きっと御幣棚のおばあさんが用事があって外出したのだろう」と言って,決してその蛇を殺しません.殺すと罰が当りますと云います.
```

### Output
```
Okay, here are the English translations of the footnotes, preserving the original meanings and keeping non-Japanese text as is:

(1) In the old days, when a boy got a little older, they would make and give him a small bow and arrow. The child would play by shooting at trees and birds, unknowingly becoming skilled in archery.
ak...... archery, shinot is play, ponai is small arrow.

(2) shiktumorke...... the look in one's eyes.
It is said that if you want to know a person's true nature, the best way is to look at their eyes, and they would be scolded if they looked around restlessly.

(3) achikara...... means "dirty."

(4) It is said that birds and animals are shot down by people because they want the arrows made by people, and they are taking the arrows.

(5) kotankorkamui...... a god who possesses a country or village.
In the mountains, there are nupurikorkamui...... a god who possesses a mountain (bear) and nupuripakorkamui...... a god who possesses the east of the mountain (wolf), and the owl is ranked after the bear and wolf.
kotankorkamui is not a rough and hasty person like the mountain god or the god of the east of the mountain. Therefore, they are usually calm and always have their eyes closed, and it is said that they only open their eyes when something very serious happens.

(6) eharkiso...... the left seat.

(7) eshiso...... the right seat.
In the center of the house is a hearth, and the side with the ※(「窗/心」) on the east side is the upper seat. Looking from the upper seat, the right is eshiso and the left is harkiso. Only men can sit in the upper seat. Guests who are of lower status than the head of the house will refrain from taking the upper seat. It is customary for the master and mistress of the house to sit side by side in the right seat. The left seat is next to the right seat, and the seat on the west side (towards the doorway) is the lowest seat.

(8) hayokpe helmet.
It is said that when birds and animals are in the mountains, they are invisible to human eyes, but each has a house like a human, and they all live in the same form as humans, and when they come to human villages, they wear helmets. And it is said that the corpses of birds and animals are helmets, and the main body is invisible, but it is between the ears of the corpse.

(9) otuipe...... a guy with a cut-off butt.
A tail that is short like a dog's cut-off tail is not highly valued.
They use abusive language to describe extremely insignificant people as wenpe...... a bad guy, otuipe...... a guy with a cut-off tail.

(10) chikashnukar. When a god is very pleased with a human, and bestows some great fortune on that person in a completely unexpected place, that person rejoices, saying ikashnukar an.

(11) apehuchi...... old woman of fire. The fire goddess is the most revered goddess in the house and is always an old woman. When mountain gods, sea gods, and other various gods come to the house as guests like this owl, this apehuchi takes the lead in entertaining and talking to the guests. It is also acceptable to simply say kamuihuchi (god old woman).

(12) neusar talking to each other.
Talking about various worldly matters is also neusar. Usually, things like kamuiyukar (god song) and uwepeker (old tales) are called neusar.

(13) ashke a uk. ashke is finger, hand. a uk is to take. It means inviting people when there is a celebration.

(14) kakkokhau...... the voice of the cuckoo bird.
Because the voice of the cuckoo bird is beautiful and clear, people who speak clearly and understandably to everyone are said to be like cuckoo birds.

(15) chisekorkamui...... a god who possesses a house.
The fire god is like the housewife, and the house god is like the master of the house. He is also called chisekorekashi...... an old man who owns a house.

(16) nusakorkamui...... a god who possesses a sacred shelf, an old woman.
The god of the sacred shelf is also always a woman. In the event of an emergency, she may appear to humans, but at that time, she appears in the form of a snake. Therefore, if a snake appears near the sacred shelf or near the east window, they say, "The old woman of the sacred shelf must have gone out on business," and they never kill the snake. It is said that if you kill it, you will be punished.

```