# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Base Partner Surname",
    "version": "1.1",
    "author": "Tiny, Serpent Consulting Services,Odoo Community Association",
    "website": "http://www.openerp.com",
    "category": "Generic Modules/Base",
    "description": """
This module is used for separate surname from contact name of partner. Now You
can give first name & last name on contact Name.
This module is deprecated, it is highly recommended to use base_contact instead.

    """,
    "depends": ["base"],
    "init_xml": [],
    "demo_xml": [],
    "update_xml": ["partner_view.xml"],
    "installable": True,
    "auto_install": False
}
