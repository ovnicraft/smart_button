# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Cristian Salamea.
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
    'name' : 'smart_button',
    'version' : '0.1.0',
    'author' : 'Cristian Salamea',
    'category': 'Web',
    'complexity': 'normal',
    'website': 'www.ayni.io',
    'description': "Smart button backport 7.0",
    'data': [
    ],
    'depends' : [
        'web'
    ],
    'js': [
        'static/lib/bootstrap/js/bootstrap.min.js',        
        'static/src/js/smart_button.js',
    ],
    'qweb': [
        'static/src/xml/base.xml'
    ],
    'css': [
        'static/lib/bootstrap/bootstrap.min.css',        
        'static/lib/fontawesome/css/font-awesome.css'
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,                
}
