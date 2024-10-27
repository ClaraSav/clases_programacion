import base64
import io
import xlsxwriter

from odoo import fields, models, api


class ReportWizard(models.TransientModel):
    _name = 'report.wizard'
    _description = 'Wizard for report xlsx'

    date_start = fields.Date(string="Date Start", required=True)
    date_end = fields.Date(string="Date End")
    content = fields.Binary(string="File")

    def _get_data(self):
        lang = self.env.user.lang

        query = """
            WITH vats_temp AS (
                SELECT 
                id,
                REGEXP_REPLACE(vat, '[^0-9]', '', 'g')     AS vat
                FROM res_partner
            )
            
            
            
        
            SELECT 
                partner.name                    AS name,
                vats_temp.vat                   AS vat,
                COALESCE(template.name::json->%s, template.name::json->'en_US')      AS product_name,
                AVG(mline.price_unit)                AS price,
                SUM(mline.quantity)                  AS quantity,
                CASE 
                    WHEN SUM(mline.quantity) >= 10 THEN 'VIP'
                    ELSE 'CLIENTE TACAÑO' 
                END                             AS type_customer
                
            FROM account_move_line mline
            LEFT JOIN res_partner partner    ON partner.id = mline.partner_id
            JOIN product_product product ON product.id = mline.product_id
            JOIN product_template template ON template.id = product.product_tmpl_id
            JOIN vats_temp ON vats_temp.id = partner.id
            
            WHERE mline.price_unit <> 0
            GROUP BY partner.name, template.name, vats_temp.vat
            HAVING SUM(mline.quantity) <= 100
            
        """
        self.env.cr.execute(query, (lang,))
        results = self.env.cr.dictfetchall()
        return results

    def action_print(self):
        data = self._get_data()

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Sheet')
        report_format = workbook.add_format({'border': 1, 'bold': True, 'font_size': 9, 'font_name': 'Calibri'})

        row = 0
        for line in data:
            col = 0
            for field in line:
                sheet.write(row, col, line[field], report_format)
                col += 1

            row += 1

        workbook.close()
        xlsx_data = output.getvalue()

        self.write({'content': base64.encodebytes(xlsx_data)})

        return {
            'type': 'ir.actions.act_url',
            'url': 'web/content/?model={}&field=content&download=true&id={}&filename=archivo.xlsx'.format(
                self._name, self.id),
        }