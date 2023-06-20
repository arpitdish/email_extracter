import pandas as pd
import re


subject_data = st.text_input("Enter the Subject of the Email")

body_data = st.text_area("Enter the Body of the Email")

def cleaning_data(data):
	cleaning_review= re.sub('[^a-zA-Z0-9/:]',' ',data)
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
		event_state=match.group(0)
	   	return event_state
	else:
	    return "No match found"


final_clean_data= cleaning_data(body_data)

print("Ticket Number: ", ticket_no(final_clean_data))
print("Start Date: ", date_and_time(final_clean_data)[0])
print("Start Time: ", date_and_time(final_clean_data)[1])
print("End Date: ", date_and_time(final_clean_data)[2])
print("End Time: ", date_and_time(final_clean_data)[3])
print("Location: ", location(final_clean_data))

print("Vendor: ", vendor(subject_data))
print("Stuatus: ", status(subject_data))