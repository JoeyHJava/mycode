d#!/usr/bin/python3
import datetime
import requests
import pprint
## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    # nasacreds = "api_key=" + nasacreds.strip("\n")
    nasacreds = "api_key=" + "8tkHvBrwS3EIB7OoEQxgfyzMjAwOsE3t9OObcsWs" #change this XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"
    start = input("Provide start date. ")
    endDate = "2001-11-11"
    endDateQuestion = input("Would you like to provide an endate (y/n)? ")
    if endDateQuestion == 'y':
        endDate = input("provide nd date in YYYY-MM-dd format.")
    print("END DATE LLLLLLLLLLLLLLL ", endDate)
    # def validate(date_text):
    #     try:
    #         datetime.datetime.strptime(date_text, '%Y-%m-%d')
    #     except ValueError:
    #         raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&endDate" +  endDate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    pprint.pprint(neodata)

if __name__ == "__main__":
    main()
