import sys
sys.path.append("..")

import streamlit as st
from reddit_analysis.app.util.utils import capitalize

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

# Define possible optimizers in a dict.
# Format: optimizer -> default learning rate
OPTIMIZERS = {
    "Adam": 0.001,
    "Adadelta": 1.0,
    "Adagrad": 0.01,
    "Adamax": 0.002,
    "RMSprop": 0.01,
    "SGD": 0.1,
}


def show():
    """Shows the sidebar components for the template and returns user inputs as dict."""

    inputs = {'task': 'testing'}

    with st.sidebar:

        st.write("## Model")
        testing_mode = st.selectbox("Testing Mode?", list(['comments', 'subreddits']), format_func=capitalize)
        inputs["testing_mode"] = testing_mode

        st.write("## Model")
        model = st.selectbox("Which model?", list(MODELS.keys()))

        # Show model variants if model has multiple ones.
        if isinstance(MODELS[model], dict):
            # different model variants
            model_variant = st.selectbox("Which variant?", list(MODELS[model].keys()))
            inputs["model"] = model.lower()
            inputs["model_func"] = MODELS[model][model_variant]
        else:
            # only one variant
            inputs["model"] = MODELS[model]
            inputs["model_func"] = MODELS[model]

    return inputs


if __name__ == "__main__":
    show()
