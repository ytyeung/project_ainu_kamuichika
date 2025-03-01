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
Translate the following text from Japanese to Chinese. The original text is footnote. Keep the original meanings. For the text which are not in Japanese, keep the original form. Display in Traditional Chinese.

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
好的，以下是日文文獻的翻譯，將日文翻譯成繁體中文，其餘部分保持不變：

(1) 以前男孩子稍微長大一點，就會製作小弓箭給他。孩子們就用它來射樹木或鳥類等作為目標來玩耍，不知不覺中就精通了弓箭的技術。
ak......是弓術, shinot 是遊戯, ponai 是小矢.

(2) shiktumorke......眼神。
想了解一個人的本性時，看他的眼神最清楚，如果稍微左顧右盼，就會被訓斥。

(3) achikara......「骯髒」的意思。

(4) 鳥或野獸被人射落，是因為想要人製作的箭，說是為了取箭。

(5) kotankorkamui......擁有國家或村莊的神。
山裡有 nupurikorkamui......擁有山的神（熊）和 nupuripakorkamui......擁有山東方的神（狼）等，貓頭鷹的地位僅次於熊和狼。
kotankorkamui 不像山神、山東方的神那樣粗暴慌張。因此平時總是沉著冷靜，總是閉著眼睛，除非有非常重大的事情才會睜開眼睛。

(6) eharkiso......左邊的座位。

(7) eshiso......右邊的座位。
家中央有爐灶，有窗戶的那一側是上座，從上座看過去，右邊是 eshiso，左邊是 harkiso。坐在上座的僅限男子。如果是客人等，身份比主人低的人會避免坐在上座。右邊的座位一定是主人夫婦並排坐著。右座的下一個是左座，西側（靠近門口）的座位是末座。

(8) hayokpe 冑（頭盔）。
鳥或野獸在山裡的時候，人類的眼睛看不見，但各自都有像人類一樣的家，大家都過著和人類一樣的生活，到人類的村莊來的時候，會戴上頭盔。鳥或野獸的屍體是頭盔，本體是眼睛看不見的，但在屍體的耳朵和耳朵之間。

(9) otuipe......斷了尾巴的傢伙。
像狗一樣斷了尾巴的短尾巴不太受重視。
會用 wenpe......壞傢伙, otuipe......斷了尾巴的傢伙來辱罵極其無用的人。

(10) chikashnukar. 神非常喜歡某個人的時候，在完全意想不到的地方，賜予這個人很大的幸福，這個人就會說 ikashnukar an 來表達喜悅。

(11) apehuchi......火的老婦。火神是家中最尊貴的神，一定是老奶奶。山神或海神，以及其他各種神明像貓頭鷹一樣成為客人來到家裡時，由這位 apehuchi 主持，負責招待客人和談話。也可以直接稱呼為 kamuihuchi（神老婦）。

(12) neusar 互相交談。
互相交談各種世間閒話也稱為 neusar。一般來說，像 kamuiyukar（神謠）或 uwepeker（昔話）之類的東西稱為 neusar。

(13) ashke a uk. ashke 是手指、手。a uk 是拿取。指有慶祝活動時邀請人。

(14) kakkokhau......杜鵑鳥的叫聲。
杜鵑鳥的叫聲清晰響亮，因此會用杜鵑鳥來形容說話清楚明瞭，大家都聽得懂的人。

(15) chisekorkamui......擁有房子的神。
火神是主婦，家神就像是主人。男性則稱為 chisekorekashi......擁有房子的老爺爺。

(16) nusakorkamui......擁有御幣棚的神，老婦。
御幣棚的神一定是女性。有變故時會顯靈給人類看，據說那時會借用蛇的形狀顯靈。因此在御幣棚附近，或是在東邊窗戶附近，如果出現蛇，就會說「一定是御幣棚的老奶奶有事外出」，絕對不會殺死那條蛇。據說殺了會受到懲罰。

```