# -*- coding: utf-8 -*-
from collections import namedtuple
import json
import time

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_round, float_compare, float_is_zero
from datetime import datetime, timedelta

class task1_task1(models.Model):
    _name = 'task.task1'
    name = fields.Char(string='Name', required=True)
    number = fields.Integer(string='Number')
    binary = fields.Binary(string='Binary')
    boolean = fields.Boolean(string='Boolean')
    ngay = fields.Date(string='Ngay')
    thoigian = fields.Datetime(string='Thoi gian')
    Float = fields.Float(string='Float')
    text = fields.Text(string='Text')
    html = fields.Html(string='HTML')
    gender = fields.Selection([
            ('php','PHP'),
            ('py','Python'),
            ('js','Javascript'),
            ('htmlcss','Html & Css')
        ], string='Gioi tinh', default='js')
    one2many_id = fields.One2many('task.one2many','many2one_id',string='Detail one 2 many')
    many2one_id = fields.Many2one('task.product',string='Many 2 one Selection')
    pro_ids = fields.Many2many('task.product','task_product_rel','task_id','pro_id',string='Many 2 many')
    # detail_ids = fields.One2many('test.detail','id', string='Detail')

# class test_detail(models.Model):
#     _name = 'test.detail'
#     name = fields.Boolean(string='Name?')
#     number = fields.Integer(string='Number')
#     float = fields.Float(string='Float')

class task_one2many(models.Model):
    _name = 'task.one2many'
    product = fields.Char(string='San pham')
    many2one_id = fields.Many2one('task.task1',string='acb')

class task_many2one(models.Model):
    _name = 'task.product'
    _rec_name = 'namepro'
    # name = namepro
    namepro = fields.Char(string='Ten san pham')
    qty = fields.Integer(string='So luong')
    task_ids = fields.Many2many('task.task1','task_product_rel','pro_id','task_id',string='Many 2 many')