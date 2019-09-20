# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, models
from openerp.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.constrains('user_ids')
    def _check_user_ids(self):
        user_obj = self.env['res.users']
        for company in self:
            users = user_obj.search([
                ('company_id', '=', company.id),
                ('share', '=', False)])
            accepted_users = company.user_ids
            conflict_users = [x for x in users if x not in accepted_users]
            if conflict_users:
                raise ValidationError(_(
                    "Unable to remove the company %s for the following"
                    " users because this is their current company.\n"
                    "Please move them in another company and try again:\n"
                    "- %s") % (
                        company.name,
                        '\n- '.join([x.name for x in conflict_users])))
