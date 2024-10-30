import re
import MeCab

stop_words_japanese = [
    "は", "が", "を", "に", "で", "と", "へ", "も", "から", "まで",
    "より", "や", "し", "そして", "また", "それ", "これ", "あれ",
    "ここ", "そこ", "あそこ", "なに", "なん", "どこ", "いつ",
    "だれ", "なぜ", "どう", "です", "ます", "でした", "ますか",
    "ください", "ありません", "いる", "ある", "なる", "いう",
    "いく", "くる", "する", "いる", "よう", "こと", "もの", "それで",
    "しかし", "だから", "ですから", "でも", "ので", "けれども",
    "ながら", "のに", "たら", "たり", "とき", "ほど", "ばかり",
    "だけ", "なら", "ので", "んで", "など", "とか", "でも",
    "この", "その", "あの", "どの", "こんな", "そんな", "あんな",
    "どんな", "こんなに", "そんなに", "あんなに", "どんなに",
    "うえ", "した", "まえ", "うしろ", "みぎ", "ひだり", "なか",
    "そば", "そと", "うち", "あと", "まえ", "とき", "ところ",
    "ころ", "さい", "かた", "がた", "ついて", "について", "とともに",
    "そして", "それに", "さらに", "または", "および", "ならびに",
    "および", "ところが", "それでも", "しかも", "すなわち",
    "つまり", "したがって", "だって", "だけど", "けれど",
    "けれども", "のに", "のだから", "なのに", "それにもかかわらず",
    "ならびに", "および", "かつて", "なお", "または", "ならびに",
    "および", "なぜなら", "たとえば", "さて", "そういえば", "ところで",
    "なお", "さて", "ちなみに", "そのうえ", "すると", "やっぱり",
    "ついに", "つぎに", "そして", "それから", "そこで", "そして",
    "つまり", "すなわち", "おまけに", "またしても", "いっぽう",
    "ただし", "ただ", "もっとも", "ちなみに", "ところで", "けっきょく",
    "はたして", "やはり", "ついでに", "すると", "つぎ", "そのうえ",
    "ひとり", "ひとつ", "ふたり", "ふたつ", "みっつ", "よっつ",
    "いつつ", "むっつ", "ななつ", "やっつ", "ここのつ", "とお",
    "そして", "いえ", "それでも", "じゃあ", "ところで", "それでは",
    "すると", "そのうえ", "そのため", "それとも", "ところが",
    "たしかに", "たとえ", "ただし", "だからといって", "それでいて",
    "しかも", "おまけに", "それにしては", "それどころか", "それなのに",
    "さらに", "それにしても", "さっき", "たった", "ちょっと",
    "だいぶ", "すごく", "やっと", "ついに", "きっと", "ぜったい",
    "たぶん", "まさに", "ほんとうに", "もちろん", "もしかすると",
    "あまり", "とても", "やはり", "もっと", "できるだけ", "おそらく",
    "何", "どこ", "いつ", "誰", "なぜ", "どうして", "どの", "どれ", "どちら", "いくら", "どんな",
    "何", "誰", "どこ", "いつ", "どうして", "どう", "どれ", "どの",
    "いくつ", "いくら", "何時", "どんな", "なんで", "なぜ", "どちら",
    "どっち", "どれくらい", "何人", "何年", "何ヶ月", "何曜日", "どのくらい",
    "何故", "どのように", 'なん', 'なに', 'だれ', 'どこ', 'いつ', 'どうして',
    'どう', 'どれ', 'どの', "いくつ", "いくら", "なんで", "なぜ", "どちら", "どっち",
    "どれくらい", "なに", "だれ", "どこ", "いつ", "どうして", "どう", "どれ", "どの", "いくつ",
    "いくら", "なんで", "なぜ", "どちら", "どっち", "どれくらい", "何人", "何年", "何ヶ月", "何曜日",
    "どのくらい", "何故", "どのように", 'か'
]


def raw_process_query(raw_text, mecab=True):
    # Loại bỏ các ký tự không mong muốn
    # Loại bỏ ký tự đặc biệt nhưng giữ lại các ký tự tiếng Nhật
    text = re.sub(r'[^\w\sぁ-んァ-ン一-龥々ー]', '', raw_text)
    text = re.sub(r'\d+', '', text)  # Loại bỏ số

    # Tách từ sử dụng MeCab
    if mecab:
        mecab = MeCab.Tagger('-Owakati')
        text = mecab.parse(text).strip()
        clean_query = ' '.join(
            [word for word in text.split() if word not in stop_words_japanese])
        if clean_query == "":
            return raw_text
        else:
            return clean_query
    else:
        if text == "":
            return raw_text
        else:
            return text
    