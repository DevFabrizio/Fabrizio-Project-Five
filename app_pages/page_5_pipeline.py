import streamlit as st
import joblib


def page_pipeline_body():
    st.title('Regression Pipeline')
    st.write('---')
    st.write("The Machine Learning Pipeline that I developed is comprised of:")
    st.markdown("**- Ordinal Categorical Encoder**\n\n"
                "This transformer was introduced aftera bug that prevented"
                " live data to be effectively predicted by the pipeline. The"
                " issue happened when I realized that I had One Hot Encoded"
                " the train and test dataset in order to run the correlation"
                " studies, since the correlation functions in the Pandas Lib"
                "rary will only accept numerical values in the dataframe."
                " This created a problem with the dataset with the inherited"
                " houses since that also continained categorical values that"
                " needed to be encoded in order to be processed and evaluated"
                " by the model. This is when I realized that the encoding step"
                " was missing in my pipeline. I then proceeded to add it and"
                " was able to continue on with the development of the"
                " pipeline.\n\n"
                "**- Winsorizer**\n\n"
                "This transformer takes care of standardizing the features whi"
                "ch show outliers. In this particular case the capping method "
                "was 'iqr' applied to both tails of the feature values. This w"
                "as a crucial step when modifing the initial transformers of t"
                "he first iteration of the pipeline."
                ".\n\n"
                "**- Feature Scaling**\n\n"
                "This transformer was simply used due to the inconsistency in"
                " the nature of the numerical features in the dataset. The Sca"
                "ler reduced all the various numerical values to a comparable"
                " format so that the algorithm could better learn their relati"
                "onships.\n\n"
                "**- Model**\n\n"
                "After a preliminary search of various regressors and using th"
                "e custom class from the Walkthrough Project, I opted for the"
                " model with the best performance wich you can see by clicking"
                " the button below.\n\n")
    if st.button('ML Model'):
        regression_pipeline = joblib.load(
            'outputs/ml_pipeline/predict_saleprice/v1/regressor_pipeline.pkl'
        )
        st.write(regression_pipeline)
    st.write("As you can see from the pipeline I didn't use the standard hyper"
             "parameters of the model, but instead I conducted a search in ord"
             "er to find the best fit for my model. More accurately I needed t"
             "o satisfy the r2 score of 0.75 on both train and test set. The s"
             "tandard hyperparameters scored below the 0.75 value for r2 and a"
             "fter a hyperparameters tuning I was able to achieve the desired "
             "result. In addition to the regular pipeline development I also d"
             "ecided to try to re-fit the pipeline with the best features foun"
             "d by the pipeline model after the first training run. The result"
             " was the same score so I decided to use the pipeline with less "
             "features. This allowed me to utilize a fewer amount of input wid"
             "gets in the predictive interface on page 3 of this dashboard.")
    st.write('---')
    st.markdown("### Model Performance")
    st.image('outputs/ml_pipeline/predict_saleprice/model_performance.png')
    st.markdown("**Train Set r2 Score** --------------- **Test Set r2"
                " Score**\n\n"
                "0.89 --------------------------------- 0.79\n\n")
    st.write("In the image above we can see the model performance on train and"
             " test set. We notice that with higher prices the accuracy of the"
             " prediction actually decreases. With this information we should "
             "consider being more careful when the model will predict a price "
             "in a higher bracket.")
