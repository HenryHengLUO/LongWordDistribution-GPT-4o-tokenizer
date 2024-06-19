import tiktoken
from langdetect import detect
from langdetect import detect_langs
import pandas as pd
import os



T = tiktoken.get_encoding("o200k_base")

length_dict = {}

for i in range(T.n_vocab):
    try:
        length_dict[i] = len(T.decode([i]))
    except:
        pass
      
# Sort by length
length_dict = dict(sorted(length_dict.items(), key=lambda item: -item[1]))


#Create a pandas dataframe
df_english = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_simplechinese = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_traditionchinese = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_japanese = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_french = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_german = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_spanish = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_italian = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_portuguese = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_korean = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
df_russian = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
<<<<<<< HEAD
=======
df_turkish = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word','Language Score'])
>>>>>>> 86d5be4 (second commit, add Turkish)






# Print the top 100 long words for each language
<<<<<<< HEAD
Num_engligh = Num_simplechinese = Num_traditionchinese = Num_japanese = Num_french = Num_german = Num_spanish = Num_italian = Num_portuguese = Num_korean = Num_russian = 1
=======
Num_engligh = Num_simplechinese = Num_traditionchinese = Num_japanese = Num_french = Num_german = Num_spanish = Num_italian = Num_portuguese = Num_korean = Num_russian = Num_turkish = 1
>>>>>>> 86d5be4 (second commit, add Turkish)
for item in length_dict:
    try:
       
        current_word = T.decode([item])
        current_lang = detect(current_word)
        current_langs = detect_langs(current_word)
        print(current_lang)
        if current_langs[0].prob < 0.5:
            continue
        if current_lang == "en" and Num_engligh <= 100:
            df_english = df_english._append({'Rank': Num_engligh, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_engligh += 1
        elif current_lang == "zh-cn" and Num_simplechinese <= 100:
            df_simplechinese = df_simplechinese._append({'Rank': Num_simplechinese, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_simplechinese += 1
        elif current_lang == "zh-tw" and Num_traditionchinese <= 100:
            df_traditionchinese = df_traditionchinese._append({'Rank': Num_traditionchinese, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_traditionchinese += 1
        elif current_lang == "ja" and Num_japanese <= 100:
            df_japanese = df_japanese._append({'Rank': Num_japanese, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_japanese += 1
        elif current_lang == "fr" and Num_french <= 100:
            df_french = df_french._append({'Rank': Num_french, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_french += 1
        elif current_lang == "de" and Num_german <= 100:
            df_german = df_german._append({'Rank': Num_german, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_german += 1
        elif current_lang == "es" and Num_spanish <= 100:
            df_spanish = df_spanish._append({'Rank': Num_spanish, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_spanish += 1
        elif current_lang == "it" and Num_italian <= 100:
            df_italian = df_italian._append({'Rank': Num_italian, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_italian += 1
        elif current_lang == "pt" and Num_portuguese <= 100:
            df_portuguese = df_portuguese._append({'Rank': Num_portuguese, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_portuguese += 1
        elif current_lang == "ko" and Num_korean <= 100:
            df_korean = df_korean._append({'Rank': Num_korean, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_korean += 1
        elif current_lang == "ru" and Num_russian <= 100:
            df_russian = df_russian._append({'Rank': Num_russian, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_russian += 1
<<<<<<< HEAD
    except:
        pass
    if Num_engligh > 100 and Num_simplechinese > 100 and Num_traditionchinese > 100 and Num_japanese > 100 and Num_french > 100 and Num_german > 100 and Num_spanish > 100 and Num_italian > 100 and Num_portuguese > 100 and Num_korean > 100 and Num_russian > 100:
=======
        elif current_lang == "tr" and Num_turkish <= 100:
            df_turkish = df_turkish._append({'Rank': Num_turkish, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score':current_langs[0].prob}, ignore_index=True);
            Num_turkish += 1
    except:
        pass
    if Num_engligh > 100 and Num_simplechinese > 100 and Num_traditionchinese > 100 and Num_japanese > 100 and Num_french > 100 and Num_german > 100 and Num_spanish > 100 and Num_italian > 100 and Num_portuguese > 100 and Num_korean > 100 and Num_russian > 100 and Num_turkish > 100:
>>>>>>> 86d5be4 (second commit, add Turkish)
        break
  

print(df_english)
print(df_simplechinese)
print(df_traditionchinese)
print(df_japanese)
print(df_french)
print(df_german)
print(df_spanish)
print(df_italian)
print(df_portuguese)
print(df_korean)
print(df_russian)
<<<<<<< HEAD
=======
print(df_turkish)
>>>>>>> 86d5be4 (second commit, add Turkish)



# Save the dataframes to csv files
root = os.path.dirname(os.path.abspath(__file__))
print("current code root path is ***************************"+root)
path = os.path.join(root, 'data/')
df_english.to_csv(path+'df_english.csv', index=False)
df_simplechinese.to_csv(path+'df_simplechinese.csv', index=False)
df_traditionchinese.to_csv(path+'df_traditionchinese.csv', index=False)
df_japanese.to_csv(path+'df_japanese.csv', index=False)
df_french.to_csv(path+'df_french.csv', index=False)
df_german.to_csv(path+'df_german.csv', index=False)
df_spanish.to_csv(path+'df_spanish.csv', index=False)
df_italian.to_csv(path+'df_italian.csv', index=False)
df_portuguese.to_csv(path+'df_portuguese.csv', index=False)
df_korean.to_csv(path+'df_korean.csv', index=False)
<<<<<<< HEAD
df_russian.to_csv(path+'df_russian.csv', index=False)
=======
df_russian.to_csv(path+'df_russian.csv', index=False)
df_turkish.to_csv(path+'df_turkish.csv', index=False)
>>>>>>> 86d5be4 (second commit, add Turkish)
