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
    boro_w_most_open_req = {}
    for row in r:
        if 'complaint_type' in row:
            type_complaint[row['complaint_type']] = type_complaint.get(row['complaint_type'], 0) + 1
        if 'borough' in row: 
            request_per_bor[row['borough']] = request_per_bor.get(row['borough'], 0) + 1
        if 'borough' in row and row['resolution_status'] == "Open":
            boro_w_most_open_req[row['borough']] = boro_w_most_open_req.get(row['borough'], 0) + 1
        if row['resolution_status'] == "Open":
            open_request += 1

    
    find_max_complaint = max(type_complaint, key=type_complaint.get)
    find_max_open_boro = max(boro_w_most_open_req, key=boro_w_most_open_req.get)

    sorted_boro = sorted(request_per_bor.items())
    
    boro = ""
    request_per_complaint = ""
    closure_rate = ""
    top_3_boro_req = ""

    for key, value in sorted_boro:
        boro += f"- {key}: {value}\n"

    for key, value in type_complaint.items():
        request_per_complaint += f"- {key}: {value}\n"

    for key, value in sorted(request_per_bor.items()):
        closed = value - boro_w_most_open_req[key]
        rate = round((closed / value) * 100, 1)
        closure_rate += f"- {key}: {rate}%\n"

    sorted_boroughs = sorted(request_per_bor.items(), key=lambda item: (-item[1], item[0]))[:3]

    count = 0
    for key, value in sorted_boroughs:
        count += 1
        top_3_boro_req += f"{count}. {key} ({value} requests)\n"

    print(top_3_boro_req)
    return open_request, {find_max_complaint, type_complaint[find_max_complaint]}, boro, request_per_complaint, {find_max_open_boro, boro_w_most_open_req[find_max_open_boro]}, closure_rate, top_3_boro_req


open_rq, t_complaint, boro, rq_per_complaint, boro_open_req, boro_req_rate, top_3_boro_req = data(rows)




with open('output.txt', 'w') as f:
    t_complaint_value, t_complaint_key = t_complaint
    f.write(f"""Open Requests: {open_rq} 
    \nMost common complaint type: {t_complaint_value} ({t_complaint_key} requests)
    \nRequests per borough: \n{boro} """) 

    boro_req_num, boro_name = boro_open_req
    f.write(f"""\nRequests by complaint type: \n{rq_per_complaint} \nBorough with most open requests: {boro_name} ({boro_req_num} open)
            \nClosure rate by borough: \n{boro_req_rate}\nTop 3 boroughs by total requests:\n{top_3_boro_req}""")


print("Output saved to output.txt")