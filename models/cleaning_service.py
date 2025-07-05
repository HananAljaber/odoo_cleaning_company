from odoo import models, fields

class CleaningService(models.Model):
    _name = "cleaning.service"
    _description = "Cleaning Service"

    name = fields.Char(string="Service Name", required=True)
    price_per_hour = fields.Float(string="Price per Hour", required=True)
    description = fields.Text(string="Description")
    

