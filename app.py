import streamlit as st
import pickle
import pandas as pd

# -------------------------------------------------
# 1. Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="AI Course Recommendation System",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------------------------
# 2. Background & UI Styling
# -------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

    h1, h2, h3, label {
        color: white !important;
    }

    .glass {
        background: rgba(255, 255, 255, 0.10);
        border-radius: 16px;
        padding: 16px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 12px;
    }

    button {
        border-radius: 12px !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# 3. App Header
# -------------------------------------------------
st.title("🎓 AI Course Recommendation System")
st.caption("Content-based course recommendations using Natural Language Processing (NLP)")

# -------------------------------------------------
# 4. Load Models (Cached)
# -------------------------------------------------
@st.cache_resource
def load_models():
    similarity = pickle.load(open("models/similarity.pkl", "rb"))
    courses_df = pickle.load(open("models/courses.pkl", "rb"))
    return similarity, courses_df

try:
    similarity, courses_df = load_models()
except Exception as e:
    st.error(f"Failed to load model files: {e}")
    st.stop()

course_list = courses_df["course_name"].values

# -------------------------------------------------
# 5. Recommendation Logic
# -------------------------------------------------
def recommend(course_name, top_n=6):
    index = courses_df[courses_df["course_name"] == course_name].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []
    for i in distances[1 : top_n + 1]:
        recommendations.append({
            "name": courses_df.iloc[i[0]].course_name,
            "url": courses_df.iloc[i[0]].course_url
        })
    return recommendations

# -------------------------------------------------
# 6. Course Selection (clean wording)
# -------------------------------------------------
selected_course = st.selectbox(
    "Select a course:",
    course_list,
    index=None,
    placeholder="Choose a course"
)

# -------------------------------------------------
# 7. Course Card UI
# -------------------------------------------------
def course_card(name, url):
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown(f"### {name}")
    st.link_button("📘 View Course", url, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# 8. Display Recommendations
# -------------------------------------------------
if selected_course:
    with st.spinner("Finding similar courses..."):
        results = recommend(selected_course)

    st.subheader("Recommended Courses")

    for item in results:
        course_card(item["name"], item["url"])
else:
    st.info("👆 Select a course to view recommendations")
