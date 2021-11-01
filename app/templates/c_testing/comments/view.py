import sys
sys.path.append("..")

import streamlit as st
from reddit_analysis.app.templates.c_testing.comments.algo import tfidf, lstm


# Define possible models in a dict.
# Format of the dict:
# option 1: model -> code
# option 2 – if model has multiple variants: model -> model variant -> code
MODELS = {
    # multiple model variants
    "Tfidf": {
        "Logistic Regression": "logistic_regression",
        "Random Forest": "random_forest"
    },
    # single model variant
    "LSTM": "lstm",
    "BERT": "bert",
    "ALBERT": "albert",
}


def show(inputs):

    st.header('Text to analyze.')
    text_to_analyze = st.text_area('Type a sample comment below.')

    # st.write("## Model")
    # model = st.selectbox("Which model?", list(MODELS.keys()))
    #
    # # Show model variants if model has multiple ones.
    # if isinstance(MODELS[model], dict):
    #     # different model variants
    #     model_variant = st.selectbox("Which variant?", list(MODELS[model].keys()))
    #     inputs["model"] = model.lower()
    #     inputs["model_func"] = MODELS[model][model_variant]
    #     print('inputs["model_func"]', inputs["model_func"])
    # else:
    #     # only one variant
    #     inputs["model"] = MODELS[model]
    #     inputs["model_func"] = MODELS[model]
    #
    # st.write("### Preprocessing...")

    if st.button('Run Analysis'):
        st.markdown("<br>", unsafe_allow_html=True)
        # show template-specific components (based on selected model).
        if inputs['model'] == 'tfidf':
            tfidf.show(inputs, text_to_analyze)

        if inputs['model'] == 'lstm':
            lstm.show()


if __name__ == "__main__":
    show()