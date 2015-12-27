from japanese import *
import random



# class JapaneseWord:

#     def __init__(self, english, japanese, kanji = None):
#         this.english  = english
#         this.japanese = japanese
#         this.kanji    = kanji

#     def asEng(self):
#         return this.english

#     def asJap(self):
#         return this.japanese

#     def asKan(Self):
#         return this.kanji



romajiHiraganaDict1 = { 
    "karaage": "fried chicken",
    "gyuudon":  "beef on rice",
    "gyuuniku": "beef meat",
    "toriniku": "chicken meat",
    "sakana":  "fish",
    "iie":     "no",
    "tenpura": "vegatables and fried fish in batter",
    "jagaimo": "potato",
    "udon":    "noodles",
    "soba":    "buckwheat noodles",
    "sukiyaki": "beef and vegetables cooked in a pot",
    "tendon":  "tenpura on rice",
    "oyakodon": "fried egg on rice",
    "teichoku": "set meal",
    "tonkatsu": "pork cutlet",
    "ringo":    "apple",
    "mikan":   "mandarin orange",
    "yasai":   "vegetable",
    "niku":    "meat",
    "kyuuri": "cubumber",
    "kyabetsu": "cabbage",
    "tomago":  "egg" ,
    "yakizakana": "fried fish",
    "budoo":      "grape",
    "kudamono":   "fruit",
    "daigakusei": "university student",
    "gakusei":    "student",
    "ichi-nen":   "first year student",
    "ni-nen":     "second year student",
    "san-nen":    "third year student",
    "sensei":     "teacher",
    "igaku":      "medicine",
    "suugaku":    "mathematics",
    "koogaku":    "engineering",
    "denshikoogaku": "electronic engineering",
    "hoogaku":    "law",
    "butsuri":    "physics",
    "bungaku":    "literature",
    "kenchiku":   "architecture",
    "keizaigaku": "economics",
    "joohookoogaku": "computer science",
    "kagaku":     "chemistry",
    "ongaku":     "music",
    "shashin":    "photography",
    "ryoori":     "travelling",
    "ryokoo":     "cooking",
    "yamanobori": "mountain climbing",
    "suiei":      "swimming",
    "dokusho":    "reading",
    "eiga":       "movies",
    "konnichiwa": "good day",
    "konbanwa":   "good evening",
    "arigatoo gozaimasu": "thank you",
    "doo itashimashite": "you're welcome",
    "ohayoo gozaimasu": "good morning",
    "sayoonara":  "good-bye",
    "oyasuminasai": "good night",
    "chuugokujin": "Chinese", 
    "Nihonjin":   "Japanese", 
    "ryuugakusei": "overseas student",
    "daigakuinsei": "graduate student",
    "kenkyuuin":  "researcher",
    "kyooju":      "professor"
    }

# Note: nationalities will have a katakana -jin ending
#  instead of a regular hiragana -jin ending
romajiKatakanaDict1 = {
    "furai":      "french fries",
    "supagetti":  "spagetti",
    "tomato":     "tomato",
    "raamen":     "ramen",
    "kareeraisu": "curry rice",
    "piano":      "piano",
    "saikuringu": "cycling",
    "tenisu":     "tennis",
    "pinpon":     "ping-pong",
    "pan":        "bread",
    "Itariajin":  "Italian",
    "Indojin":    "Indian",
    "Taijin":     "Thai",
    "Amerikajin": "American",
    "Igirisujin": "Englishperson",
    "Ejiputojin": "Egyptian",
    "kanadajin":  "Canadian",
    "Doitsujin":  "German",
    "Furansujin": "Frenchperson",
    "Betonamujin": "Vietnamese",
    "Iranjin":    "Iranian",
    "Indoneshiajin": "Indonesian",
    "Oosutorariajin": "Australian",
    "Kankokujin": "Korean",
    "Firipinjin": "Filipino",
    "Roshiajin":  "Russian"
    }

hiraganaWordbank1 = translationDict(romajiHiraganaDict1, hiraganaTable)
katakanaWordbank1 = translationDict(romajiKatakanaDict1, katakanaTable)


totalWordbank1 = dict()
totalWordbank1.update(hiraganaWordbank1)#.update(katakanaWordbank1)
totalWordbank1.update(katakanaWordbank1)


# Do NOT use!!!
def randomHiraganaWord1():
    hirakeys = list(hiraganaWordbank1.keys())
    hiraword = random.choice(hirakeys)
    translation = hiraganaWordbank1[hiraword]
    print ("Write this in romaji (and know what it translates too): " + 
        hiraword)
    i = input()
    i.strip()
    # hirai = parseJ(i, hiragana)
    if i in romajiHiraganaDict1 and romajiHiraganaDict1[i] == translation:
        print ("...Correct! " + hiraword + " is " + i + 
            " meaning " + translation)
    else:
        print ("...Incorrect! " + hiraword + " is " + i + 
            " meaning " + translation)
    #print (hiraganaWordbank1.keys()[3])

def randomKanaWord(romajidict, transtable):
    romajikeys  = list(romajidict.keys())
    romajiword  = random.choice(romajikeys)
    kanaword    = parseJ(romajiword, transtable)
    translation = romajidict[romajiword]

    print ("Write this in romaji (and know what it translates to): " + 
        kanaword)

    i = input().strip()

    if i == romajiword:
        print ("...Correct! " + kanaword + " is " + romajiword + 
            " meaning " + translation)
    else:
        print ("...Incorrect! " + kanaword + " is " + romajiword + 
            " meaning " + translation)

def randomEnglishWord(romajidict, transtable):
    romajikeys  = list(romajidict.keys())
    romajiword  = random.choice(romajikeys)
    kanaword    = parseJ(romajiword, transtable)
    translation = romajidict[romajiword]

    print ("What is this in romaji? " + translation)

    i = input().strip()

    if i == romajiword:
        print ("...Correct! " + translation + " is " + romajiword + 
            ", or " + kanaword)
    else:
        print ("...Incorrect! " + translation + " is " + romajiword + 
            ", or " + kanaword)

if __name__ == "__main__":
    # for key in totalWordbank1:
    #     print ("'" + key + "': " + totalWordbank1[key])  
    for i in range(5):
        randomKanaWord(romajiHiraganaDict1, hiraganaTable)