import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

title = None
xaxis = None
yaxis = None
data = None


# functions ///////////////////////////////     


def parse_input(boxdata):       #converting the text input values to a list of floats
    boxdata = boxdata.replace(",", " ").split()
    i = len(boxdata) 
    x = 0
    while x < i:
        boxdata[x] = float(boxdata[x])
        x += 1
    return boxdata

def csvinput(uploaded_file):
    df = pd.read_csv(uploaded_file)
    data = df.values.flatten().astype(float).tolist()
    return data

def histo(data,title,xaxis,yaxis):        #histogram function
    fig, ax = plt.subplots(facecolor="#0d1118")
    ax.set_facecolor("#0d1118") 
    ax.hist(data, 
            bins = "fd",
            color ="white",
            edgecolor="lightgrey")
    ax.set_title(title,
                 family="DejaVu Sans",
                 color="white",
                 fontweight="bold")
    ax.set_xlabel(xaxis,
                  family="DejaVu Sans",
                  color="white",
                  fontweight="bold")
    ax.set_ylabel(yaxis,
                  family="DejaVu Sans",
                  color="white",
                  fontweight="bold")
    ax.tick_params(axis="both",
                   colors="white",
                   labelcolor="white",
                   which="both",)
    
    for spine in ax.spines.values(): #make little tick thingys white
        spine.set_color("white")
    plt.tight_layout()

    return(fig, ax) 



# display ///////////////////////////////     

st.title("Histogram Tool")      #title

boxdata = st.text_input("Data Input:")      #input textbox for data
uploaded_file = st.file_uploader("Or upload a file")           #dropbox


title = st.text_input("Title:")                #title
xaxis = st.text_input("Label x-axis:")          #xaxis
yaxis = st.text_input("Label y-axis:")          #yaxis

with st.popover("Settings"):            #settings for smt
    st.markdown("Settings")
    



# backend stuff ///////////////////////////////    
try:
    data = parse_input(boxdata)
except ValueError:
    st.error("Please only add numbers (comma & space separated)")
    data = None

if uploaded_file != None:           #checking if the uploaded file is valid or not
    if uploaded_file.name.endswith(".csv"):        #if it ends w/ csv its valid (.csv file)
        pass
    else:
        st.error("Please upload a valid supported file! (.csv)")        #error msg if not

if uploaded_file != None:
    data = csvinput(uploaded_file)
    fig, ax = histo(data,title,xaxis,yaxis) # call function
    st.pyplot(fig)  #load graph

elif boxdata != None:
    data = parse_input(boxdata)
    fig, ax = histo(data,title,xaxis,yaxis) # call function
    st.pyplot(fig)  #load graph







                 