#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

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

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.s1000.forms import *
from emensageriapro.s1000.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1000_alteracao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1000_alteracao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s1000_alteracao = get_object_or_404(s1000alteracao.objects.using( db_slug ), excluido = False, id = s1000_alteracao_id)
    dados_evento = {}
    if s1000_alteracao_id:
        dados_evento = s1000_alteracao.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s1000_alteracao_apagar'] = 0
            dict_permissoes['s1000_alteracao_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s1000_alteracao), indent=4, sort_keys=True, default=str)
            s1000alteracao.objects.using( db_slug ).filter(id = s1000_alteracao_id).delete()
            #s1000_alteracao_apagar_custom
            #s1000_alteracao_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's1000_alteracao', s1000_alteracao_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's1000_alteracao_salvar':
            return redirect('s1000_alteracao', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,

        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 's1000_alteracao_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class s1000alteracaoList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s1000alteracao.objects.using(db_slug).all()
    serializer_class = s1000alteracaoSerializer
    permission_classes = (IsAdminUser,)


class s1000alteracaoDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s1000alteracao.objects.using(db_slug).all()
    serializer_class = s1000alteracaoSerializer
    permission_classes = (IsAdminUser,)


def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s1000_alteracao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1000_alteracao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_classtrib': 1,
            'show_contato': 0,
            'show_cpfctt': 1,
            'show_email': 0,
            'show_fimvalid': 0,
            'show_fonecel': 0,
            'show_fonefixo': 0,
            'show_ideperiodo': 0,
            'show_indconstr': 0,
            'show_indcoop': 0,
            'show_inddesfolha': 1,
            'show_indented': 0,
            'show_indett': 1,
            'show_indopccp': 0,
            'show_indoptregeletron': 1,
            'show_infocadastro': 0,
            'show_inivalid': 1,
            'show_natjurid': 0,
            'show_nmctt': 1,
            'show_nmrazao': 1,
            'show_nrregett': 0,
            'show_s1000_evtinfoempregador': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'classtrib__icontains': 'classtrib__icontains',
                'contato': 'contato',
                'cpfctt__icontains': 'cpfctt__icontains',
                'email__icontains': 'email__icontains',
                'fimvalid__icontains': 'fimvalid__icontains',
                'fonecel__icontains': 'fonecel__icontains',
                'fonefixo__icontains': 'fonefixo__icontains',
                'ideperiodo': 'ideperiodo',
                'indconstr': 'indconstr',
                'indcoop': 'indcoop',
                'inddesfolha': 'inddesfolha',
                'indented__icontains': 'indented__icontains',
                'indett__icontains': 'indett__icontains',
                'indopccp': 'indopccp',
                'indoptregeletron': 'indoptregeletron',
                'infocadastro': 'infocadastro',
                'inivalid__icontains': 'inivalid__icontains',
                'natjurid__icontains': 'natjurid__icontains',
                'nmctt__icontains': 'nmctt__icontains',
                'nmrazao__icontains': 'nmrazao__icontains',
                'nrregett__icontains': 'nrregett__icontains',
                's1000_evtinfoempregador': 's1000_evtinfoempregador',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'classtrib__icontains': 'classtrib__icontains',
                'contato': 'contato',
                'cpfctt__icontains': 'cpfctt__icontains',
                'email__icontains': 'email__icontains',
                'fimvalid__icontains': 'fimvalid__icontains',
                'fonecel__icontains': 'fonecel__icontains',
                'fonefixo__icontains': 'fonefixo__icontains',
                'ideperiodo': 'ideperiodo',
                'indconstr': 'indconstr',
                'indcoop': 'indcoop',
                'inddesfolha': 'inddesfolha',
                'indented__icontains': 'indented__icontains',
                'indett__icontains': 'indett__icontains',
                'indopccp': 'indopccp',
                'indoptregeletron': 'indoptregeletron',
                'infocadastro': 'infocadastro',
                'inivalid__icontains': 'inivalid__icontains',
                'natjurid__icontains': 'natjurid__icontains',
                'nmctt__icontains': 'nmctt__icontains',
                'nmrazao__icontains': 'nmrazao__icontains',
                'nrregett__icontains': 'nrregett__icontains',
                's1000_evtinfoempregador': 's1000_evtinfoempregador',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s1000_alteracao_lista = s1000alteracao.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s1000_alteracao_lista) > 100:
            filtrar = True
            s1000_alteracao_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #s1000_alteracao_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1000_alteracao'
        context = {
            's1000_alteracao_lista': s1000_alteracao_lista,
  
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,

        }
        if for_print in (0,1):
            return render(request, 's1000_alteracao_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1000_alteracao_listar.html',
                filename="s1000_alteracao.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('s1000_alteracao_listar.html', context)
            filename = "s1000_alteracao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s1000_alteracao_csv.html', context)
            filename = "s1000_alteracao.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
    else:
        context = {
            'usuario': usuario,
  
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s1000_alteracao_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1000_alteracao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s1000_alteracao_id:
        s1000_alteracao = get_object_or_404(s1000alteracao.objects.using( db_slug ), excluido = False, id = s1000_alteracao_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if s1000_alteracao_id:
        dados_evento = s1000_alteracao.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s1000_alteracao_apagar'] = 0
            dict_permissoes['s1000_alteracao_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s1000_alteracao_id:
            s1000_alteracao_form = form_s1000_alteracao(request.POST or None, instance = s1000_alteracao, slug = db_slug)
        else:
            s1000_alteracao_form = form_s1000_alteracao(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if s1000_alteracao_form.is_valid():
                dados = s1000_alteracao_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s1000_alteracao_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s1000_alteracao_campos_multiple_passo1
                        s1000alteracao.objects.using(db_slug).filter(id=s1000_alteracao_id).update(**dados)
                        obj = s1000alteracao.objects.using(db_slug).get(id=s1000_alteracao_id)
                        #s1000_alteracao_editar_custom
                        #s1000_alteracao_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s1000_alteracao), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's1000_alteracao', s1000_alteracao_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s1000_alteracao_cadastrar_campos_multiple_passo1
                    obj = s1000alteracao(**dados)
                    obj.save(using = db_slug)
                    #s1000_alteracao_cadastrar_custom
                    #s1000_alteracao_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's1000_alteracao', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('s1000_alteracao_apagar', 's1000_alteracao_salvar', 's1000_alteracao'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if s1000_alteracao_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('s1000_alteracao_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s1000_alteracao_form = disabled_form_fields(s1000_alteracao_form, permissao.permite_editar)
        if s1000_alteracao_id:
            if dados_evento['status'] != 0:
                s1000_alteracao_form = disabled_form_fields(s1000_alteracao_form, 0)
        #s1000_alteracao_campos_multiple_passo3

        for field in s1000_alteracao_form.fields.keys():
            s1000_alteracao_form.fields[field].widget.attrs['ng-model'] = 's1000_alteracao_'+field
        if int(dict_hash['print']):
            s1000_alteracao_form = disabled_form_for_print(s1000_alteracao_form)

        s1000_alteracao_dadosisencao_form = None
        s1000_alteracao_dadosisencao_lista = None
        s1000_alteracao_infoop_form = None
        s1000_alteracao_infoop_lista = None
        s1000_alteracao_infoorginternacional_form = None
        s1000_alteracao_infoorginternacional_lista = None
        s1000_alteracao_softwarehouse_form = None
        s1000_alteracao_softwarehouse_lista = None
        s1000_alteracao_situacaopj_form = None
        s1000_alteracao_situacaopj_lista = None
        s1000_alteracao_situacaopf_form = None
        s1000_alteracao_situacaopf_lista = None
        s1000_alteracao_novavalidade_form = None
        s1000_alteracao_novavalidade_lista = None
        if s1000_alteracao_id:
            s1000_alteracao = get_object_or_404(s1000alteracao.objects.using( db_slug ), excluido = False, id = s1000_alteracao_id)

            s1000_alteracao_dadosisencao_form = form_s1000_alteracao_dadosisencao(initial={ 's1000_alteracao': s1000_alteracao }, slug=db_slug)
            s1000_alteracao_dadosisencao_form.fields['s1000_alteracao'].widget.attrs['readonly'] = True
            s1000_alteracao_dadosisencao_lista = s1000alteracaodadosIsencao.objects.using( db_slug ).filter(excluido = False, s1000_alteracao_id=s1000_alteracao.id).all()
            s1000_alteracao_infoop_form = form_s1000_alteracao_infoop(initial={ 's1000_alteracao': s1000_alteracao }, slug=db_slug)
            s1000_alteracao_infoop_form.fields['s1000_alteracao'].widget.attrs['readonly'] = True
            s1000_alteracao_infoop_lista = s1000alteracaoinfoOP.objects.using( db_slug ).filter(excluido = False, s1000_alteracao_id=s1000_alteracao.id).all()
            s1000_alteracao_infoorginternacional_form = form_s1000_alteracao_infoorginternacional(initial={ 's1000_alteracao': s1000_alteracao }, slug=db_slug)
            s1000_alteracao_infoorginternacional_form.fields['s1000_alteracao'].widget.attrs['readonly'] = True
            s1000_alteracao_infoorginternacional_lista = s1000alteracaoinfoOrgInternacional.objects.using( db_slug ).filter(excluido = False, s1000_alteracao_id=s1000_alteracao.id).all()
            s1000_alteracao_softwarehouse_form = form_s1000_alteracao_softwarehouse(initial={ 's1000_alteracao': s1000_alteracao }, slug=db_slug)
            s1000_alteracao_softwarehouse_form.fields['s1000_alteracao'].widget.attrs['readonly'] = True
            s1000_alteracao_softwarehouse_lista = s1000alteracaosoftwareHouse.objects.using( db_slug ).filter(excluido = False, s1000_alteracao_id=s1000_alteracao.id).all()
            s1000_alteracao_situacaopj_form = form_s1000_alteracao_situacaopj(initial={ 's1000_alteracao': s1000_alteracao }, slug=db_slug)
            s1000_alteracao_situacaopj_form.fields['s1000_alteracao'].widget.attrs['readonly'] = True
            s1000_alteracao_situacaopj_lista = s1000alteracaosituacaoPJ.objects.using( db_slug ).filter(excluido = False, s1000_alteracao_id=s1000_alteracao.id).all()
            s1000_alteracao_situacaopf_form = form_s1000_alteracao_situacaopf(initial={ 's1000_alteracao': s1000_alteracao }, slug=db_slug)
            s1000_alteracao_situacaopf_form.fields['s1000_alteracao'].widget.attrs['readonly'] = True
            s1000_alteracao_situacaopf_lista = s1000alteracaosituacaoPF.objects.using( db_slug ).filter(excluido = False, s1000_alteracao_id=s1000_alteracao.id).all()
            s1000_alteracao_novavalidade_form = form_s1000_alteracao_novavalidade(initial={ 's1000_alteracao': s1000_alteracao }, slug=db_slug)
            s1000_alteracao_novavalidade_form.fields['s1000_alteracao'].widget.attrs['readonly'] = True
            s1000_alteracao_novavalidade_lista = s1000alteracaonovaValidade.objects.using( db_slug ).filter(excluido = False, s1000_alteracao_id=s1000_alteracao.id).all()
        else:
            s1000_alteracao = None
        #s1000_alteracao_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's1000_alteracao' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1000_alteracao_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s1000_alteracao_id, tabela='s1000_alteracao').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's1000_alteracao': s1000_alteracao,
            's1000_alteracao_form': s1000_alteracao_form,
            'mensagem': mensagem,
            's1000_alteracao_id': int(s1000_alteracao_id),
            'usuario': usuario,
  
            'hash': hash,

            's1000_alteracao_dadosisencao_form': s1000_alteracao_dadosisencao_form,
            's1000_alteracao_dadosisencao_lista': s1000_alteracao_dadosisencao_lista,
            's1000_alteracao_infoop_form': s1000_alteracao_infoop_form,
            's1000_alteracao_infoop_lista': s1000_alteracao_infoop_lista,
            's1000_alteracao_infoorginternacional_form': s1000_alteracao_infoorginternacional_form,
            's1000_alteracao_infoorginternacional_lista': s1000_alteracao_infoorginternacional_lista,
            's1000_alteracao_softwarehouse_form': s1000_alteracao_softwarehouse_form,
            's1000_alteracao_softwarehouse_lista': s1000_alteracao_softwarehouse_lista,
            's1000_alteracao_situacaopj_form': s1000_alteracao_situacaopj_form,
            's1000_alteracao_situacaopj_lista': s1000_alteracao_situacaopj_lista,
            's1000_alteracao_situacaopf_form': s1000_alteracao_situacaopf_form,
            's1000_alteracao_situacaopf_lista': s1000_alteracao_situacaopf_lista,
            's1000_alteracao_novavalidade_form': s1000_alteracao_novavalidade_form,
            's1000_alteracao_novavalidade_lista': s1000_alteracao_novavalidade_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1000_alteracao_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's1000_alteracao_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1000_alteracao_salvar.html',
                filename="s1000_alteracao.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('s1000_alteracao_salvar.html', context)
            filename = "s1000_alteracao.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
        context = {
            'usuario': usuario,
  
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

