from transformers import pipeline
import numpy as np




#Data per month:
# - hp brand
# - hp edition
# - price 
# - total number of sales
# - discount at that month
# - sentiment of that month gained from reviews


class Product:
    def __init__(self,product_name) -> None:
        self.product_name = product_name
        self.data_points = []
        self.max_price = self.set_max_price()
    
    def set_max_price(self):
        max_price = 0
        for i in self.data_points:
            mprice = max(i['prices'])
            if max_price == 0:
                max_price = mprice
            elif max_price < mprice:
                max_price = mprice
            
        return max_price 

        

class data_points:
    def __init__(self, hp_brand, month, units_sold) -> None:
        self.hp_model =  hp_brand
        self.month = month
        self.units_sold = units_sold
        self.monthly_reviews = []
        self.prices = []
        self.sentiments = self.get_sentiment()
    ###change this to whole dataset
    def get_max_price(product_max_price):
        return product_max_price
    
    def get_monthly_average_price(self):
        return np.sum(self.prices) / len(self.prices)

    def get_discount(self):

        if self.get_monthly_average_price() == self.get_max_price():
            return 0
        else:
            return 1 - (self.get_monthly_average_price() / self.get_max_price())
    
    def get_sentiment(self):
        
        sentiment = pipeline("sentiment-analysis")
        self.sentiments = sentiment(self.monthly_reviews)
        

    def get_average_sentiment(self):
        
        num_reviews = len(self.monthly_reviews)
        num_positive = 0
        num_negative = 0
        percent_positive = 0
        percent_negative = 0
        for value in self.sentiments:

            if value.label == 'NEGATIVE':
                num_negative +=1
            if value.label == 'POSITIVE':
                num_positive +=1
        
        percent_positive = num_positive/num_reviews
        percent_negative = -1* num_negative/ num_reviews

        return percent_positive, percent_negative


    


dict_ = [{'month': 0, 'prices': [1,3,2,4,10,3,2,44,1,23]},{'month': 1, 'prices': [1,3,2,4,10,3,2,100,1,23]}]





# - Features = [month, discount, average_positive_sentiment, average_negative_sentiment,average_price]
# - Label = units sold 

### - - - This is the form that the data will be scraped in - - - ###

sample_product = Product('Sennheiser Momentum 4')

sample_review_list_for_one_month = ["This product is great", "this product is bad", "this product is good", "this product was amazing"]
sample_product_sale_prices = []
sample_data_scrapped = data_points(sample_product.product_name, 1, 5)
sample_data_scrapped.monthly_reviews = sample_review_list_for_one_month



data_set = []



        





