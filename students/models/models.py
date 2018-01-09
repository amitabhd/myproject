# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
class students(models.Model):
    _name = 'students.studentdata'
    name = fields.Char(string='Students Name',Required=True)
    dob = fields.Date(string='Date of Birth')
    emailid = fields.Char(string='Email address', Required=True)
    phoneno = fields.Integer(string='Phone No')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),('female', 'Female')], 'Gender', default='male',help="Select your gender.")
    undergraduate = fields.Boolean()
    coursetaken = fields.Many2one('tutorial.course',ondelete='set null',string='Course Taken')
    relatedcontact = fields.Many2one('res.partner',ondelete='set null',string='Related Contacts')

    @api.onchange('relatedcontact')  # if these fields are changed, call method
    def check_change(self):
        contactid = self.relatedcontact
        recordset = self.env['students.studentdata'].search([('relatedcontact','=',contactid.id)])
        self.name = recordset.name
        self.dob = recordset.dob
        self.emailid = recordset.emailid
        self.phoneno=recordset.phoneno
        self.age=recordset.age
        self.gender=recordset.gender
        self.undergraduate=recordset.undergraduate
        self.coursetaken=recordset.coursetaken
    @api.onchange('dob')
    def calc_age(self):
        if self.dob:
            fmt = '%Y-%m-%d'
            birthdate = datetime.strptime(self.dob, fmt)
            currrentyear = datetime.now().year
            currrentmonth = datetime.now().month
            currrentday = datetime.now().day
            currentdate=datetime.now().date
            
            daysdiff= currrentyear - birthdate.year - ((currrentmonth, currrentday) < (birthdate.month, birthdate.day))
            self.age = daysdiff
