# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime
class topics(models.Model):
    _name='openacademy.topics'
    name=fields.Char(string='Topic Name')
class teachers(models.Model):
     _name = 'openacademy.teacher'
     name=fields.Char(string='First Name')
     lastname = fields.Char(string='Last Name')
     topicsid = fields.Many2many('openacademy.topics', String='Topis Taught')
class academy(models.Model):
    _name = 'openacademy.course'
    name = fields.Char(String='First Name',required=True)
    startdate=fields.Date(String='Start Date',default=datetime.today())
    enddate = fields.Date(String='End Date',default=datetime.today())
    duration = fields.Integer(String='Duration')
    fees=fields.Float(String='Fees')
    seats=fields.Integer(String='Seats Available')
    topicsid = fields.Many2many('openacademy.topics', String='Topics Included')
    @api.onchange('startdate','enddate')
    def calculate_duration(self):
        if self.startdate:

            if self.enddate:
                fmt = '%Y-%m-%d'
                d1 = datetime.strptime(self.startdate, fmt)
                d2 = datetime.strptime(self.enddate, fmt)
                if d1<d2 :
                    daysdiff = str((d2 - d1).days)
                    self.duration=daysdiff
                else:
                    self.duration = 0
                    self.enddate=self.startdate






