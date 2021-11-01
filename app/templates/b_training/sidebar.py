import streamlit as st


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

LR_SOLVERS = ['lbfgs', 'liblinear', 'newton-cg', 'sag', 'saga']


def show():
    """Shows the sidebar components for the template and returns user inputs as dict."""

    inputs = {'task': 'training'}

    with st.sidebar:
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

        inputs["pretrained"] = st.checkbox("Use pre-trained model", value=True)

        if not inputs["pretrained"]:

            if inputs["model"] == 'tfidf':

                if inputs["model_func"] == 'logistic_regression':
                    inputs['max_iter'] = st.slider('Max. Iteration', min_value=200, value=400, max_value=600)
                    inputs['solver'] = st.selectbox("Which solver?", list(LR_SOLVERS))

                if inputs["model_func"] == 'random_forest':
                    inputs['max_iter'] = st.number_input(label='Maximum Depth', min_value=6, value=8, max_value=20)

    return inputs


if __name__ == "__main__":
    show()
