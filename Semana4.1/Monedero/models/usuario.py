config.conexion_bd import base_de_datos
from sqlalchemy import Column,types,orm
class UsuarioModel(base_de_datos.Model):
    __tablename__="usuarios"
    usuarioId =column(name='id',type_=types.Integer,primary_key=True,
                      unique=True,autoincrement=True,nullable=False)

    usuarioNombre=Column(name='nombre',type_=types.String(45),nullable=False)
    usuarioApellido=Column(name='apellido',type_=types.String(45),nullable=False)
    usuarioCorreo=Column(name='correo',type_=types.String(25),nullable=False)
    usuarioPassword=Column(name='password',type_=types.Text,nullable=False)

    movimientos = orm.relationship('MovimientoModel',backref='movimientoUsuario')
    def __init__ (self ,nombre,apellido,correo,password):
        self.usuarioNombre=nombre
        self.usuarioApellidos=apellido
        self.usuarioCorreo= correo
        # ENCRIPTAR LA PASSWORD
        # SELF.UAUARIOPASSWORD =PASSWORD
