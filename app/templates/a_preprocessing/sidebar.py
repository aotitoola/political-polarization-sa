# don't delete, needed by the application to work
import sys
sys.path.append("..")
import streamlit as st


def show():
    """Shows the sidebar components for the template and returns user inputs as dict."""

    inputs = {'task': 'preprocessing', 'visualize': False}

    with st.sidebar:

        st.write("## Input data")
        st.write("### Left Wing")
        inputs["left_wing_subreddits"] = st.multiselect('Select left wing subreddit', key='left_wing_subreddits',
                                                        options=['/r/liberal', '/r/others'],
                                                        default=['/r/liberal'])

        st.write("### Right Wing")
        inputs["right_wing_subreddits"] = st.multiselect('Select right wing subreddit',  key='right_wing_subreddits',
                                                         options=['/r/conservative', '/r/others'],
                                                         default=['/r/conservative'])

        st.markdown("<br>", unsafe_allow_html=True)
        inputs['visualize'] = st.button('Preprocess Data & Visualize')
        st.markdown("<br>", unsafe_allow_html=True)

    return inputs


if __name__ == "__main__":
    show()

