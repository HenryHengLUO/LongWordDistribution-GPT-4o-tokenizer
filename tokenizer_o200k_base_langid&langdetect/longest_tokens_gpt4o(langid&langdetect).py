import tiktoken
import os
import sys
root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(root, 'langidfile')
sys.path.append(path)
import langid
from langid.langid import LanguageIdentifier, model
from langdetect import detect
from langdetect import detect_langs
import pandas as pd

# Load the language identifier model
identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)


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
df_english = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])
df_chinese = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])
df_japanese = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])
df_french = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])
df_german = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])
df_spanish = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])
df_italian = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])
df_portuguese = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])
df_korean = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])
df_russsian = pd.DataFrame(columns=['Rank', 'Encoding', 'Word Length', 'Word', 'Language Score_langdetect', 'Language Score_langid'])



# Print the top 100 long words for each language
Num_engligh = Num_chinese = Num_japanese = Num_french = Num_german = Num_spanish = Num_italian = Num_portuguese = Num_korean = Num_russsian = 1

for item in length_dict:
    try:
        current_word = T.decode([item])
        current_lang_class_langid = identifier.classify(current_word)
        current_lang_langid = current_lang_class_langid[0]
        print(current_lang_langid + " **detect by langid @" + str(item))
        if current_lang_class_langid[1] < 0.5:
            continue

        current_lang_langdetect = detect(current_word)
        current_langs_langdetect = detect_langs(current_word)
        print(current_lang_langdetect + " **detect by langdetect @" + str(item))
        if current_langs_langdetect[0].prob < 0.5:
            continue

        if current_lang_langdetect == "zh-cn" or current_lang_langdetect == "zh-tw":
            current_lang_langdetect = "zh"

        if current_lang_langid != current_lang_langdetect:
            continue
        else:
            current_lang = current_lang_langid

        if current_lang == "en" and Num_engligh <= 100:
            print("********************************************")
            df_english = df_english._append({'Rank': Num_engligh, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_engligh += 1
            print("Current English word is: "+current_word+"  "+str(Num_engligh)+"\n")
        elif current_lang == "zh" and Num_chinese <= 100:
            df_chinese = df_chinese._append({'Rank': Num_chinese, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_chinese += 1
        elif current_lang == "ja" and Num_japanese <= 100:
            df_japanese = df_japanese._append({'Rank': Num_japanese, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_japanese += 1
        elif current_lang == "fr" and Num_french <= 100:
            df_french = df_french._append({'Rank': Num_french, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word,'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_french += 1
        elif current_lang == "de" and Num_german <= 100:
            df_german = df_german._append({'Rank': Num_german, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_german += 1
        elif current_lang == "es" and Num_spanish <= 100:
            df_spanish = df_spanish._append({'Rank': Num_spanish, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_spanish += 1
        elif current_lang == "it" and Num_italian <= 100:
            df_italian = df_italian._append({'Rank': Num_italian, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_italian += 1
        elif current_lang == "pt" and Num_portuguese <= 100:
            df_portuguese = df_portuguese._append({'Rank': Num_portuguese, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_portuguese += 1
        elif current_lang == "ko" and Num_korean <= 100:
            df_korean = df_korean._append({'Rank': Num_korean, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_korean += 1
        elif current_lang == "ru" and Num_russsian <= 100:
            df_russsian = df_russsian._append({'Rank': Num_russsian, 'Encoding': item, 'Word Length': length_dict[item], 'Word': current_word, 'Language Score_langdetect':current_langs_langdetect[0].prob, 'Language Score_langid':current_lang_class_langid[1]}, ignore_index=True);
            Num_russsian += 1  
    except:
        pass
    if Num_engligh > 100 and Num_chinese > 100 and Num_japanese > 100 and Num_french > 100 and Num_german > 100 and Num_spanish > 100 and Num_italian > 100 and Num_portuguese > 100 and Num_korean > 100:
        break


print(df_english)
print(df_chinese)
print(df_japanese)
print(df_french)
print(df_german)
print(df_spanish)
print(df_italian)
print(df_portuguese)
print(df_korean)
print(df_russsian)



# Save the dataframes to csv files
root = os.path.dirname(os.path.abspath(__file__))
print("current code root path is ***************************"+root)
path = os.path.join(root, 'data/')
df_english.to_csv(path+'df_english.csv', index=False)
df_chinese.to_csv(path+'df_chinese.csv', index=False)
df_japanese.to_csv(path+'df_japanese.csv', index=False)
df_french.to_csv(path+'df_french.csv', index=False)
df_german.to_csv(path+'df_german.csv', index=False)
df_spanish.to_csv(path+'df_spanish.csv', index=False)
df_italian.to_csv(path+'df_italian.csv', index=False)
df_portuguese.to_csv(path+'df_portuguese.csv', index=False)
df_korean.to_csv(path+'df_korean.csv', index=False)
df_russsian.to_csv(path+'df_russsian.csv', index=False)