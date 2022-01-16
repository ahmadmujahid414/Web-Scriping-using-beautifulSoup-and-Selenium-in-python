from bs4 import BeautifulSoup
import requests
import Edmunds_Automation as EA

def Soup():
    content = EA.website_content()
    soup = BeautifulSoup(content,'html.parser')
    return soup
Car_name = list()
def access_to_car_names():
    soup = Soup()
    content = soup.find('ul',class_='usurp-card-list list-unstyled align-items-stretch row')

    #we will create a set datastructure to store 
    #links of the different cars
    #to accesss them after
    for car_href_link in content.find_all('a'):
        links = (car_href_link.text)
        if links.strip():
            Car_name.append(links)
    
#return name of the cars 
# these name also will be used as links 
def Car_List():
    return Car_name

#return price of a car in text
def price():
    soup = Soup()
    price = soup.find('div',class_='heading-2 mb-0')
    return price.text

#return VIN of a car in text
def VIN():
	soup = Soup()
	vin = soup.find('span',class_='mr-1')
	return vin.text

#return summary details of a car in text form
def VehicleSummary():
	soup = Soup()
	summary = " "
	div_tag = soup.find('section',class_='vehicle-summary mb-0_5 text-gray-darker')
	for su in div_tag.find_all('div'):
		summary= summary+str(su.text)+"\n"
	return summary

#return Top Features details of a car in text form
def Top_Features():
	soup = Soup()
	features = " "
	div_tag = soup.find('section',class_='features-and-specs text-gray-darker')
	for fs in div_tag.find_all('div'):
		features = features+str(fs.text)+"\n"
	return features



