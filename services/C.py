from flask import request
from flask import jsonify
from services import helperfunctions as help
import simulate_dbCalls as database 
import customer as customer
import datetime

class C():
	def __init__(self,customer_id, base_price=0.4, discount = 0):
            self.customer_id = customer_id
            self.base_price = base_price
            self.discount = discount
		
def serviceC():
    try:
            
        if request.method == 'GET':
            return "400",400 

        if request.method == 'POST':
            data = request.json

            customer_id = data['customer_id']
            start = data['start']
            end = data['end']


            #In this case I want to make a database query for the customer, to be able to fetch discounts
            #and agreed price, If no price is agreed it will be the default. Since this is a micro service I will assume
            #that a database storing all the customers with their agreed prices, can be queried.
            customer_db = database.getCustomer(customer_id)
            database.insertStartDate(customer_id,start,service="c")

            c =  customer.Customer(customer_id,start)
            ServiceC = C(customer_id)

            discount = ServiceC.discount
            free_days = c.free_days

            if customer_db["discount"] != 0:
                discount = customer_db["discount"] 

            if customer_db["free_days"] != 0:
                free_days = customer_db["free_days"]

            if customer_db["price-C"] != 0:
                ServiceC.base_price = customer_db["price-C"]


            if discount > 100:
                discount = 100
            if discount < 0:
                discount = 0


            if discount != 0:
                new_discounted_price = (100-discount)/100*ServiceC.base_price
                ServiceC.base_price = new_discounted_price


            days = help.days(start, end, serviceC=True)
            if free_days != 0:

                if days > free_days:
                        database.updateFreeDays(customer_id, 0)
                else:
                    days_left = free_days - days 
                    if days_left < 0:
                        days_left = 0
                    database.updateFreeDays(customer_id,days_left)
                days = days - free_days
            total_price =  days * ServiceC.base_price

            if total_price < 0:
                total_price = 0

            obj = {
                "service": "A",
                "customer_id": customer_id,
                "start": start,
                "end": end,
                "discount": discount, 
                "price": ServiceC.base_price,
                "estimated-price-euro": "{:.2f}".format(total_price),
                }


        return jsonify(obj)

    except IndexError:
            return "Error in body of the request.", 400








