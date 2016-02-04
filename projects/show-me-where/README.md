# Show Me Where Project

# About the dataset

The Office of Arts & Culture is counting every existing theater, gallery, arts office, rehearsal room, library, music club, museum, and cinema (i.e. cultural space) in Seattle. The dataset contains slightly more than 850 spaces and its fields contain the address, latitude and longitude (or geolocation) of practically all of those cultural spaces as well as descriptions of the place, their websites, and its audience/ customers.


## Basic facts about the dataset

- The source of the data: [Seattle, Open Data Portal](https://data.seattle.gov/)
- The data's landing page: [Seattle Cultural Space Inventory](https://data.seattle.gov/Community/Seattle-Cultural-Space-Inventory/vsxr-aydq)
- Direct link to the data: [https://data.seattle.gov/api/views/vsxr-aydq/rows.csv?accessType=DOWNLOAD&bom=true](https://data.seattle.gov/api/views/vsxr-aydq/rows.csv?accessType=DOWNLOAD&bom=true)
- The data format: CSV
- Number of rows: 857

## Description of data fields

#### Name

Contains a __text string__ representing the name of the cultural space.


#### Phone

Contains a __text string__ representing the 10-digit phone number of the cultural space, mostly written in this format: "(207) 799-1180" *but not always* written in that format. Other formats include: "206-935-1966" or "2069301276"


#### URL

Contains a __text string__ representing the URL of the cultural space. Typically beings with a "www.", but not necessarily...


#### Square Feet Total

Contains a __number__ that represents the size of the cultural space in square feet.


#### Neighborhood

Contains a __text string__ representing the neighborhood in Seattle the cultural space resides in.


#### Nonprofit?

Contains a __text string__ representing whether or not the cultural space is a nonprofit. If it is, it's denoted with a "Y", if not it's denoted with a "N", if government owned it's designated by "Government", if some combo it is marked, "Other", and if unclear there is nothing in the box.


#### Dominant Discipline, 2nd Discipline, 3rd Discipline

These three data fields each contain a __text string__ representing a discipline the cultural space promotes. Examples of disciplines include: "Performance", "Literary", "Multi-use", "Studios", and "Heritage".


#### Year of Occupation

Contains a __number__ that represents the year the cultural space was moved into. All are 4 digits (if the number is there at all (which most are!)).


#### Own or Rent?

Contains a __text string__ representing whether the cultural space is rented or owned. If rented the designation is "R", if owned the designation is "O", and if some combo the designation is "Other". It seems to be all filled in.


#### Year bldg built?

Contains a __number__ that represents the year the cultural space was built. All are 4 digits (if the number is there at all (which most are)).


#### Year Founded

Contains a __number__ that represents the year the business was founded. All are 4 digits (if the number is there at all (which most are!)).


#### Previous Facilities?

Contains a __number__ that represents the amount of previous buildings the business had. Numbers range from 0 upwards, and nearly all seem to be filled out.


#### How many Theaters?

Contains a __number__ that represents the amount of theaters the cultural space has. Numbers range from 0 upwards, and nearly all seem to be filled out.


#### Seats Total?

Contains a __number__ that represents the amount of seats the theaters in the cultural space have. Numbers range from 0 upwards, and most seem to be filled out.


#### Theater 1, 2, 3, 4, and 5

Contains a __text string__ that should represent (I suppose) the name of the theater in the cultural space. **However**, I don't see anything filled out.


#### Seats in Theater 1, 2, 3, 4, and 5

Contains a __number__ that should represent the amount of seats in the respective theater of the cultural space. **However**, I don't see anything filled out.


#### Visual Art Galleries?

Contains a __text string__ representing whether the cultural space has a visual art gallery. If it does, it's denoted with a "Y", if not it's denoted with a "N", and if not known it's not filled in or "I don't know" is written.


#### Square Feet

Contains a __number__ that represents the size of the Visual Art Gallery of the cultural space in square feet. Numbers range from 0 upwards, and most are filled in.


#### ADA Compliant

Contains a __text string__ representing whether the cultural space is compliant with the ADA. If it is, it's denoted with a "Y", if not it's denoted with a "N", and if not known it's not filled in or "I don't know" is written.


#### Parking Spaces?

Contains a __number__ that represents the amount of parking spaces the cultural space has. Numbers range from 0 upwards, and most are filled in.


#### Street Frontage?

Contains a __text string__ representing whether the cultural space has street frontage. I think this means if it's off of a street, but I'm not 100% certain. Anyways, if it does, it's denoted with a "Y", if not it's denoted with a "N", and if not known it's not filled in or "I don't know" is written.


#### Rental Space Avail?

Contains a __text string__ representing whether the cultural space has room for rent. If it does, it's denoted with a "Y", if not it's denoted with a "N", and if not known it's not filled in or "I don't know" is written.


#### Serve Alcohol?

Contains a __text string__ representing whether the cultural space serves alcohol. If it does, it's denoted with a "Y", if not it's denoted with a "N", and if not known it's not filled in.


#### Funded by A&C?

Contains a __text string__ representing whether the cultural space is funded by A&C or not. Honestly I don't know what A&C is, so I probably won't use this. But anyways, if it is, it's denoted with a "Y", if not it's denoted with a "N", and if not known it's not filled in or "I don't know" is written.


#### Stability Index (5=very stable, 1=very uncertain)

Contains a __number__ that represents how stable the cultural space is. I'm not certain if this means structurally or as a business staying in that place so I probably won't touch this measure either. Numbers range from 1 to 5, and most are filled in.


#### Constituency over 50% one race?

Contains a __text string__ representing a (essentially) how diverse the audience of the cultural space is. Some answers include: "No single race is more than 50% of our audience", "White", "Native American and Alaska Native", "Two or more races", and "Black or African American".


#### Site control through (date)

Contains a __text string__ representing if the cultural space has site control for a while. There seems to be no standard formatting whatsoever so I will not be using this data field.


#### Closed date

Very unclear what this data field is supposed to represent. There seems to be no standard formatting whatsoever so I will not be using this data field.


#### Closed

Contains a __number__ that is boolean in nature representing if the cultural space is closed or not. "1" means yes it's true, it's closed. "0" means false - it's open! The ones that are blank or with strings will have to be looked over.


#### Address

Contains a __text string__ of the street address of the cultural location. The location is often described as being one specific place like "5423 Delridge Way SW, Seattle, WA 98106" or occasionally as a PO Box like "PO BOX 16306, Seattle, WA 98116". It appears that all are filled in.


#### Location

Contains a __location__ that represents the latitude and longitude coordinate of the incident location. All the data points look like this: (47.5530455˚, -122.3632976˚) or aren't included. But nearly all are included.


## Anticipated data wrangling

Not everything is filled in completely, so I'll have to choose what seems most interesting after I see how much data is filled in for that column.

I also don't like how not everything is in a standard format, so I'll either have to write several regular expressions or skip over some rows.