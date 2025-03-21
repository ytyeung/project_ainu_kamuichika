# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Kamuichikap Kamui yaieyukar, “Konkuwa” 梟の神が自ら歌った謡「コンクワ」

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
Translate the following text from Japanese to Chinese. The original text is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original Japanese meaning accurately. Use modern Chinese. Display in Traditional Chinese.
If a term cannot be translated, keep the original language.

梟の神が自ら歌った謡
         「コンクワ」

「コンクワ
昔私の物言う時は桜皮を巻いた弓の
弓把きゅうはの央を鳴り渡らす如くに
言ったのであったが,
今は衰え年老いてしまった事よ.
けれども誰か雄弁で
使者としての自信を持ってる者があったら,
天国へ五ツ半の談判
を言いつけてやりたいものだ.」と
たがつきのシントコの蓋の上をたたきながら
私は言った,ところが入口で誰かが
「私をおいて誰が使者として雄弁で
自信のあるものがあるでしょう.」というので
見ると鴉からすの若者であった.
私は家に入れて,それから,たがつきのシントコの
蓋の上をたたきながら
鴉の若者を使者にたてる為
その談判を云いきかせて三日たって
三つ目の談判を話しながら見ると
鴉の若者は炉縁の後で
居眠りをしている,それを見ると,癪しゃくに
さわったので鴉の若者を
羽ぐるみ引っぱたいて殺してしまった.
それから又たがつきのシントコの蓋の上を
たたきながら
「誰か使者として自信のある者が
あれば天国へ五ツ半の
談判を言いつけてやりたい.」と
言うと,誰かがまた入口へ
「誰が私をおいて,雄弁で
天国へ使者に立つほどの者がありましょう.」
と言うので見ると山のかけす
であった.
家へ入れてそれからまた
たがつきのシントコの蓋の上をたたきながら
五ツ半の談判を話して
四日たって,四つの用向を言っているうちに
山のかけすは炉縁の後で居眠りをしている.
私は腹が立って山のかけすを羽ぐるみひっぱたいて
殺してしまった.
それからまたたがつきのシントコの蓋の上を
たたきながら,
「誰か雄弁で使者として
自信のある者があれば,天国へ
五ツ半の談判を持たせてやりたい.」
と言うと,誰かが
慎つつしみ深い態度ではいって来たので見ると
川ガラスの若者,美しい様子で
左の座に坐った.それで私は
たがつきのシントコの蓋の上をたたきながら
五ツ半の用件を夜でも
昼でも言い続けた.見れば
川ガラスの若者,何も疲れた様子もなく
聞いていて昼と夜を
数えて六日目に
私が言い終ると直ぐに天窗から
出て天国へ行ってしまった.
その談判の大むねは,人間の世界に
饑饉があって人間たちは今にも
餓死しようとしている.どういう訳かと
見ると天国に
鹿を司つかさどる神様と魚を司る神様とが
相談をして鹿も出さず魚も出さぬことに
したからであったので,神様たちから
どんなに言われても知らぬ顔をして
いるので人間たちは猟に
山へ行っても鹿も無い,魚漁に
川へ行っても魚も無い.
私はそれを見て腹が立ったので
鹿の神,魚の神へ使者をたてた
のである.
それから幾日もたって
空の方に微かな音がきこえていたが
誰かがはいって来た.見ると
川ガラスの若者,今は前よりも美しさを増し
勇ましい気品をそなえて
返し談判を述べはじめた.
天国の鹿の神や魚の神が
今日まで鹿を出さず魚を出さなかった
理由は,人間たちが鹿を捕る時に
木で鹿の頭をたたき,皮を剥ぐと
鹿の頭をそのまま山の木原に
捨ておき,魚をとると
腐れ木で魚の頭をたたいて殺すので,
鹿どもは,裸で泣きながら
鹿の神の許もとへ帰り,魚どもは
腐れ木をくわえて魚の神の
許へ帰る.鹿の神,魚の神は
怒って相談をし,鹿を出さず
魚を出さなかったのであった.がこののち
人間たちが鹿でも魚でも
ていねいに取扱うという事なら鹿も出す
魚も出すであろう,と鹿の神と
魚の神が言ったという事を詳しく申し立てた.
私はそれを聞いてから川ガラスの若者に
讃辞を呈して,見ると本当に
人間たちは鹿や魚を
粗末に取扱ったのであった.
それから,以後は,決してそんな事をしない様に
人間たちに,眠りの時,夢の中に
教えてやったら,人間たちも
悪かったという事に気が付き,それからは
幣ぬさの様に魚をとる道具を美しく作り
それで魚をとる.鹿をとったときは,鹿の頭も
きれいに飾って祭る,それで
魚たちは,よろこんで美しい御幣ごへいをくわえて
魚の神のもとに行き,鹿たちは
よろこんで新しく月代さかやきをして鹿の神
のもとに立ち帰る.それを鹿の神や
魚の神はよろこんで
沢山,魚を出し,沢山,鹿を出した.
人間たちは,今はもうなんの困る事も
ひもじい事もなく暮している,
私はそれを見て安心をした.
私は,もう年老い,衰え弱った
ので,天国へ行こうと
思っていたのだけれども,私が守護している人間の国に
饑饉があって人間たちが餓死しようとしているのに
構わずに行く事が出来ないので,
これまで居たのだけれども,今はもう
なんの気がかりも無いから,最も強い者
若い勇者を私のあとにおき人間の世を
守護させて,今天国へ行く所なのだ.
と,国の守護神なる翁神(梟)が
物語って天国へ行きました.と.
```

### Output
```
貓頭鷹神親自吟唱的歌謠

