
prefixTable = {
    ""  : 0 ,  "k" : 5 ,  "s" : 10,  "t" : 15,  "n" : 20,
    "h" : 25,  "m" : 30,  "y" : 35,  "r" : 40,  "w" : 45,
    "g" : 50,  "z" : 55,  "d" : 60,  "p" : 65,  "b" : 70,
    "j" : 75,  "ky": 80,  "sh": 85,  "ny": 90,  "hy": 95,
    "py": 100, "by": 105, "my": 110, "ch": 115, "ry": 120, 
    "gy": 125, "f" : 130, "ts": 135, "v" : 140, 
    "elongations"  : 145,
    "nn" : 150, ".": 151, "," : 152, "smalltsu" : 153, " " : 154,
    "oh" : 155 
    }

romajitable = {}

# this will include things like "smalltsu" and "nn" but
#  romajitable is intended for the romaji algorithm
#  further below
for eachKey in prefixTable:
    romajitable[prefixTable[eachKey]] = eachKey


# prefixTable.setdefault()
# Mostly for readability. I.E. if x in vowels:
vowels           = {"a": 0, "i": 1, "u": 2, "e": 3, "o": 4}
japvowelstr      = "aiueo"
doubleConsonants = ["k", "p", "s", "t"]
beginningLetters = ["k", "s", "t", "n", "h", "m", "y", "r", "w",
                    "g", "z", "d", "p", "b", "j", "c", "f", "v"]
secondLetters    = ["y", "h", "s"] # No, there isn't a lot
pronouncination  = [".", ",", " "]

# Move these into a more appriopriate spot
transliterableString = " abcdefghijklmnopqrstuvwxyz,."
ycompoundstring      = "knhpbmrg"
hcompoundstring      = ["sh", "ch"]
nullcompoundstring   = "j"
compounders          = "ゃゅょャュョ"

# ゃ ゅ ょ
hiraganaTable = [
    "あ", "い", "う", "え", "お", # No consonants
    "か", "き", "く", "け", "こ", # K 
    "さ", "?",  "す", "せ", "そ", # S
    "た", "?",  "?",  "て", "と", # T
    "な", "に", "ぬ", "ね", "の", # N
    "は", "ひ", "?",  "へ", "ほ", # H
    "ま", "み", "む", "め", "も", # M
    "や", "?",  "ゆ", "?",  "よ", # Y
    "ら", "り", "る", "れ", "ろ", # R
    "わ", "?",  "?",  "?", "?", # W 
    "が", "ぎ", "ぐ", "げ", "ご", # G
    "ざ", "?",  "ず", "ぜ", "ぞ", # Z
    "だ", "?",  "?",  "で", "ど", # D
    "ぱ", "ぴ", "ぷ", "ぺ", "ぽ", # P
    "ば", "び", "ぶ", "べ", "ぼ", # B

    "じゃ", "じ", "じゅ", "?", "じょ", # J
    "きゃ", "?",  "きゅ", "?", "きょ", # Ky
    "しゃ", "し", "しゅ", "?", "しょ", # Sh
    "にゃ", "?",  "にゅ", "?", "にょ", # Ny
    "ひゃ", "?",  "ひゅ", "?", "ひょ", # Hy
    "ぴゃ", "?",  "ぴゅ", "?", "ぴょ", # Py
    "びゃ", "?",  "びゅ", "?", "びょ", # By
    "みゃ", "?",  "みゅ", "?", "みょ", # My
    "ちゃ", "ち", "ちゅ", "?", "ちょ", # Ch
    "りゃ", "?",  "りゅ", "?", "りょ", # Ry
    "ぎゃ", "?",  "ぎゅ", "?", "ぎょ", # Gy

    "?", "?", "ふ", "?", "?", # F
    "?", "?", "つ", "?", "?", # Ts
    "?", "?", "?",  "?", "?", # V, which doesn't exist 
                              #  in Hiragana.


    "あ", "い", "う", "い", "う", # Elongations
    "ん", "。", "、", "っ", " ",
    "を", "?" # hiraganaTable[-1]
    ]

