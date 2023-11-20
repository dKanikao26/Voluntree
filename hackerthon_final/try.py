# # # data1={
# # #     "Punjab":
# # #         [
# # #             {"User": "Karman", "Title": "Swatch bharat", "Desc": "we will clean india"},
# # #             {"User": "rehet", "Title": "Swatch bharat 1", "Desc": "we will clean Bharat"}
# # #         ]
# # # }
# # # a=input("state: ")
# # try:
# #     data1[a].append({"User": "Anhad", "Title": "Swatch bharat 1", "Desc": "we will clean Bharat"})
# # except KeyError:
# #     data1[a]=[]
# #     data1[a].append({"User": "Anhad", "Title": "Swatch bharat 1", "Desc": "we will clean Bharat"})
# #
# # #
# # # print(data1)
# #
# # import json
# # def write(what):
# #     with open("post_data.json", "w") as file:
# #         json.dump(what, file, indent=4)
# #
# #
# #
# #
# # data1={
# #     "Punjab":
# #         [
# #             {"User": "Karman", "Title": "Swatch bharat", "Desc": "we will clean india"},
# #             {"User": "rehet", "Title": "Swatch bharat 1", "Desc": "we will clean Bharat"}
# #         ]
# # }
# # try:
# #     with open("post_data.json", "r") as file:
# #         data = json.load(file)
# # except FileNotFoundError:
# #     write(data1)
# #     data=data1
# # else:
# #     data.update(data1)
# #     write(data)
# #
# #
# # print(data)
# #
# # def date_fix(dateee):
# #     listtt=dateee.split("-")
# #     for lis in range(0,len(listtt)):
# #         listtt[lis]=int(listtt[lis])
# #     return listtt
# #
# # print(date_fix("2023-10-03"))
#
#
#
#
#
# data1={
#     "Punjab": [
#         {
#             "User": "Karman",
#             "Title": "Swatch bharat",
#             "Desc": "we will clean india",
#             "Date": [
#                 2022,
#                 4,
#                 19
#             ]
#         },
#         {
#             "User": "rehet",
#             "Title": "Swatch bharat 1",
#             "Desc": "we will clean Bharat",
#             "Date": [
#                 2021,
#                 4,
#                 19
#             ]
#         },
#         {
#             "User": "Karman Singh Sethi Ji",
#             "Title": "Orphanage",
#             "Desc": "help orphans",
#             "Date": [
#                 2023,
#                 10,
#                 30
#             ],
#             "Email": "sethikarmansingh@gmail.com",
#             "Phone number": "09316166166",
#             "Location": "166 r model town Jalandhar"
#         }
#     ],
#     "Goa": [
#         {
#             "User": "Karman Singh Sethi",
#             "Title": "Plant Watering",
#             "Desc": "watering plants",
#             "Date": [
#                 2023,
#                 10,
#                 31
#             ]
#         },
#         {
#             "User": "Navdeep Singh Sethi",
#             "Title": "Beach Cleaning",
#             "Desc": "we will clean beaches",
#             "Date": [
#                 2023,
#                 10,
#                 29
#             ]
#         }
#     ],
#     "Delhi": [
#         {
#             "User": "Anhad Singh",
#             "Title": "Pollution",
#             "Desc": "clean landfills",
#             "Date": [
#                 2023,
#                 10,
#                 30
#             ]
#         }
#     ],
#     "Mumbai": [
#         {
#             "User": "Rehet Kaur Sethi",
#             "Title": "Fish Saving",
#             "Desc": "we will save fishes",
#             "Date": [
#                 2023,
#                 10,
#                 31
#             ]
#         }
#     ]
# }
# import datetime
# todays_date=datetime.datetime.now()
# print(todays_date)
# print(f"{data1}")
# print(todays_date.hour+todays_date.minute)
# all_posts=[]
# a=input("dd")
# print(data1[a])
# for dat in data1[a]:
#     pass
data={
    "Punjab": [
        {
            "User": "Jasnoor",
            "Title": "Obesity ",
            "Desc": "\r\nObesity carries health risks, including heart disease and diabetes, and is associated with stigma and an economic burden. Lifestyle changes and medical interventions can mitigate its effects and improve well-being . We want to aware people about obesity . Its different cons on our society We aware people on various healthier options",
            "Date": [
                2023,
                11,
                7
            ],
            "Email": "dhingranaman0@gmail.com",
            "Phone number": "+919888331477",
            "Location": "2578,Noor Di Bazar ,Near Jyoti Light House, Jandiala Guru, Amritsar"
        },
        {
            "User": "Karman",
            "Title": "River Cleaning ",
            "Desc": "A small river flows through Amritsar near New Amritsar Enclave. During Navratri, many of the people threw holy religious photos , Navaratri's required things into river making the river a mess. About 10-20 tons of religious materials has been gathered in the bank of new Amritsar which is a cause of serious concern. We as citizen of India it is our outmost priority to clean it as soon as possible as it results in the banishing of fisheries resulting in dirty water. so we are organising a river cleaning event in Amritsar which involves the incoming of volunteers at 7 am in the morning. the activity will be of 2-3 hrs where we will be cleaning the river with the help of Amritsar Municipal Cooporation. All people of all ages are allowed in this. ",
            "Date": [
                2024,
                10,
                21
            ],
            "Email": "LiveWithus0@gmail.com",
            "Phone number": "7347372327",
            "Location": "2578,Chache Di Haiti  ,Near Mall of Amritsar , Amritsar"
        },
        {
            "User": "Karan Singh",
            "Title": "Tree Planting",
            "Desc": "It's a mango tree planting",
            "Date": [
                2023,
                11,
                15
            ],
            "Email": "sethikarmansingh@gmail.com",
            "Phone number": "09316166166",
            "Location": "166 r model town Jalandhar",
            "Discussion": [
                {
                    "Harshleen": {
                        "Why only mango trees?": []
                    }
                },
                {
                    "Harshleen": {
                        "Why only mango trees?": []
                    }
                }
            ]
        },
        {
            "User": "Anhad Kaur",
            "Title": "Sewage Cleaning",
            "Desc": "We will remove waste from sewage that is causing blockage of drains",
            "Date": [
                2023,
                11,
                16
            ],
            "Email": "sethikarmansingh@gmail.com",
            "Phone number": "09814865547",
            "Location": "Urban Estate phase II, Jalandhar, Punjab 144022",
            "Discussion": [
                {
                    "Karman": {
                        "How will you arrange gloves?": [
                            "We have tie up with a factory"
                        ]
                    }
                }
            ]
        },
        {
            "User": "Karman Sethi Saab",
            "Title": "Crop Rotation",
            "Desc": "We will educate people about crop rotation",
            "Date": [
                2023,
                11,
                16
            ],
            "Email": "sethikarmansingh@gmail.com",
            "Phone number": "09316166166",
            "Location": "166 r model town Jalandhar",
            "Discussion": [
                {
                    "Karman": {
                        "Do you have knowledge?": [
                            {
                                "hne": "yes"
                            },
                            {
                                "daaaa": "who gave it to you"
                            }
                        ]
                    }
                },
                {
                    "Rehet": {
                        "I want to contribute too": []
                    }
                },
                {
                    "Anhad": {
                        "Event will be awesome": []
                    }
                },
                {
                    "Karman": {
                        "Which crops do we use?": [
                            {
                                "Anhad": "Coriander"
                            }
                        ]
                    }
                }
            ]
        },
        {
            "User": "Karmannn",
            "Title": "Hackerthon",
            "Desc": "coding competition",
            "Date": [
                2023,
                11,
                3
            ],
            "Email": "sethikarmansingh@gmail.com",
            "Phone number": "09814865547",
            "Location": "166-R, Model town",
            "Discussion": []
        }
    ],
    "Uttarakhand": [
        {
            "User": "Rehet Kaur",
            "Title": "Clock Tower Road Cleaning",
            "Desc": "We will clean area near clock tower as it is most polluted and busy road, it is also the only route connecting Delhi and Dehradun",
            "Date": [
                2023,
                11,
                14
            ],
            "Email": "sethikarmansingh@gmail.com",
            "Phone number": "9814865547",
            "Location": "Rest Camp, Dehradun"
        },
        {
            "User": "Anhad Singh Sethi",
            "Title": "Cleaning Plastic Waste In Mussoorie ",
            "Desc": "As it is the end of tourist season so we will clean plastic waste ",
            "Date": [
                2023,
                11,
                9
            ],
            "Email": "sethikarmansingh@gmail.com",
            "Phone number": "9814865547",
            "Location": "Dear park, Mussoorie Road"
        }
    ],
    "Rajasthan": [
        {
            "User": "Kritika",
            "Title": "Women Empowerment",
            "Desc": "  We help women self-help groups get loans from banks, increase the income of poor and marginal women, and social and economic progress of women through skill development",
            "Date": [
                2023,
                11,
                6
            ],
            "Email": "kritika@gmail.com",
            "Phone number": "7347372327",
            "Location": " D-44, Subhash Marg, C-Scheme, Jaipur, Rajasthan, India"
        }
    ],
    "Tamil Nadu": [
        {
            "User": "Karman Singh",
            "Title": "Winter Clothes Distribution",
            "Desc": "We will distribute winter clothes like jacket, sweaters to the students of government schools in Chennai",
            "Date": [
                2023,
                11,
                14
            ],
            "Email": "sethikarmansingh@gmail.com",
            "Phone number": "09316166166",
            "Location": "14, NH 11 Chennai"
        }
    ],
    "Delhi": []
}
emails=[]
STATE="Uttarakhand"
for key,value in data.items():
    if STATE==key:
        for x in value:
            emails.append(x["Email"])
        emails=list(set(emails))
        break
print(emails)