import streamlit as st


def page_hypothesis_body():
    st.title('Project Hypothesis')
    st.write('---')
    st.write("In this page we will explore our initial hypothesis regarding"
             " our project expectations. We'll also highlight the findings"
             " of the research we conducted.")
    st.write('---')
    st.write('After a first evaluation of the dataset I went over the'
             " features which comprised our source. I immediately noticed the"
             " presence of the 'Overall Quality' feature. Obviously I realized"
             " that this could have been one of the most prominant feature"
             " capable of determining the target variable which is"
             " 'Sale Price. In addition to that is fairly common in a real"
             " estate context to pair in a positevely correlated manner the"
             " total amount of square feet of a property to its worth. This"
             " line of reasoning was also supported by the amount of variables"
             " in the dataset which referenced square feet as a metric. So to"
             " summarize our initial hypothesis was:")
    st.markdown("* The feature 'Overall Quality' was predictive of"
                " 'Sale Price'\n"
                "* The features which tracked the square feet were predictive"
                " of 'Sale Price'\n"
                "* The presence of 'Wood Deck' was predictive of"
                " 'Sale Price'\n"
                "* The presence of 'Open Porch' was predictive of"
                " 'Sale Price'")
    st.write('---')
    st.write("Now let's take a look at which features were recognized by the"
             " machine learning model to be the best predictors of"
             " 'Sale Price'")
    st.image(
        'outputs/ml_pipeline/predict_saleprice/v1/features_importance.png')
    st.markdown("**In this plot the features are:**")
    st.write("- Total Basement Square Feet\n"
             "- Square ft. of above ground living area\n"
             "- Kitchen Quality\n"
             "- Year of remodelling")
    st.subheader("Comparisons and Conclusions")
    st.write("From the plot we can see that the model didn't recognize the"
             " feature 'Overall Quality' as a strong predictor of"
             " 'Sale Price'. However we have two features which track a"
             " square feet value, In particular the 'Total basement square"
             " feet' and 'Square Feet of living area above ground'. It is safe"
             " to say that 'Kitchen Quality' should have been expected to be"
             " a determining factor in our initial anylysis. On the same note"
             " the same can be said for the 'Year of remodelling' feature."
             " In conclusion we can safely assume that our initial hypothesis"
             " was only partially correct and that the model showed us some"
             " features that were overall better predictors of the target"
             " value of 'Sale Price'.")
