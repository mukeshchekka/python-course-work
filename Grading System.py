for i in data.keys():
    print(f'{i}.data[i]["name"]')
studid=int(input("Enter the student id: "))
if studid in data:
    if data[studid]["exam_status]:
                    total=(data[studid]["python"]+data[studid]["sql"]+data[studid]["html"])/3
                    if total>90:
                        print(f'congrats!!!\n{data[studid]["name"]} got "A" grade')
                    elif total>75:
                        print(f'Good!!!\n{data[studid]["name"]} got "B" grade')
                    elif total>50:
                        print(f'Need Improvement!!!\n{data[studid]["name"]} got "C" grade')
                        
                    
                    
