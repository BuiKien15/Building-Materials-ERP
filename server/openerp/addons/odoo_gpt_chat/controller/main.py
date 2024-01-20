
from odoo import http
from odoo.http import request

class KitchenScreenBase(http.Controller):

    @http.route('/get/chatbot', type="json", auth="public")
    def _get_chatbot(self):
        whis_settings = request.env['ir.config_parameter'].sudo()
        if whis_settings.get_param('odoo_gpt_chat.chat_bot_id', False) and whis_settings.get_param('odoo_gpt_chat.show_chat_bot', False):
            return {
                'id': whis_settings.get_param('odoo_gpt_chat.chat_bot_id', False), 
                'front_end': whis_settings.get_param('odoo_gpt_chat.show_chat_bot_f', False), 
                'back_end': whis_settings.get_param('odoo_gpt_chat.show_chat_bot_b', False) 
            }
        else:
            return False