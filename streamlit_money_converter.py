import streamlit as st

page_bg_color = '''
<style>
body {
background-image: url('https://t4.ftcdn.net/jpg/02/66/97/53/360_F_266975389_sBNp4HyE8gG58U62Fv2A6JTsaAVtLMk4.jpg');
background-size: cover;
}
</style>
<h1 style="font-family:'Impact'">Online Money Converter</h1>
'''

st.markdown(page_bg_color, unsafe_allow_html=True)
input_unit = st.selectbox('Convert',['dollars','rupees','euros','pounds'])
output_unit = st.selectbox('To',['dollars','rupees','euros','pounds'])
value = st.number_input('Enter Value')
done = st.button('Convert')

converted_value = 0


# 1 dollar = 72.55 r, 0.83 euro, 0.71 pounds
# 1 ruppee = 0.014 d, 0.011 euro, 0.0098 pounds
# 1 euro = 87.92 r, 1.21 d, 0.86 pounds
# 1 pound = 1.40 d, 101.70 r, 1.16 Euro


def convert(x):
    global converted_value
    if input_unit == 'dollars' and output_unit == 'rupees':
        converted_value = x*72.55
        st.subheader('$'+str(x)+' is equal to  '+'₹ '+str(converted_value))
    elif input_unit == 'dollars' and output_unit == 'euros':
        converted_value = x*0.83
        st.subheader('$'+str(x)+' is equal to  '+'€ '+str(converted_value))
    elif input_unit == 'dollars' and output_unit == 'pounds':
        converted_value = x*0.71
        st.subheader('$' + str(x) + ' is equal to  ' + '£ ' + str(converted_value))
    #=============================================================================
    elif input_unit == 'rupees' and output_unit == 'dollars':
        converted_value = x*0.014
        st.subheader('₹ '+str(x)+' is equal to  '+'$ '+str(converted_value))
    elif input_unit == 'rupees' and output_unit == 'euros':
        converted_value = x*0.011
        st.subheader('₹ '+str(x) + ' is equal to  ' + '€ '+str(converted_value))
    elif input_unit == 'rupees' and output_unit == 'pounds':
        converted_value = x*0.0098
        st.subheader('₹ '+str(x) + ' is equal to  ' + '£ '+str(converted_value))
    #=============================================================================
    elif input_unit == 'euros' and output_unit == 'dollars':
        converted_value = x*1.21
        st.subheader('€ '+str(x)+' is equal to  '+'$ '+str(converted_value))
    elif input_unit == 'euros' and output_unit == 'rupees':
        converted_value = x*87.92
        st.subheader('€ '+str(x) + ' is equal to  ' + '₹ '+str(converted_value))
    elif input_unit == 'euros' and output_unit == 'pounds':
        converted_value = x*0.86
        st.subheader('€ '+str(x) + ' is equal to  ' + '£ '+str(converted_value))
    #=============================================================================
    elif input_unit == 'pounds' and output_unit == 'dollars':
        converted_value = x*1.40
        st.subheader('£ '+str(x)+' is equal to  '+'$ '+str(converted_value))
    elif input_unit == 'pounds' and output_unit == 'rupees':
        converted_value = x*101.70
        st.subheader('£ '+str(x) + ' is equal to  ' + '₹ '+str(converted_value))
    elif input_unit == 'pounds' and output_unit == 'euros':
        converted_value = x*1.16
        st.subheader('£ '+str(x) + ' is equal to  ' + '£ '+str(converted_value))
    #=============================================================================
    elif input_unit and output_unit == 'dollars' or input_unit and output_unit == 'rupees' or input_unit and output_unit == 'euros' or input_unit and output_unit == 'pounds':
        st.markdown('<h1 style="color:red;font-family:Consolas;">Same UNITS Provided! 😕</h1>', unsafe_allow_html=True)





if done:
    convert(value)
