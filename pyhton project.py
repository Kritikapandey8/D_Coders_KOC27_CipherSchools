class_AW = {
        "Azmi":"748886**",
        "Adiya Raj":"62079373",
        "Debasis Sahu":"78550322",
        "Arhiant Jain":"95097*730",
        "Kamal Singh": "6367615068",
        "Kritika Pandey": "6268938510",
        "Aditi":"9508660033",
        "Mansi":"8303934546",
        "Amisha":"9569990704",
        "Deepali":"8931001730",
        "Pallavi":"6204326370",
        "Harsh":"8396016718",
        "Rahul Kanyal":"6397090527",
        "Khushpreet kaur":"6280878685",
        "Mohit":"9599766609",
        "Isha":"8950687682",
        "Sparsh":"6393006650",
        "Rechi":"9550673648",
        "Kapil":"6377054831",
        "Ujjawal":"6376747170",
        "Sai krishna":"6281271608",
        "Mohd. Afaq":"7727892007",
        "Gaurav":"7895806221",
        "Sakshi":"8306708813",
        "Navdeep":"8530876498",
        "Dheeraj":"8629051279",
        "Sinan":"8714170520",
        "Naga Sai Reddy":"89193003762",
        "Rahul Rajeshwar":"9074031840",
        "Aditya":"9168546881",
        "Sonu":"9358421276",
        "Shivam Yadav":"9386840524",
        "Vignesh":"9391588556",
        "Suhaib":"9622084629",
        "Sohil":"9675336153",
        "Prateek":"9772159844",
        "Ritik":"9801830465",
        "Yash":"8576942222",
        "Rahul Gupta":"8427533412",
        "Divyendra":"8263043261",
        "Arshil":"6393274424",
        "Deepak":"7634088256",
        "Abhay":"7900569319",
        "Ashutosh singh":"7988842174",
        "Yunesh":"8000969036",
        "Sudarshan Reddy":"8074747385",
        "Nani":"8106808412",
        "Shivam Prakash":"8368319653",
        "Simar":"9877675724",
        "Shivansh":"8368310200",
        "Saqib":"7006489594",
        "Roshan":"7478177365",
        "Kartikey":"7985966256",
        "Kartik":"7981376828",
        "Mohit Choudhary":"8824958436",
        "Shahid": "9319801328",
        "Shivam": "9508187092",
        "Mashuk": "9633848403",
        "Tarun": "9805394341",
        "Saad":"8340115069",
        "Arshdeep Singh": "7888401683",
        "Abhishek":"9508504054",
        "Ashutosh Negi":"8894649843"}




print("Type name to get phone number.")
print("Type exit to exit.")
a=input("name: ")
while True:
    if a !="exit":
        if a.title() not in class_AW:
            print("Enter valid name.")
            a = input("Name: ")
        else:
            print(class_AW.get(a.title()))
            a = input("Name: ")
    else:
        break