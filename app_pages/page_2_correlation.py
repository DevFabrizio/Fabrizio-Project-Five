import streamlit as st
import pandas as pd

# This function contains the content of the page. It will be called in the
# app.py file


def page_correlation_body():
    st.title('Correlation Study')
    st.info("This page will illustrate the correlation study and the most"
            " significant variables correlated with the Sale Price.")
    st.markdown("### What is a correlation?")
    st.write("A correlation happens when for a given value change another"
             "value changes as well. Correlation can be positive which means"
             " that when one value increases the other increases as well, or"
             " it can be negative, which means that if a given value increases"
             " the other value descreases. The correlation levels are"
             " described"
             " on a continuous value from -1 to 1. When the value is either -1"
             " or 1, then we know the correlation is perfect. Obviously -1"
             " would be a perfect negative correlation while 1 is a perfect"
             " positive. It is important to note that correlation doesn't"
             " mean causation so we should always indulge in more"
             " investigation after drawing some conclusions. Especially from"
             " the correlation of just 1 variable against another.")
    st.markdown("#### Spearman Correlation")
    st.write('---')
    # This segment of code load shows the one hot encoded dataset. (10 samples)
    df_ohe = pd.read_csv(
        'outputs/'
        'dataset/collection/feature_engineered_dataset.csv'
    )
    if st.checkbox('Dataset'):
        st.write('These are 10 rows from the pre-processed dataset')
        st.write(df_ohe.head(10))

    # this section shows the sperman correlation
    st.write('We are going to show correlation with the Spearman method'
             "This is just one of the available methods we have to calculate"
             "correlations between two variables.")
    if st.checkbox('Show correlation'):
        df_ohe_corr_spearman = (df_ohe
                                .corr(method='spearman')['SalePrice']
                                .sort_values(key=abs, ascending=False)[1:]
                                .head(10))
        st.write(df_ohe_corr_spearman)
        st.write("Now that we know our most correlated features we can"
                 "say that:\n\n"

                 "- The price of a house increases with the increase of"
                 " Overall Quality\n"
                 "- The price of a house increases with the increase of Ground"
                 " Living Area (in square feet) when above grade\n"
                 "- The price of a house increases when the year of"
                 " construction is more recent\n"
                 "- The price of a house increases with the increase of"
                 " Garage Area\n"
                 "- The price of a house increases when the Kitchen Quality is"
                 " NOT assesed as Typical/Average\n"
                 "- The price of a house increases when the year of"
                 " construction of the garage is more recent\n"
                 "- The price of a house increases when the basement surface"
                 " (measured in square feet) increases\n"
                 "- The price of a house increases when the year of"
                 " remodelling is more recent\n"
                 "- The price of a house increases when the surface area of"
                 " the 1st floor (measured in square feet) increases\n"
                 "- The price of a house increases when the state of the"
                 " garage is NOT unfinished\n")
    # in this section we'll show the correlation plots for the 10
    # most correlated variables, a correlation heatmap and a pps heatmap
    st.markdown('#### Correlation Plots')
    st.write("---")
    if st.checkbox('Heatmap'):
        st.write("This image shows how the different variables are correlated"
                 " together. In order to read it you need to take note of the"
                 " sidebar. On it you'll find the colors mapped to the levels"
                 " of the correlation. As I previously mentioned, the closer"
                 " the value is to -1 or 1 the better is the correlation.")
        st.image(
            "outputs/images/corr_heatmap.png", width=1200)

    if st.checkbox('1st Floor Squared Feet'):
        st.write('In this plot we can clearly see that there is a moderate'
                 " level of correlation with the sf area of the 1st floor."
                 " Precisely we notice that when the surface area increases"
                 " we get weaker level of correlation. This means that, in"
                 " simple terms, bigger is not always better.")
        st.image(
            "outputs/images/correlation_1stFlrSF.png", width=1200)

    if st.checkbox('Garage Area'):
        st.write('In this plot we have a similar correlation dynamic as the'
                 " previous one. The correlation gets weaker as the value of"
                 " the squared feet of the area increases.")
        st.image(
            "outputs/images/correlation_GarageArea.png", width=1200)

    if st.checkbox("Garage Finish"):
        st.write("Here we find a different plot. This is called a violin plot."
                 " In this plot the we can also notice that the variable we"
                 " are analyzing is wether the garage state is finished or not"
                 "In this case we see way higher prices for few houses with"
                 " finished garages but most of the other houses are around"
                 "100K and 250k.")
        st.image(
            "outputs/images/correlation_GarageFinish_Unf.png", width=1200)

    if st.checkbox("Year Built of the Garage"):
        st.write("In this case the plot is showing us a slightly more linear"
                 "correlation. We can still appreciate some outliers in the"
                 "group but generally we see that the price increases if the"
                 "garage is newer.")
        st.image(
            "outputs/images/correlation_GarageYrBlt.png", width=1200)

    if st.checkbox("Squared Feet of Living Area Above Ground"):
        st.write("This plot has similar correlation dynamics as our first plot"
                 " The correlation is strong at first but after a certain"
                 " threshold it gets weaker. We should be careful when drawing"
                 " conclusions about the price. This variable gives us some"
                 " insights but we need to take into considearation other"
                 " factors before deciding a final selling price.")
        st.image(
            "outputs/images/correlation_GrLivArea.png", width=1200)

    if st.checkbox("Average Kitchen Quality"):
        st.write("Here we have another violin plot. We can see that the"
                 " majority of the houses are priced around 200k. An curious"
                 " fact is that the highest price for houses with average"
                 " kitchens is just shy of 400k. This is a useful"
                 " discriminatory value and it will allow us to make more"
                 " precise decision based on the state of the kitchen in our"
                 " properties.")
        st.image(
            "outputs/images/correlation_KitchenQual_TA.png", width=1200)

    if st.checkbox("Overall Quality of the Property"):
        st.write("Despite this being the variable that more than any other"
                 "correlates to the final sale price, we notice an"
                 "interesting trend. The better the higher the Overall Quality"
                 " value, the more variation in final price. Obviously this"
                 " metric is a summary of many others and it is in line with"
                 " the other plots with similar metrics")
        st.image(
            "outputs/images/correlation_OverallQual.png", width=1200)

    if st.checkbox("Squared Feet of the Basement"):
        st.write("Similar to other plots we've seen, here we also notice that"
                 " the correlation gets weaker when the value on the x axis"
                 " increases. One thing we can see from this specific plot is"
                 " that the price increases dramatically even with a relative"
                 " small increase of the basement surface area.")
        st.image(
            "outputs/images/correlation_TotalBsmtSF.png", width=1200)

    if st.checkbox("Construction Year of the House"):
        st.write("This plot is posseses quite a few similarities to the one"
                 " which shows the construction year for the garage. Here,"
                 " thanks to the visual plot, we see that even some houses"
                 " built in the past century can still retain an appreciable"
                 " value. There is also the presence of many outlier values"
                 " so careful consideration is advised when taking this metric"
                 " in order to decide a final price.")
        st.image(
            "outputs/images/correlation_YearBuilt.png", width=1200)

    if st.checkbox("Year of Remodeling"):
        st.write("As all other metrics where the construction year was taken"
                 " into account, here too we see that the correlation is not"
                 " the best but we can still see moderate levels. The values"
                 " for the various years are indicative of the value of the"
                 " property only to a certain extent. Lots of outliers tell us"
                 " that we need to include insights from other variables when"
                 " considering a final price.")
        st.image(
            "outputs/images/correlation_YearRemodAdd.png", width=1200)

    if st.checkbox("Predictive Power Score Heatmap"):
        st.write("This is another heatmap but it shows the correlations"
                 " calculated with the Predictive Power Score method. This"
                 " method is when we want to find correlations that might"
                 " remain hidden when using conventional process like the"
                 " Spearman method we've used for all of our previous"
                 " correlations. In this heatmap is important to remember that"
                 " even a 0.2 value for correlation is considered moderate.")
        st.image(
            "outputs/images/pps_heatmap.png", width=1200)
