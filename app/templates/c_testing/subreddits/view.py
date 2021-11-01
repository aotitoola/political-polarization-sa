import sys
sys.path.append("..")

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


def show(inputs):

    st.header('Type a sample comment in text box.')
    comments = st.text_input('Movie title', 'Life of Brian')

    st.write("## Model")
    model = st.selectbox("Which model?", list(MODELS.keys()))

    # Show model variants if model has multiple ones.
    if isinstance(MODELS[model], dict):
        # different model variants
        model_variant = st.selectbox("Which variant?", list(MODELS[model].keys()))
        inputs["model"] = model.lower()
        inputs["model_func"] = MODELS[model][model_variant]
        print('inputs["model_func"]', inputs["model_func"])
    else:
        # only one variant
        inputs["model"] = MODELS[model]
        inputs["model_func"] = MODELS[model]

    inputs["pretrained"] = st.checkbox("Use pre-trained model")

    if inputs["pretrained"]:
        pass

    st.write("## Preprocessing")

    st.write("## Testing")

    inputs["checkpoint"] = st.checkbox("Save model checkpoint each epoch")
    if inputs["checkpoint"]:
        st.markdown(
            "<sup>Checkpoints are saved to timestamped dir in `./checkpoints`. They may consume a lot of storage!</sup>",
            unsafe_allow_html=True,
        )

    default_lr = 3e-4
    inputs["lr"] = st.number_input(
        "Learning rate", 0.000, None, default_lr, format="%f"
    )
    inputs["batch_size"] = st.number_input("Batch size", 1, None, 128)
    inputs["num_epochs"] = st.number_input("Epochs", 1, None, 3)
    inputs["print_every"] = st.number_input(
        "Print progress every ... batches", 1, None, 1
    )


if __name__ == "__main__":
    show()