katakanaTable = [
    "ア", "イ", "ウ", "エ", "オ", # No consonants
    "カ", "キ", "ク", "ケ", "コ", # K 
    "サ", "?",  "ス", "セ", "ソ", # S
    "タ", "ティ","トゥ","テ","ト", # T
    "ナ", "ニ", "ヌ", "ネ", "ノ", # N
    "ハ", "ヒ", "?",  "ヘ", "ホ", # H
    "マ", "ミ", "ム", "メ", "モ", # M
    "ヤ", "?",  "ユ", "?",  "ヨ", # Y
    "ラ", "リ", "ル", "レ", "ロ", # R
    "ワ", "ウィ","?", "ウェ","ウォ", # W 
    "ガ", "ギ", "グ", "ゲ", "ゴ", # G
    "ザ", "?",  "ズ", "ゼ", "ゾ", # Z
    "ダ", "ディ","デュ","デ","ド", # D
    "パ", "ピ", "プ", "ペ", "ポ", # P
    "バ", "ビ", "ブ", "ベ", "ボ", # B

    "ジャ", "ジ", "ジュ", "ジェ","ジョ", # J
    "キャ", "?",  "きゅ", "?", "キョ",  # Ky
    "シャ", "シ", "シュ", "シェ","ショ", # Sh
    "ニャ", "?",  "ニュ", "?", "ニョ", # Ny
    "ヒャ", "?",  "ヒュ", "?", "ヒョ", # Hy
    "ピャ", "?",  "ピュ", "?", "ピョ", # Py
    "ビャ", "?",  "ビュ", "?", "ビョ", # By
    "ミャ", "?",  "ミュ", "?", "ミョ", # My
    "チャ", "チ", "チュ", "チェ", "チョ", # Ch
    "リャ", "?",  "リュ", "?", "リョ", # Ry
    "ギャ", "?",  "ギュ", "?", "ギョ", # Gy

    "ファ", "フィ", "フ", "フェ", "フォ", # F
    "ツァ", "ツィ", "ツ", "ツェ", "ツォ", # Ts
    "ヴァ", "ヴィ", "?",  "ヴェ", "ヴォ", # V

    "ー", "ー", "ー", "ー", "ー", # Elongations
    "ン", "。", "、", "ッ", " ",  # etc.
    "ヲ", "?" # katakanaTable[-1]
    ]

# Short forms
hir = hiraganaTable
kat = katakanaTable

# The Romaji is the string with latin characters to convert into
#  either katakana or hiragana. Writing is either the dictionary
#  "hiraganaTable" (for hiragana) or "katakanaTable" (for katana)
def parseJ(romaji, writing):
    japanese = "\0"
    romaji   = romaji.lower()
    c        = 0

    while c < len(romaji):
        vowel    = ''
        posbe    = ''
        basiclen = 0

        # If its a space, ,/., or a non-letter character,
        #  do that first
 
        if romaji[c] in pronouncination:
            japanese += writing[prefixTable[romaji[c]]]
            c += 1
            continue
        if romaji[c] not in transliterableString:
            japanese += romaji[c]
            c += 1
            continue

        # Special Particles:
        # These particles must be surrounded by a space, a comma,
        #  a period, or something that is not a letter (whitespace
        #  for example)
        # Wa (spelled as ha)
        if (
            c + 2 < len(romaji) and
            (japanese[-1] in pronouncination 
                or japanese[-1] not in transliterableString)  and
            (romaji[c+2]  in pronouncination 
                or romaji[c+2] not in transliterableString)   and
            (romaji[c] + romaji[c+1]) == "wa" 
        ):
            japanese += writing[25] 
            c += 2
            continue
        # (w)o
        elif (
            c + 1 < len(romaji) and
            (japanese[-1] in pronouncination 
                or japanese[-1] not in transliterableString)  and
            (romaji[c+1]  in pronouncination 
                or romaji[c+1] not in transliterableString)   and
            romaji[c]    == "o"
        ):
            japanese += writing[155]
            c += 1
            continue


        # Vowel only
        if romaji[c] in vowels:
            basiclen = 1
            japanese += writing[vowels[romaji[c]]]
        # one or two consonsant then a vowel
        elif romaji[c] in beginningLetters:
            posbe = romaji[c]
            basiclen = 1

            # Test to see if another consonsant follows it
            if c + 1 < len(romaji) and romaji[c+1] in secondLetters:
                basiclen = 2
                posbe   += romaji[c+1]

            # Then look for a vowel
            if (c + basiclen < len(romaji) and 
                romaji[c + basiclen] in vowels
            ):
                append = writing[prefixTable[posbe] 
                               + vowels[romaji [c + basiclen]]]
                japanese += append
                #c += 1 + basiclen
                basiclen += 1
            else:
                japanese += "?"
                c += 1
                continue  
        else:
            japanese += "?"
            c += 1
            continue

        # elongation (only one allowed - maybe allow more for onomotopoiea?)
        if (c + basiclen < len(romaji) and 
            romaji[c + basiclen] in vowels and
            romaji[c + basiclen - 1] == romaji[c + basiclen]
        ):
            index  = (prefixTable["elongations"] 
                      + vowels[romaji[c + basiclen]])
            append = writing[index]
            japanese += append
            basiclen += 1

        # Is there an n after it and there's no vowel?
        if (c + basiclen + 1 < len(romaji) and
            romaji[c + basiclen] == "n" and
            romaji[c + basiclen + 1] not in vowels
        ):
            n = writing[150]
            japanese += n
            basiclen += 1
        # Is there an n /and/ its the last thing there is?
        elif (c + basiclen == len(romaji) - 1 and
            romaji[c + basiclen] == "n"
        ):
            n = writing[150]
            japanese += n
            basiclen += 1
        # Is it a double consonant?
        elif (c + basiclen + 1 < len(romaji) and
              romaji[c + basiclen] == romaji[c + basiclen + 1] and
              romaji[c + basiclen] in doubleConsonants
        ):
            japanese += writing[153]
            basiclen += 1
 
        c += basiclen        
    # while loop end is here

    return japanese[1:]

