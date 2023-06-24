from django.db import models

# Create your models here.
class League(models.Model):
    league_id = models.CharField(max_length=200)
    league_realm = models.CharField(max_length=200)
    league_text = models.CharField(max_length=200)
    def __str__(self):
        return self.league_text
    
class Static(models.Model):
    static_type_id = models.CharField(max_length=200,null=True)
    static_type_label = models.CharField(max_length=200,null=True)
    static_id = models.CharField(max_length=200,null=True)
    static_text = models.CharField(max_length=200,null=True)
    static_image_url = models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.static_type_label + self.static_text
    
class SearchStats(models.Model):
    search_stat_id = models.CharField(max_length=200)
    search_stat_label = models.CharField(max_length=200)
    stat_id = models.CharField(max_length=200)
    stat_text = models.CharField(max_length=200)
    stat_type = models.CharField(max_length=200)
    def __str__(self):
        return self.search_stat_label + self.stat_text
    
class Items(models.Model):
    item_type_id = models.CharField(max_length=200)
    item_type_label = models.CharField(max_length=200,null=True)
    item_name = models.CharField(max_length=200,null=True)
    item_type = models.CharField(max_length=200,null=True)
    item_text = models.CharField(max_length=200,null=True)
    item_json_flags = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.text