import sys
sys.path.append("..")

from reddit_analysis.app.util.tokenizer import tokenize_df
from reddit_analysis.app.util.pipeline import get_data, rebalance_data, display_dataframe

import streamlit as st

# Import Scikit-learn modules
from sklearn import model_selection

# Data Science modules
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
plt.style.use('ggplot')


def show():

    # LOAD INPUT DATA
    data_load_state = st.info('Loading data...')
    raw_train_data, train_df = get_data()
    data_load_state.info('Data Loaded!')

    # display data
    display_dataframe(raw_train_data, 6)

    # rebalanced
    train_df = rebalance_data(train_df)

    # Display the distribution graph
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(17, 5))
    sns.countplot(x='label', data=train_df, ax=ax1)
    ax1.set_title('The number of data for each label', fontsize=14)
    sns.histplot([len(x) for x in train_df['body']], kde=True, stat="density", ax=ax2, bins=60)

    ax2.set_title('The number of letters in each data', fontsize=14)
    ax2.set_xlim(0, 1500)
    ax2.set_xlabel('number of letters')
    ax2.set_ylabel("")
    sns.histplot(train_df['count'], kde=True, stat="density", ax=ax3, bins=60)

    ax3.set_title('The number of words in each data', fontsize=14)
    ax3.set_xlim(0, 250)
    ax3.set_xlabel('number of words')
    ax3.set_ylabel("")

    st.subheader('Distribution Graph')
    st.markdown("<br>", unsafe_allow_html=True)
    st.pyplot(fig)

    with st.spinner(text='Tokenization in progress...'):
        tokenized, tokenized_text, bow, vocab, id2vocab, token_ids = tokenize_df(train_df, col='body',
                                                                                 lemma=True, use_stopwords=True,
                                                                                 tokenizer='NLTK', show_graph=True)

    # reset index
    train_df.reset_index(drop=True, inplace=True)

    # X and Y data used
    X_data = tokenized_text
    Y_data = train_df['label']

    # Train test split (Shuffle=False will make the test data for the most recent ones)
    X_train, X_test, Y_train, Y_test = \
        model_selection.train_test_split(X_data, Y_data.values, test_size=0.2, shuffle=True)

    st.markdown("<br>", unsafe_allow_html=True)
    return X_train, X_test, Y_train, Y_test
