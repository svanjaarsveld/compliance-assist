import streamlit as st


def main():
    st.title("Search Your PDF 🐦📄")
    with st.expander("About the App"):
        st.markdown(
            """
            This is a Generative AI powered Question and Answering app that responds to questions about your PDF File.
            """
        )
    question = st.text_area("Enter your Question")
    if st.button("Ask"):
        st.info("Your Question: " + question)

        st.info("Your Answer")
        
        answer = 'I am not sure?'
        
        st.write(answer)


if __name__ == '__main__':
    main()