「コンクワ」

「コンクワ
往昔我發言之時，如鳴響纏繞櫻花樹皮的弓，
弓把之央迴盪不已，
如今卻已衰老，年歲漸長。
然而，若有雄辯滔滔，
對使者之職充滿自信之人，
我願派遣其前往天國，進行五又二分之一的談判。」

我一邊敲擊著鑲邊的シントコ蓋子，一邊說道。此時，入口處傳來聲音：
「捨我其誰，能擔此雄辯之使者重任，充滿自信？」

我定睛一看，原來是隻年輕的烏鴉。
我將其迎入屋內，然後，一邊敲擊著鑲邊的シントコ蓋子，
為了派遣這年輕的烏鴉為使者，
我向其詳細講述談判內容，三日過去，
當我講述第三項談判要點時，卻發現
這年輕的烏鴉在爐邊打起了瞌睡。見此情景，我怒火中燒，
一把抓住年輕烏鴉的翅膀，將其活活打死。

隨後，我又敲擊著鑲邊的シントコ蓋子，
「若有對使者之職充滿自信之人，
我願派遣其前往天國，進行五又二分之一的談判。」

話音剛落，又有人在入口處說道：
「捨我其誰，能如此雄辯，
足以擔當前往天國的使者？」

我循聲望去，原來是隻山喜鵲。
我將其迎入屋內，然後再次
敲擊著鑲邊的シントコ蓋子，
向其講述五又二分之一的談判內容，
四日過去，當我講述第四項要點時，
這山喜鵲竟在爐邊打起了瞌睡。
我怒不可遏，一把抓住山喜鵲的翅膀，將其活活打死。

之後，我又敲擊著鑲邊的シントコ蓋子，
「若有雄辯滔滔，對使者之職
充滿自信之人，我願派遣其前往天國，
攜帶五又二分之一的談判內容。」

此時，有人以恭敬的姿態走了進來，我仔細一看，
原來是隻年輕的河烏，姿態優美，
端坐在左側。於是我
敲擊著鑲邊的シントコ蓋子，
不分晝夜地向其講述五又二分之一的要事。

只見這年輕的河烏，毫無疲憊之色，
靜靜地聆聽著，日夜兼程，
數到第六日，
我剛一講完，它便立刻從天窗
飛出，前往天國。

這場談判的大致內容是，人類世界
正遭受饑荒，人們瀕臨
餓死。究其原因，
原來是天國
掌管鹿的神明和掌管魚的神明
商議決定，不再降下鹿和魚，
無論人們如何懇求，他們都置之不理，
因此，人們前往山中
狩獵，卻一無所獲，前往河中
捕魚，也空手而歸。

我見此情景，怒火中燒，
遂派遣使者前往鹿神和魚神處。

數日過去，
空中傳來微弱的聲響，
有人走了進來。我定睛一看，
原來是那年輕的河烏，如今比之前更加俊美，
渾身散發著英勇的氣概，
開始陳述回覆的談判內容。

天國的鹿神和魚神
之所以至今不降下鹿和魚，
是因為人類在捕獲鹿時，
用木頭敲擊鹿的頭部，剝下鹿皮後，
便將鹿頭隨意丟棄在山林之中；
捕獲魚時，
用腐爛的木頭敲擊魚的頭部致其死亡，
因此，鹿群赤身裸體，哭泣著
回到鹿神的身邊，魚群
口銜腐爛的木頭，回到魚神的
身邊。鹿神和魚神
怒不可遏，商議決定，不再降下鹿和魚。

但如果今後
人類能夠善待鹿和魚，
那麼他們便會再次降下鹿和魚，
鹿神和魚神如此說道，並詳細陳述了緣由。

聽聞此言，我向年輕的河烏
表達了讚賞之情，並發現
人類確實
對待鹿和魚過於粗暴。

從那以後，為了讓人們不再重蹈覆轍，
我在他們入睡時，於夢中
告誡他們，人類也意識到
自己的過錯，從此以後，
他們像對待幣帛ぬさ一般，精美地製作捕魚工具，
用其捕魚。捕獲鹿時，也會將鹿頭
精心裝飾並祭祀，因此，
魚兒們歡欣鼓舞地銜著美麗的御幣ごへい
前往魚神的身邊，鹿兒們
也高興地梳理著新月代さかやき，回到鹿神的
身邊。鹿神和
魚神見此情景，喜出望外，
降下大量的魚，降下大量的鹿。

人類如今已不再有任何困擾，
也不再遭受饑餓之苦，
我見此情景，感到十分安心。

我已年老體衰，
本想前往天國，
但想到我所守護的人類國度
正遭受饑荒，人們瀕臨餓死，
我無法置之不理，
因此一直留在此處，但如今已
再無任何牽掛，我將選出最為強大、
年輕的勇者來繼承我的職位，守護人類世界，
而我，今日便將前往天國。」

國家的守護神，貓頭鷹翁神，
講述完畢，便前往天國了。故事到此結束。
```
