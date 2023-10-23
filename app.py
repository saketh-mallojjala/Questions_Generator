import streamlit as st
from sec import extract_text_from_pdf
from Questgen import main
from pprint import pprint
import io

st.title("PDF Text Extraction")
st.write("Upload a PDF file for text extraction:")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
if uploaded_file is not None:
    if st.button("Extract Text"):
        file_contents = uploaded_file.read()
    # Convert bytes to a string
        file_contents_str = file_contents.decode('utf-16')
        text = extract_text_from_pdf(file_contents_str)

        st.subheader("Extracted Text:")
        st.write(text)

        # Add a button to download the extracted text as a text file
        download_button = st.button("Download Text File")

        if download_button:
            text_io = io.StringIO(text)
            st.write("### Download the extracted text as a text file")
            st.download_button(
                label="Click to Download",
                data=text_io,
                key="extracted_text_file.txt",
                on_click=None,
                args=None,
                help="Click to download the extracted text as a text file."
            )

        generate_button = st.button("Generate Boolean Questions")
        text1 = ''
        if generate_button:
            text = ' '.join(text.split())
            payload = {
                "input_text": text
            }
            qe = main.BoolQGen()
            output1 = qe.predict_boolq(payload)

            text1 = str(output1['Boolean Questions'])
            st.write(text1)

        download_button1 = st.button("Download Boolean Questions File")

        if download_button1:
            text_io = io.StringIO(text1)
            st.write("### Download the Boolean Questions as a text file")
            st.download_button(
                label="Click to Download",
                data=text_io,
                # key="Boolean_Questions_file.txt",
                on_click=None,
                args=None,
                help="Click to download the Boolean_Questions as a text file."
            )

        generate_button = st.button("Generate MCQ Questions")
        text2 = ''
        if generate_button:
            text = ' '.join(text.split())
            payload = {
                "input_text": text
            }
            qg = main.QGen()
            output2 = qg.predict_mcq(payload)

            text2 = output2['questions']
            st.write(text2)

        download_button1 = st.button("Download MCQ Questions File")

        if download_button1:
            text_io = io.StringIO(text2)
            st.write("### Download the MCQ Questions as a text file")
            st.download_button(
                label="Click to Download",
                data=text_io,
                key="MCQ_Questions_file.txt",
                on_click=None,
                args=None,
                help="Click to download the MCQ_Questions as a text file."
            )

        generate_button = st.button("Generate One Word Answer Questions")
        text3 = ''
        if generate_button:
            text = ' '.join(text.split())
            payload = {
                "input_text": text
            }
            qg = main.QGen()
            output3 = qg.predict_shortq(payload)

            text3 = output3['questions']
            st.write(text3)

        download_button1 = st.button("Download Ome Word Answer Questions File")

        if download_button1:
            text_io = io.StringIO(text3)
            st.write("### Download the One Word Answer Questions as a text file")
            st.download_button(
                label="Click to Download",
                data=text_io,
                key="One_Word_Answer_Questions_file.txt",
                on_click=None,
                args=None,
                help="Click to download the One_Word_Answer_Questions as a text file."
            )
