# Import the csv package to access DictReader
import csv

rows = []


with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

def data(r):
    open_request = 0
    type_complaint = {}
    request_per_bor = {}
    for row in r:
        if 'complaint_type' in row:
            type_complaint[row['complaint_type']] = type_complaint.get(row['complaint_type'], 0) + 1
        if 'borough' in row: 
            request_per_bor[row['borough']] = request_per_bor.get(row['borough'], 0) + 1
        if row['resolution_status'] == "Open":
            open_request += 1
    
    find_max_complaint = max(type_complaint, key=type_complaint.get)

    sorted_boro = sorted(request_per_bor.items())
    
    boro = ""
    for key, value in sorted_boro:
        boro += f"-{key}: {value}\n"

    print(boro)

    return open_request, {find_max_complaint, type_complaint[find_max_complaint]}, boro

open_rq, t_complaint, boro = data(rows)


    

meaning_of_life = 42

with open('output.txt', 'w') as f:
    t_complaint_value, t_complaint_key = t_complaint
    f.write(f"""Open Requests: {open_rq} 
    \nMost common complaint type: {t_complaint_value} ({t_complaint_key} requests)
    \nRequests per borough: \n{boro} """) 

print("Output saved to output.txt")