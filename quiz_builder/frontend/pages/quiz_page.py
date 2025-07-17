import streamlit as st

st.set_page_config(page_title="Take Your Quiz")

if "quiz_data" not in st.session_state:
    st.error("🚫 No quiz loaded. Go to home page.")
    st.stop()

st.title("📋 Your Quiz")


if "answers" not in st.session_state:
    st.session_state.answers = {}

for idx, item in enumerate(st.session_state.quiz_data):
    selected_option = st.radio(
        f"Q{idx+1}: {item['question']}",
        item['options'],
        index=None,
        key=f"q_{idx}"
    )
    st.session_state.answers[f"q_{idx}"] = item['options'].index(selected_option) if selected_option else None

if st.button("Submit"):
    correct = 0
    total = len(st.session_state.quiz_data)

    st.subheader("📝 Results")
    for idx, item in enumerate(st.session_state.quiz_data):
        selected = st.session_state.answers.get(f"q_{idx}")
        correct_index = item["answer"]
        if selected == correct_index:
            st.success(f"Q{idx+1}: Correct ✅")
            correct += 1
        elif selected is None:
            st.warning(f"Q{idx+1}: No answer selected ⚠️")
        else:
            st.error(f"Q{idx+1}: Incorrect ❌ (Correct: Option {correct_index + 1})")
    st.markdown(f"### 🎯 Your Score: **{correct} / {total}**")
