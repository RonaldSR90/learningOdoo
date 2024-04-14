# -*- coding: utf-8 -*-

from odoo import models, fields

# Profesores

class profesor(models.Model):
    _name = 'escuela.profesor'
    _description = 'profesor'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripcion")
    edad = fields.Integer(string="Edad", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    saldo = fields.Float(string="Saldo")
    estado = fields.Boolean(string="Estado del Profesor")
    grado = fields.Selection(
        [
            ("primaria", "Primaria"),
            ("secundaria", "Secundaria"),
        ],
        string="Grado",
        default="primaria",
        required=True,
    )
    alumno = fields.One2many("escuela.alumno", inverse_name="profesor", string="Alumnos")
    materia = fields.Many2many(
        comodel_name="escuela.materia",
        relation_name = "escuela_materias",
        column1="escuela_id",
        column2="materia_id",
    )

# Alumnos

class alumno(models.Model):
    _name = 'escuela.alumno'
    _description = 'alumno'

    name = fields.Char(string="Nombre", required=True)
    profesor = fields.Many2one("escuela.profesor")

# Materias

class materia(models.Model):
    _name = 'escuela.materia'
    _description = 'materias'

    name = fields.Char(string="Nombre", required=True)
    profesor = fields.Many2many(
        comodel_name="escuela.profesor",
        relation_name = "escuela_materias",
        column1="materia_id",
        column2="escuela_id",        
    )