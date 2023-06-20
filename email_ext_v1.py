import streamlit as st
import pandas as pd
import re

st.subheader("Email Extraction made simple (Sorry, Only for Crown Castle for now!)")


subject_data = st.text_input("Enter the Subject of the Email")

body_data = st.text_input("Enter the Body of the Email")

def cleaning_data(data):
	cleaning_review= re.sub('[^a-zA-Z0-9/:]',' ',str(data))
	return cleaning_review



def ticket_no(text):
	match = re.search(r'Ticket Number:\s*([A-Z]+\d+)', text)
	ticket_number = match.group(1) if match else None

	if ticket_number:
	    return ticket_number
	else:
	    return "Ticket number not found"



def date_and_time(text):
	pattern = r'(\d{1,2}/\d{1,2}/\d{4}) (\d{1,2}:\d{2} [AP]M)'
	matches = re.findall(pattern, text)

	if matches:
	    start_date = matches[0][0]
	    start_time = matches[0][1]
	    end_date = matches[1][0]
	    end_time = matches[1][1]
	    return (start_date, start_time, end_date, end_time)
	else:
	    return "No matches found"



def location(text):
	pattern = r'Location of Work:  (\w+\s?\w+)'
	match = re.search(pattern, text)

	if match:
	    location_of_work = match.group(1)
	    return location_of_work
	else:
	    return "No match found"



def vendor(sub_text):
	pattern= r'Castle'
	match=re.search(pattern,sub_text)
	if match:
		return "Crown Castle Fiber"
	else:
	    return "No match found"


def status(sub_text):
	pattern = r'Event (\w+\s?\w+)'
	match = re.search(pattern, sub_text)

	if match:
	    return match.group(0)
	else:
	    return "No match found"


final_clean_data= cleaning_data(body_data)


st.write("Ticket Number: ", ticket_no(final_clean_data))
st.write("Start Date: ", date_and_time(final_clean_data)[0])
st.write("Start Time: ", date_and_time(final_clean_data)[1])
st.write("End Date: ", date_and_time(final_clean_data)[2])
st.write("End Time: ", date_and_time(final_clean_data)[3])
st.write("Location: ", location(final_clean_data))

st.write("Vendor: ", vendor(subject_data))
st.write("Stuatus: ", status(subject_data))

st.write("Body: ", body_data)