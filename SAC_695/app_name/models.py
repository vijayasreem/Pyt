from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    # Indexing
    indexing_engine = models.CharField(max_length=50, default='ElasticSearch')
    
    def __str__(self):
        return self.name
        
    def index_data(self):
        # Automatically index the product data in the search engine or database
        pass
    
    def update_index(self):
        # Automatically update the search index to reflect any changes
        pass
    
    def execute_query(self):
        # Execute search queries against the search index instead of querying the database
        pass