def parseJlist(romajiList, writing): # probably not useful.
    x = []
    for eachstring in romajiList:
        x.append(parseJ(eachstring, writing))
    return x

def intoRomaji(kanaString):
    returnstr = ""
    i = 0

    while i < len(kanaString):
        character = kanaString[i]

        if not (character in hir or character in kat):
            returnstr += character
            i += 1
            continue

        if character in hir:
            charcode = hir.index(character)

        elif character in kat:
            charcode = kat.index(character)


        if charcode < 145:
            vowel     = japvowelstr[charcode % 5]
            prefix    = romajitable[charcode - (charcode % 5)]

            #ゃゅょャュョ
            # Kya, kyo, shi, tsa, etc.. They'll need to be seperate
            #  logic for new katakana "wi", "tu", "ti", etc.
            if i + 1 != len(kanaString) and kanaString[i+1] in compounders:
                nextvowel = kanaString[i+1]
                nextpart  = "?"
                firstpart  = "?"
                if nextvowel == "ゃ" or nextvowel == "ャ":
                    nextpart = "a"
                elif nextvowel == "ゅ" or nextvowel == "ュ":
                    nextpart = "u"
                elif nextvowel == "ょ" or nextvowel == "ョ":
                    nextpart = "o"
                if prefix in ycompoundstring:
                    firstpart = prefix[0] + "y"
                elif prefix in hcompoundstring:
                    firstpart = prefix[0] + "h"
                elif prefix in nullcompoundstring:
                    firstpart = prefix[0] 

                returnstr += (firstpart + nextpart)
                i += 1 # We'll want to skip over the small "y[auo]"!
            else:
                returnstr += (prefix + vowel)

        # We came across a double consonant (such as the first
        #  p in "nippon"). It requires a special algorithm
        elif charcode == 153:
            if i == len(kanaString) - 1: pass # End of string
            else:
                # This may return something other then s, p, b, or t
                #  if the string input is not a correct kana string
                returnstr += intoRomaji(kanaString[i+1])[0]
        else:
            returnstr += character

        i += 1

    return returnstr


# create a dict from from a dictionary of "romaji": "english" pair
#  that'll have the form "romaji": "writing (hiragana or katakana"
def translationDict(romajiDictionary, writing):
    x = {}
    for eachstring in romajiDictionary:
        i = parseJ(eachstring, writing)
        x[i] = romajiDictionary[eachstring]
    return x


class JapaneseWord:

    def __init__(self, english, japanese, kanji = None):
        this.english  = english
        this.japanese = japanese
        this.kanji    = kanji

    def asEng(self):
        return this.english

    def asJap(self):
        return this.japanese

    def asKan(Self):
        return this.kanji


def tests():
    print (hiraganaTable[prefixTable["ky"] + vowels["o"]])
    print (hiraganaTable[prefixTable["m"]  + vowels["u"]]) 
    print (parseJ(" wa o aieuo", hiraganaTable))
    print (parseJ(" wa o aieuo", katakanaTable))
    print (parseJ("wa o aieuo ha sa hasa hya tsu tsi", hiraganaTable))
    print (parseJ("wa o aieuo ha sa hasa hya tsu tsi", katakanaTable))
    print (parseJ("myaa kyoo", hiraganaTable))
    print (parseJ("myaa kyoo", katakanaTable))
    print (parseJ("kyuushu", hir))
    print (parseJ("kyuushu", kat))
    print (parseJ("konohana sakuya ninja nippon", hir))
    print (parseJ("konohana sakuya ninja nippon", kat))

    print (parseJ(" o\n", hir))

    # My name is Mike Solomon
    print (
        parseJ("Watashi no onamae wa ", hir) +
        parseJ("Maiku soromon ", kat) +
        parseJ("desu.", hir)
    )

    # My hobby is ninjutsu
    print (parseJ("\nWatashi no shumi wa ninjutsu desu.", hir))

    # One plus 2 is...\n ...3!
    print (parseJ("1 + 2 wa...\n ...san desu!", hir))

    #つ
    print(intoRomaji("るム123ッカャつカ つッ") + "\n")
    print(intoRomaji("きゃ きゅ ちゅ しゅ ジャ") + "\n")
    # There's a chance I may be forgetting how some new katakana works...
    print(intoRomaji("ヴャ ヴ ヴィ") + "\n")


if __name__ == "__main__":
    tests()