import streamlit as st
from graph import app
from career_agent import career_app

st.set_page_config(page_title="Cortex AI", page_icon="🧠", layout="wide")

st.title("🧠 Cortex AI")
st.subheader("Your AI-Powered Career & Research Intelligence System")

mode = st.selectbox("What do you want to do?", [
    "🎯 Career Intelligence — Get my personalized roadmap",
    "🎤 Interview Prep — Prepare for a specific company",
    "🔍 Research Assistant — Deep research on any topic"
])

st.divider()

if "Career Intelligence" in mode:
    st.subheader("🎯 Career Intelligence")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        current_skills = st.text_area("Your current skills", 
            placeholder="e.g. Python, Pandas, basic ML, SQL")
    with col2:
        dream_role = st.text_input("Your dream role", 
            placeholder="e.g. AI/ML Engineer at a startup")
    with col3:
        timeline = st.text_input("Your timeline", 
            placeholder="e.g. 4 weeks, 3 months")
    
    if st.button("Generate My Roadmap 🚀"):
        if current_skills and dream_role and timeline:
            with st.spinner("🔍 Searching job market... analyzing your skills... building your roadmap..."):
                result = career_app.invoke({
                    "current_skills": current_skills,
                    "dream_role": dream_role,
                    "timeline": timeline,
                    "search_results": "",
                    "skill_gaps": "",
                    "roadmap": ""
                })
            
            st.subheader("📊 Skill Gap Analysis")
            st.markdown(result["skill_gaps"])
            
            st.divider()
            
            st.subheader("🗺️ Your Personalized Roadmap")
            st.markdown(result["roadmap"])
        else:
            st.warning("Please fill in all three fields.")

elif "Interview Prep" in mode:
    st.subheader("🎤 Interview Prep")
    
    col1, col2 = st.columns(2)
    
    with col1:
        company = st.text_input("Company Name", placeholder="e.g. Amazon, Goldman Sachs")
    with col2:
        role = st.text_input("Role", placeholder="e.g. SDE, Data Analyst, AI Engineer")
    
    if st.button("Prepare Me! 🎯"):
        if company and role:
            with st.spinner(f"Researching {company} {role} interview..."):
                from career_agent import interview_prep
                result = interview_prep(company, role)
            st.markdown(result["interview_prep"])
            
            st.download_button(
                label="📥 Download Interview Prep",
                data=result["interview_prep"],
                file_name=f"{company}_{role}_prep.txt",
                mime="text/plain"
            )
        else:
            st.warning("Please enter both company and role.")

else:
    st.subheader("🔍 Research Assistant")
    
    question = st.text_input("Enter your research question:")
    
    if st.button("Research 🔍"):
        if question:
            with st.spinner("🔍 Searching..."):
                result = app.invoke({"question": question})
            st.markdown(result["answer"])
        else:
            st.warning("Please enter a question.")
            