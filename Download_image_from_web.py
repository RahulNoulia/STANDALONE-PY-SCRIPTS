
"""
        Explaination of a Script ->
        First of all import requests modeule (install it by command on terminal pip3 install requests )
        Here the variable response object store the http response which is return by get function of module requests .
        get function is use to send http request to the server and save the response in  a response object .
        After that when we get the response object then we have to write it to a new file in a binary mode   .
"""

import requests

"""
 example of url (  https://images.alphacoders.com/793/793242.jpg ) 

 want to test Script use the above  image url  

"""


url = input("Enter url of image which u want to download -> ")

format = input("\nEnter image format ( jpg/png )->")



try:

    response_object  = requests.get(url,stream=True)



    if format=="jpg":

        with open("image.jpg",'wb') as file_object:

        # Here The http response content ( which is stored in a response_object ) is write to a file called image.jpg in binary format

            file_object.write(response_object.content)

    else:

        r = requests.get(url)

        with open("inamge.png",'wb') as file_object:

            file_object.write(response_object.content)

except requests.exceptions.MissingSchema:

    print("\n\n Entered url is not valid try again !!\n\n USAGE ->\n url =  https://images.alphacoders.com/793/793242.jpg \n format = jpg or png")
