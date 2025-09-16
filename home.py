import streamlit as st

def classify_abstract(abstract):
    """
    Classifies an abstract into a study design based on keywords.
    """
    abstract_lower = abstract.lower()
    
    # Define keywords for each study design
    keywords = {
        "Randomized Controlled Trial (RCT)": ["randomized", "randomised", "control group", "placebo", "double-blind"],
        "Non-randomized Trial": ["non-randomized", "quasi-experimental", "pre-post intervention"],
        "Cohort Study": ["cohort", "follow-up", "prospective", "longitudinal", "retrospective cohort"],
        "Case–Control Study": ["case-control", "cases", "controls", "retrospective"],
        "Cross-Sectional Study": ["cross-sectional", "prevalence", "one-time", "snapshot"],
        "Systematic Review / Meta-analysis": ["systematic review", "meta-analysis", "review of the literature"],
        "Case Report / Case Series": ["case report", "case series", "a patient with", "a series of patients"],
        "In vitro Study": ["in vitro", "cell culture", "laboratory", "cell line"],
        "In vivo (animal) Study": ["in vivo", "animal model", "mice", "rats", "animal study"],
        "Computational / AI Model Study": ["computational model", "ai model", "machine learning", "algorithm", "deep learning"],
        "Other (specify)": []
    }

    # Iterate through keywords and find a match
    for design, key_list in keywords.items():
        if any(key in abstract_lower for key in key_list):
            return design
    
    # If no specific keywords are found, return "Other"
    return "Other (specify)"

# --- Streamlit App Layout ---

st.set_page_config(page_title="Study Design Classifier", layout="centered")
st.title("🔬 Study Design Classifier")
st.markdown("Enter an abstract below, and I'll classify its study design.")
st.divider()

# Text input area for the abstract
abstract_text = st.text_area("Paste Abstract Here:", height=200, help="The abstract will be analyzed for keywords to determine the study design.")

# Classification button
if st.button("Classify Study Design", type="primary"):
    if abstract_text:
        # Perform classification
        classification = classify_abstract(abstract_text)
        
        # Display the result
        st.divider()
        st.subheader("Classification Result")
        st.info(f"The study design is likely: **{classification}**")
        st.markdown("---")
        st.markdown("**Explanation of the Classification:**")
        
        # Provide a simple rationale
        if classification == "Cohort Study":
            st.write(f"The abstract contains the keyword(s) **'cohort'**, which is characteristic of a **Cohort Study** where a group of people is followed over time to observe outcomes.")
        else:
            st.write("This classification is based on identifying specific keywords within the abstract that are commonly associated with a particular study design. The current model is a basic keyword-based classifier and may not be as accurate as a more advanced machine learning model.")
    else:
        st.warning("Please paste an abstract to classify.")
