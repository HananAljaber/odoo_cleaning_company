from odoo import models, fields, api

class CleaningOrder(models.Model):
    _name = "cleaning.order"
    _description = "Cleaning Order"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    service_id = fields.Many2one("cleaning.service", string="Service", required=True)
    hours = fields.Integer(string="Hours", required=True, default=1)

    price_per_hour = fields.Float(string="Price per Hour", compute="_compute_price", store=True)
    total_price = fields.Float(string="Total Price", compute="_compute_total_price", store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('quoted', 'Quoted'),
        ('invoiced', 'Invoiced'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='draft', string="Status", tracking=True)


    cleaner_id = fields.Many2one('hr.employee', string="Cleaner")

    @api.depends('service_id')
    def _compute_price(self):
        for rec in self:
            rec.price_per_hour = rec.service_id.price_per_hour

    @api.depends('price_per_hour', 'hours')
    def _compute_total_price(self):
        for rec in self:
            rec.total_price = rec.price_per_hour * rec.hours
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_reset_to_draft(self):
        for rec in self:
            rec.state = 'draft'
    def action_create_invoice(self):
        for rec in self:
            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': rec.customer_id.id,
                'invoice_date': fields.Date.today(),
                'invoice_line_ids': [(0, 0, {
                    'name': rec.service_id.name,
                    'quantity': rec.hours,
                    'price_unit': rec.price_per_hour,
                })]
            })
            rec.state = 'invoiced'
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'res_id': invoice.id,
                'view_mode': 'form',
                'target': 'current',
            }
