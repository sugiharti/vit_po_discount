from openerp import api, fields, models, _

class PurchaseOrderLine(models.Model):
	_name = 'purchase.order.line'
	_inherit = 'purchase.order.line'

	@api.model
	def _calc_line_base_price(self,line):
		res = super(PurchaseOrderLine, self)._calc_line_base_price(line)
		return res*(1 - line.discount/100.0)

	_description = 'Purchase Order Line'
	discount = fields.Float(string='Discount')
