import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain import LLMChain
from langchain_groq import ChatGroq
import streamlit as st

# Initialize the Groq Llama Versatile model
llm = ChatGroq(model="mixtral-8x7b-32768")

examples = [
    {
        "query": "Good Morning",
        "output": """Ohayou gozaimasu. (おはようございます) 
                      \nOhayou (おはよう) is a casual way to say good morning among friends and family.  
                      \nAdding gozaimasu (ございます) makes it more polite and formal, suitable for use in professional or respectful settings.""" 
    },
    {
        "query": "My name is Jacob",
        "output": """Watashi no namae wa Jeikobu desu.(わたしのなまえはじぇいこぶです)  
                      \nWatashi no namae (わたしのなまえ)  means my name. 
                      \nwa (は) is the topic particle.  
                      \nJeikobu (じぇいこぶ) is Jacob in hiragana.  
                      \ndesu (です) is a polite sentence-ending particle."""
    },
    {
        "query": "How are you",
        "output": """Ogenki desu ka? (おげんきですか)  
                      \nOgenki (おげんき) means well-being or health. 
                      \ndesu (です)  is a polite form of is.  
                      \nka (か) is a question particle"""
    },
    {
        "query": "I am learning Japanese because I love anime.",
        "output": """Watashi wa nihongo o benkyou shiteimasu, anime ga daisuki dakara desu. (わたしはにほんごをべんきょうしています、アニメがだいすきだからです)  
                      \nWatashi wa (わたしは) means "I" with the topic particle wa (は).  
                      \nNihongo (にほんご) means Japanese language.  
                      \nO (を) is the object particle.  
                      \nBenkyou shiteimasu (べんきょうしています) means "am learning."  
                      \nAnime (アニメ) refers to Japanese animation.  
                      \nGa (が) is the subject particle.  
                      \nDaisuki (だいすき) means "love a lot."  
                      \nDakara desu (だからです) translates to "because it is," indicating the reason."""
    },
      {
    "query": "I am learning Japanese because I love anime.",
    "output": """Watashi wa nihongo o benkyou shiteimasu, anime ga daisuki dakara desu. (わたしはにほんごをべんきょうしています、アニメがだいすきだからです)  
                  \nWatashi wa (わたしは) means "I" with the topic particle wa (は).  
                  \nNihongo (にほんご) means Japanese language.  
                  \nO (を) is the object particle.  
                  \nBenkyou shiteimasu (べんきょうしています) means "am learning."  
                  \nAnime (アニメ) refers to Japanese animation.  
                  \nGa (が) is the subject particle.  
                  \nDaisuki (だいすき) means "love a lot."  
                  \nDakara desu (だからです) translates to "because it is," indicating the reason."""
   },
   {
    "query": "Can you recommend a good Japanese restaurant near me?",
    "output": """Watashi no chikaku ni aru osusume no nihon-ryouri no resutoran wa arimasu ka? (わたしのちかくにあるおすすめのにほんりょうりのレストランはありますか)  
                  \nWatashi no (わたしの) means "my."  
                  \nChikaku (ちかく) refers to "nearby" or "close to me."  
                  \nAru (ある) means "to exist" (for non-living things).  
                  \nOsusume (おすすめ) means "recommendation."  
                  \nNihon-ryouri (にほんりょうり) means "Japanese cuisine."  
                  \nResutoran (レストラン) is the Japanese word for "restaurant."  
                  \nWa (は) and ka (か) denote the topic and question, respectively."""
    },
    {
    "query": "I want to travel to Japan next year and visit Kyoto.",
    "output": """Watashi wa rainen Nihon e ryokou shite, Kyoto o otozuretai desu. (わたしはらいねんにほんへりょこうして、きょうとをおとずれたいです)  
                  \nWatashi wa (わたしは) introduces the topic as "I."  
                  \nRainen (らいねん) means "next year."  
                  \nNihon e (にほんへ) indicates movement "to Japan."  
                  \nRyokou shite (りょこうして) means "traveling."  
                  \nKyoto (きょうと) is the city name, Kyoto.  
                  \nO (を) is the object particle.  
                  \nOtozuretai (おとずれたい) means "want to visit."  
                  \nDesu (です) adds politeness."""
    },
    {
    "query": "What is the difference between hiragana, katakana, and kanji?",
    "output": """Hiragana to katakana to kanji no chigai wa nan desu ka? (ひらがなとかたかなと漢字のちがいはなんですか)  
                  \nHiragana (ひらがな) is one of the Japanese phonetic alphabets used for native words.  
                  \nKatakana (かたかな) is another phonetic alphabet, mainly used for foreign words and loanwords.  
                  \nKanji (漢字) are logographic characters borrowed from Chinese, representing entire words or concepts.  
                  \nTo (と) connects multiple items.  
                  \nChigai (ちがい) means "difference."  
                  \nWa (は) marks the topic of the sentence.  
                  \nNan desu ka (なんですか) means "what is it?" indicating a question."""
    }
]


example_template = """
User : {query}
Output : {output}
"""

prompt_template = PromptTemplate(
    template=example_template,
    input_variables=["query", "output"]
)

prefix = """
The following are translations of English phrases to Japanese, along with their meanings. Each response must follow this structure:
1. Provide the Japanese phrase.
2. Make sure to break down the Japanese sentence into its each components and explain their meanings only.

Here are some examples:
"""

suffix = """
User : {query}
Output : """  # Ensure the model knows where to generate the output

few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_template,
    prefix=prefix,
    suffix=suffix, 
    input_variables=["query"],
    example_separator="\n\n"
)

# Streamlit framework
st.title("Learn Nihongo (Japanese)")
st.subheader("Learn to speak Japanese")
input_text = st.text_input("Let's go! Type your word")

if input_text:
    chain = LLMChain(llm=llm, prompt=few_shot_prompt_template)
    result = chain.run({"query": input_text})

    st.write(result)