data=open("file.txt","r")
isLarger_count=0
bucket1=[]
bucket2=[]
bucket3=[]
for i,measurement in enumerate(data):
    current_measurement=int(measurement)
    if i<3:
        prev_measurement=int(measurement)
        continue
    if current_measurement>prev_measurement:
        isLarger_count=isLarger_count+1
    prev_measurement=current_measurement
print(isLarger_count)