#coding: utf-8

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_S2260_TPLOGRAD = (
    ('A', u'A - Área'),
    ('A V', u'A V - Área Verde'),
    ('AC', u'AC - Acesso'),
    ('ACA', u'ACA - Acampamento'),
    ('ACL', u'ACL - Acesso Local'),
    ('AD', u'AD - Adro'),
    ('AE', u'AE - Área Especial'),
    ('AER', u'AER - Aeroporto'),
    ('AL', u'AL - Alameda'),
    ('AMD', u'AMD - Avenida Marginal Direita'),
    ('AME', u'AME - Avenida Marginal Esquerda'),
    ('AN', u'AN - Anel Viário'),
    ('ANT', u'ANT - Antiga Estrada'),
    ('ART', u'ART - Artéria'),
    ('AT', u'AT - Alto'),
    ('ATL', u'ATL - Atalho'),
    ('AV', u'AV - Avenida'),
    ('AVC', u'AVC - Avenida Contorno'),
    ('AVM', u'AVM - Avenida Marginal'),
    ('AVV', u'AVV - Avenida Velha'),
    ('BAL', u'BAL - Balneário'),
    ('BC', u'BC - Beco'),
    ('BCO', u'BCO - Buraco'),
    ('BEL', u'BEL - Belvedere'),
    ('BL', u'BL - Bloco'),
    ('BLO', u'BLO - Balão'),
    ('BLS', u'BLS - Blocos'),
    ('BLV', u'BLV - Bulevar'),
    ('BSQ', u'BSQ - Bosque'),
    ('BVD', u'BVD - Boulevard'),
    ('BX', u'BX - Baixa'),
    ('C', u'C - Cais'),
    ('CAL', u'CAL - Calçada'),
    ('CAM', u'CAM - Caminho'),
    ('CAN', u'CAN - Canal'),
    ('CH', u'CH - Chácara'),
    ('CHA', u'CHA - Chapadão'),
    ('CIC', u'CIC - Ciclovia'),
    ('CIR', u'CIR - Circular'),
    ('CJ', u'CJ - Conjunto'),
    ('CJM', u'CJM - Conjunto Mutirão'),
    ('CMP', u'CMP - Complexo Viário'),
    ('COL', u'COL - Colônia'),
    ('COM', u'COM - Comunidade'),
    ('CON', u'CON - Condomínio'),
    ('COR', u'COR - Corredor'),
    ('CPO', u'CPO - Campo'),
    ('CRG', u'CRG - Córrego'),
    ('CTN', u'CTN - Contorno'),
    ('DSC', u'DSC - Descida'),
    ('DSV', u'DSV - Desvio'),
    ('DT', u'DT - Distrito'),
    ('EB', u'EB - Entre Bloco'),
    ('EIM', u'EIM - Estrada Intermunicipal'),
    ('ENS', u'ENS - Enseada'),
    ('ENT', u'ENT - Entrada Particular'),
    ('EQ', u'EQ - Entre Quadra'),
    ('ESC', u'ESC - Escada'),
    ('ESD', u'ESD - Escadaria'),
    ('ESE', u'ESE - Estrada Estadual'),
    ('ESI', u'ESI - Estrada Vicinal'),
    ('ESL', u'ESL - Estrada de Ligação'),
    ('ESM', u'ESM - Estrada Municipal'),
    ('ESP', u'ESP - Esplanada'),
    ('ESS', u'ESS - Estrada de Servidão'),
    ('EST', u'EST - Estrada'),
    ('ESV', u'ESV - Estrada Velha'),
    ('ETA', u'ETA - Estrada Antiga'),
    ('ETC', u'ETC - Estação'),
    ('ETD', u'ETD - Estádio'),
    ('ETN', u'ETN - Estância'),
    ('ETP', u'ETP - Estrada Particular'),
    ('ETT', u'ETT - Estacionamento'),
    ('EVA', u'EVA - Evangélica'),
    ('EVD', u'EVD - Elevada'),
    ('EX', u'EX - Eixo Industrial'),
    ('FAV', u'FAV - Favela'),
    ('FAZ', u'FAZ - Fazenda'),
    ('FER', u'FER - Ferrovia'),
    ('FNT', u'FNT - Fonte'),
    ('FRA', u'FRA - Feira'),
    ('FTE', u'FTE - Forte'),
    ('GAL', u'GAL - Galeria'),
    ('GJA', u'GJA - Granja'),
    ('HAB', u'HAB - Núcleo Habitacional'),
    ('IA', u'IA - Ilha'),
    ('IND', u'IND - Indeterminado'),
    ('IOA', u'IOA - Ilhota'),
    ('JD', u'JD - Jardim'),
    ('JDE', u'JDE - Jardinete'),
    ('LD', u'LD - Ladeira'),
    ('LGA', u'LGA - Lagoa'),
    ('LGO', u'LGO - Lago'),
    ('LOT', u'LOT - Loteamento'),
    ('LRG', u'LRG - Largo'),
    ('LT', u'LT - Lote'),
    ('MER', u'MER - Mercado'),
    ('MNA', u'MNA - Marina'),
    ('MOD', u'MOD - Modulo'),
    ('MRG', u'MRG - Projeção'),
    ('MRO', u'MRO - Morro'),
    ('MTE', u'MTE - Monte'),
    ('NUC', u'NUC - Núcleo'),
    ('NUR', u'NUR - Núcleo Rural'),
    ('OUT', u'OUT - Outeiro'),
    ('PAR', u'PAR - Paralela'),
    ('PAS', u'PAS - Passeio'),
    ('PAT', u'PAT - Pátio'),
    ('PC', u'PC - Praça'),
    ('PCE', u'PCE - Praça de Esportes'),
    ('PDA', u'PDA - Parada'),
    ('PDO', u'PDO - Paradouro'),
    ('PNT', u'PNT - Ponta'),
    ('PR', u'PR - Praia'),
    ('PRL', u'PRL - Prolongamento'),
    ('PRM', u'PRM - Parque Municipal'),
    ('PRQ', u'PRQ - Parque'),
    ('PRR', u'PRR - Parque Residencial'),
    ('PSA', u'PSA - Passarela'),
    ('PSG', u'PSG - Passagem'),
    ('PSP', u'PSP - Passagem de Pedestre'),
    ('PSS', u'PSS - Passagem Subterrânea'),
    ('PTE', u'PTE - Ponte'),
    ('PTO', u'PTO - Porto'),
    ('Q', u'Q - Quadra'),
    ('QTA', u'QTA - Quinta'),
    ('QTS', u'QTS - Quintas'),
    ('R', u'R - Rua'),
    ('R I', u'R I - Rua Integração'),
    ('R L', u'R L - Rua de Ligação'),
    ('R P', u'R P - Rua Particular'),
    ('R V', u'R V - Rua Velha'),
    ('RAM', u'RAM - Ramal'),
    ('RCR', u'RCR - Recreio'),
    ('REC', u'REC - Recanto'),
    ('RER', u'RER - Retiro'),
    ('RES', u'RES - Residencial'),
    ('RET', u'RET - Reta'),
    ('RLA', u'RLA - Ruela'),
    ('RMP', u'RMP - Rampa'),
    ('ROA', u'ROA - Rodo Anel'),
    ('ROD', u'ROD - Rodovia'),
    ('ROT', u'ROT - Rotula'),
    ('RPE', u'RPE - Rua de Pedestre'),
    ('RPR', u'RPR - Margem'),
    ('RTN', u'RTN - Retorno'),
    ('RTT', u'RTT - Rotatória'),
    ('SEG', u'SEG - Segunda Avenida'),
    ('SIT', u'SIT - Sitio'),
    ('SRV', u'SRV - Servidão'),
    ('ST', u'ST - Setor'),
    ('SUB', u'SUB - Subida'),
    ('TCH', u'TCH - Trincheira'),
    ('TER', u'TER - Terminal'),
    ('TR', u'TR - Trecho'),
    ('TRV', u'TRV - Trevo'),
    ('TUN', u'TUN - Túnel'),
    ('TV', u'TV - Travessa'),
    ('TVP', u'TVP - Travessa Particular'),
    ('TVV', u'TVV - Travessa Velha'),
    ('UNI', u'UNI - Unidade'),
    ('V', u'V - Via'),
    ('V C', u'V C - Via Coletora'),
    ('V L', u'V L - Via Local'),
    ('V-E', u'V-E - Via Expressa'),
    ('VAC', u'VAC - Via de Acesso'),
    ('VAL', u'VAL - Vala'),
    ('VCO', u'VCO - Via Costeira'),
    ('VD', u'VD - Viaduto'),
    ('VER', u'VER - Vereda'),
    ('VEV', u'VEV - Via Elevado'),
    ('VL', u'VL - Vila'),
    ('VLA', u'VLA - Viela'),
    ('VLE', u'VLE - Vale'),
    ('VLT', u'VLT - Via Litorânea'),
    ('VPE', u'VPE - Via de Pedestre'),
    ('VRT', u'VRT - Variante'),
    ('ZIG', u'ZIG - Zigue-Zague'),
)

ESTADOS = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AM', u'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', u'Minas Gerais'),
    ('MS', u'Mato Grosso do Sul'),
    ('MT', u'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('RS', u'Rio Grande do Sul'),
    ('SC', u'Santa Catarina'),
    ('SE', u'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', u'Tocantins'),
)

class s2260localTrabInterm(models.Model):
    s2260_evtconvinterm = models.OneToOneField('esocial.s2260evtConvInterm',
        related_name='%(class)s_s2260_evtconvinterm')
    def evento(self): return self.s2260_evtconvinterm.evento()
    tplograd = models.CharField(choices=CHOICES_S2260_TPLOGRAD, max_length=4)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complem = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2260_evtconvinterm) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complem) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2260_localtrabinterm_custom#
    #s2260_localtrabinterm_custom#
    class Meta:
        db_table = r's2260_localtrabinterm'
        managed = True
        ordering = ['s2260_evtconvinterm', 'tplograd', 'dsclograd', 'nrlograd', 'complem', 'bairro', 'cep', 'codmunic', 'uf']


#VIEWS_MODELS
