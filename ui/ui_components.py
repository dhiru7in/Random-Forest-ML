import streamlit as st


def show_prediction_result(prediction):

    category = prediction["predicted_category"]
    confidence = prediction["confidence"]
    probabilities = prediction["class_probabilities"]

    # Choose color
    if category == "High":
        category_color = "#ef4444"   # Red
    elif category == "Medium":
        category_color = "#f59e0b"   # Orange
    else:
        category_color = "#22c55e"   # Green

    # Prediction card
    st.markdown(
        f"""
        <div style="padding:30px; border-radius:15px; background-color:#1e293b; text-align:center; margin-bottom:20px;">
            <p style="font-size:18px; color:#cbd5e1; margin-bottom:5px;">
                Predicted Insurance Premium Category
            </p>
            <h1 style="color:{category_color}; font-size:45px; margin:0;">
                {category}
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Premium Category",category)
    with col2:
        st.metric("Model Confidence",f"{confidence:.2%}")

    st.divider()

    st.subheader("Class Probabilities")

    for class_name, probability in probabilities.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(f"**{class_name}**")
        with col2:
            st.progress(float(probability))
        st.caption(f"{probability:.2%}")