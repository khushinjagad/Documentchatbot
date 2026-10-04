import streamlit as st # type: ignore
from pypdf import PdfReader # type: ignore

from embeddings import create_embeddings
from vector_store import create_vector_store
from chatbot import generate_answer


# -----------------------------------------
# TEXT CHUNKING
# -----------------------------------------

def split_text(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# -----------------------------------------
# PAGE TITLE
# -----------------------------------------

st.title("📚 Document Q&A Chatbot")

st.write(
    "Upload a PDF and ask questions about its content!"
)


# -----------------------------------------
# PDF UPLOAD
# -----------------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload your PDF",
    type=["pdf"]
)


if uploaded_file:

    st.success("PDF uploaded successfully! ✅")


    # -----------------------------------------
    # READ PDF
    # -----------------------------------------

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text


    # -----------------------------------------
    # SPLIT TEXT
    # -----------------------------------------

    chunks = split_text(text)

    st.write(
        f"📊 Document contains {len(chunks)} chunks."
    )


    # -----------------------------------------
    # CREATE EMBEDDINGS
    # -----------------------------------------

    with st.spinner("🧠 Creating embeddings..."):

        embeddings = create_embeddings(chunks)


    # -----------------------------------------
    # CREATE FAISS INDEX
    # -----------------------------------------

    index = create_vector_store(embeddings)


    st.success("Document is ready for questions! 🔎")


    # -----------------------------------------
    # QUESTION INPUT
    # -----------------------------------------

    question = st.text_input(
        "💬 Ask a question about your document:"
    )


    # -----------------------------------------
    # ASK BUTTON
    # -----------------------------------------

    if st.button("🤖 Ask"):

        if question:


            # -----------------------------------------
            # CREATE QUESTION EMBEDDING
            # -----------------------------------------

            question_embedding = create_embeddings(
                [question]
            )


            # -----------------------------------------
            # SEARCH FAISS
            # -----------------------------------------

            distances, indices = index.search(
                question_embedding.astype("float32"),
                3
            )


            # -----------------------------------------
            # GET RELEVANT CHUNKS
            # -----------------------------------------

            relevant_chunks = []

            for i in indices[0]:

                relevant_chunks.append(
                    chunks[i]
                )


            # -----------------------------------------
            # COMBINE CONTEXT
            # -----------------------------------------

            context = "\n\n".join(
                relevant_chunks
            )


            # -----------------------------------------
            # GENERATE ANSWER
            # -----------------------------------------

            with st.spinner(
                "🤖 Generating answer..."
            ):

                answer = generate_answer(
                    question,
                    context
                )


            # -----------------------------------------
            # DISPLAY ANSWER
            # -----------------------------------------

            st.subheader("🤖 Answer")

            st.write(answer)


            # -----------------------------------------
            # SHOW SOURCES
            # -----------------------------------------

            with st.expander(
                "📚 View retrieved document sections"
            ):

                for i, chunk in enumerate(
                    relevant_chunks
                ):

                    st.write(
                        f"**Retrieved section {i + 1}**"
                    )

                    st.write(chunk)

                    st.divider()


        else:

            st.warning(
                "Please enter a question."
            )