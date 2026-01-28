#!/usr/bin/env python3
"""
JBF Capital - Gerador de Pitch Deck
Gera apresentação PowerPoint baseada na identidade visual e storytelling definidos
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Cores da Identidade Visual JBF Capital
class JBFColors:
    PRIMARY = RGBColor(102, 126, 234)  # #667EEA
    SECONDARY = RGBColor(118, 75, 162)  # #764BA2
    DARK_SLATE = RGBColor(30, 41, 59)   # #1E293B
    SLATE_GRAY = RGBColor(100, 116, 139)  # #64748B
    COOL_GRAY = RGBColor(71, 85, 105)   # #475569
    LIGHT_SLATE = RGBColor(148, 163, 184)  # #94A3B8
    WHITE = RGBColor(255, 255, 255)
    LIGHT_BG = RGBColor(248, 250, 252)  # #F8FAFC
    BORDER_GRAY = RGBColor(226, 232, 240)  # #E2E8F0
    SUCCESS_GREEN = RGBColor(16, 185, 129)  # #10B981
    WARNING_ORANGE = RGBColor(245, 158, 11)  # #F59E0B
    ERROR_RED = RGBColor(239, 68, 68)  # #EF4444

def apply_gradient_background(slide, color1, color2):
    """Aplica gradiente de fundo ao slide"""
    background = slide.background
    fill = background.fill
    fill.gradient()
    fill.gradient_angle = 135.0
    fill.gradient_stops[0].color.rgb = color1
    fill.gradient_stops[1].color.rgb = color2

def add_footer(slide, text, slide_number, prs):
    """Adiciona rodapé padrão ao slide"""
    # Logo placeholder (texto por enquanto)
    left = Inches(0.5)
    top = Inches(7)
    width = Inches(1.5)
    height = Inches(0.3)
    
    footer_left = slide.shapes.add_textbox(left, top, width, height)
    text_frame = footer_left.text_frame
    text_frame.text = "JBF Capital"
    p = text_frame.paragraphs[0]
    p.font.size = Pt(10)
    p.font.color.rgb = JBFColors.SLATE_GRAY
    p.font.bold = True
    
    # Título da apresentação (centro)
    center_left = Inches(2.5)
    center_width = Inches(5)
    footer_center = slide.shapes.add_textbox(center_left, top, center_width, height)
    text_frame = footer_center.text_frame
    text_frame.text = text
    p = text_frame.paragraphs[0]
    p.font.size = Pt(10)
    p.font.color.rgb = JBFColors.LIGHT_SLATE
    p.alignment = PP_ALIGN.CENTER
    
    # Número do slide (direita)
    right_left = Inches(8.5)
    right_width = Inches(1)
    footer_right = slide.shapes.add_textbox(right_left, top, right_width, height)
    text_frame = footer_right.text_frame
    text_frame.text = str(slide_number)
    p = text_frame.paragraphs[0]
    p.font.size = Pt(10)
    p.font.color.rgb = JBFColors.SLATE_GRAY
    p.alignment = PP_ALIGN.RIGHT

def add_title(slide, title_text, subtitle_text=None, color=None):
    """Adiciona título ao slide"""
    left = Inches(0.7)
    top = Inches(0.5)
    width = Inches(8.6)
    height = Inches(1.2)
    
    title_box = slide.shapes.add_textbox(left, top, width, height)
    text_frame = title_box.text_frame
    text_frame.text = title_text
    
    p = text_frame.paragraphs[0]
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = color if color else JBFColors.DARK_SLATE
    
    if subtitle_text:
        p = text_frame.add_paragraph()
        p.text = subtitle_text
        p.font.size = Pt(18)
        p.font.color.rgb = JBFColors.SLATE_GRAY
        p.space_before = Pt(10)

def add_bullet_points(slide, items, left, top, width, height):
    """Adiciona lista de pontos ao slide"""
    text_box = slide.shapes.add_textbox(left, top, width, height)
    text_frame = text_box.text_frame
    text_frame.word_wrap = True
    
    for i, item in enumerate(items):
        if i == 0:
            p = text_frame.paragraphs[0]
        else:
            p = text_frame.add_paragraph()
        
        p.text = item
        p.font.size = Pt(16)
        p.font.color.rgb = JBFColors.COOL_GRAY
        p.level = 0
        p.space_after = Pt(12)

def create_slide_1_capa(prs):
    """Slide 1: Capa"""
    slide_layout = prs.slide_layouts[6]  # Blank layout
    slide = prs.slides.add_slide(slide_layout)
    
    # Aplicar gradiente de fundo
    apply_gradient_background(slide, JBFColors.PRIMARY, JBFColors.SECONDARY)
    
    # Título principal
    left = Inches(1)
    top = Inches(2.5)
    width = Inches(8)
    height = Inches(2)
    
    title_box = slide.shapes.add_textbox(left, top, width, height)
    text_frame = title_box.text_frame
    text_frame.text = "JBF CAPITAL"
    
    p = text_frame.paragraphs[0]
    p.font.size = Pt(54)
    p.font.bold = True
    p.font.color.rgb = JBFColors.WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Subtítulo
    p = text_frame.add_paragraph()
    p.text = "Democratizando o Acesso ao Crédito"
    p.font.size = Pt(24)
    p.font.color.rgb = JBFColors.WHITE
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(20)
    
    # Tagline
    p = text_frame.add_paragraph()
    p.text = "Conectando pessoas a soluções financeiras inteligentes através de tecnologia e parcerias estratégicas"
    p.font.size = Pt(16)
    p.font.color.rgb = RGBColor(255, 255, 255)  # Branco com transparência visual
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(30)
    
    # Data/versão
    footer_left = Inches(1)
    footer_top = Inches(6.8)
    footer_width = Inches(8)
    footer_height = Inches(0.3)
    
    footer_box = slide.shapes.add_textbox(footer_left, footer_top, footer_width, footer_height)
    text_frame = footer_box.text_frame
    text_frame.text = "Janeiro 2026 • Versão 1.1"
    p = text_frame.paragraphs[0]
    p.font.size = Pt(12)
    p.font.color.rgb = JBFColors.WHITE
    p.alignment = PP_ALIGN.CENTER

def create_slide_2_contexto(prs):
    """Slide 2: Contexto & Oportunidade"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    add_title(slide, "O Mercado de Crédito no Brasil", "Uma oportunidade de R$ 5,4 trilhões")
    
    # Conteúdo
    left = Inches(0.7)
    top = Inches(2)
    width = Inches(4)
    height = Inches(4)
    
    items = [
        "📊 Estoque de crédito: R$ 5,4 trilhões (2024)",
        "⚠️ Apenas 30% da população tem acesso adequado",
        "📈 Crescimento anual de 12-15%",
        "🏠 Home Equity: R$ 500 bi de potencial",
        "🎯 Gap de acesso: 70% da população excluída"
    ]
    add_bullet_points(slide, items, left, top, width, height)
    
    # Box de destaque
    box_left = Inches(5.2)
    box_top = Inches(2.5)
    box_width = Inches(4)
    box_height = Inches(3)
    
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        box_left, box_top, box_width, box_height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(241, 245, 249)
    shape.line.color.rgb = JBFColors.PRIMARY
    shape.line.width = Pt(2)
    
    text_frame = shape.text_frame
    text_frame.text = "OPORTUNIDADE"
    p = text_frame.paragraphs[0]
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = JBFColors.PRIMARY
    p.alignment = PP_ALIGN.CENTER
    
    p = text_frame.add_paragraph()
    p.text = "\nMercado em expansão com alta demanda por soluções digitais e transparentes"
    p.font.size = Pt(16)
    p.font.color.rgb = JBFColors.COOL_GRAY
    p.space_before = Pt(15)
    
    add_footer(slide, "Pitch Deck Institucional", 2, prs)

def create_slide_3_problema(prs):
    """Slide 3: Problema"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    add_title(slide, "Os Desafios do Acesso ao Crédito")
    
    # Grid de problemas
    problems = [
        ("📋", "Burocracia\nExcessiva", "Processos manuais\ne papelada"),
        ("💸", "Juros\nAbusivos", "Taxas até 300%\nsem transparência"),
        ("⏱️", "Processos\nLentos", "30-60 dias para\naprovação"),
        ("🤔", "Falta de\nTransparência", "Taxas ocultas\ne letras miúdas"),
        ("🚫", "Exclusão", "Score baixo =\ncrédito negado")
    ]
    
    x_positions = [0.7, 2.5, 4.3, 6.1, 7.9]
    
    for i, (icon, title, desc) in enumerate(problems):
        left = Inches(x_positions[i])
        top = Inches(2.2)
        width = Inches(1.6)
        height = Inches(3)
        
        # Box
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = JBFColors.LIGHT_BG
        shape.line.color.rgb = JBFColors.BORDER_GRAY
        
        # Conteúdo
        text_frame = shape.text_frame
        text_frame.text = icon
        p = text_frame.paragraphs[0]
        p.font.size = Pt(32)
        p.alignment = PP_ALIGN.CENTER
        
        p = text_frame.add_paragraph()
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = JBFColors.DARK_SLATE
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(10)
        
        p = text_frame.add_paragraph()
        p.text = desc
        p.font.size = Pt(11)
        p.font.color.rgb = JBFColors.SLATE_GRAY
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(8)
    
    # Citação
    quote_left = Inches(1.5)
    quote_top = Inches(5.8)
    quote_width = Inches(7)
    quote_height = Inches(0.8)
    
    quote_box = slide.shapes.add_textbox(quote_left, quote_top, quote_width, quote_height)
    text_frame = quote_box.text_frame
    text_frame.text = '"73% dos brasileiros consideram o processo de obtenção de crédito confuso e demorado"'
    p = text_frame.paragraphs[0]
    p.font.size = Pt(14)
    p.font.italic = True
    p.font.color.rgb = JBFColors.PRIMARY
    p.alignment = PP_ALIGN.CENTER
    
    add_footer(slide, "Pitch Deck Institucional", 3, prs)

def create_slide_4_solucao(prs):
    """Slide 4: Solução"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    add_title(slide, "JBF Capital: Tecnologia + Parcerias = Acesso Simplificado")
    
    # Fluxo
    steps = [
        ("1", "🌐", "Cliente acessa\nplataforma"),
        ("2", "🤖", "Análise\ninteligente"),
        ("3", "🎯", "Matching com\nprodutos ideais"),
        ("4", "✅", "Aprovação\nem 48h"),
        ("5", "📱", "Contrato\ndigital")
    ]
    
    y_pos = 2.5
    
    for i, (num, icon, text) in enumerate(steps):
        left = Inches(0.5 + i * 1.9)
        top = Inches(y_pos)
        width = Inches(1.5)
        height = Inches(2)
        
        # Circle para número
        circle = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            left + Inches(0.4), top - Inches(0.3), Inches(0.7), Inches(0.7)
        )
        circle.fill.solid()
        circle.fill.fore_color.rgb = JBFColors.PRIMARY
        circle.line.color.rgb = JBFColors.PRIMARY
        
        circle_text = circle.text_frame
        circle_text.text = num
        p = circle_text.paragraphs[0]
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = JBFColors.WHITE
        p.alignment = PP_ALIGN.CENTER
        circle_text.vertical_anchor = MSO_ANCHOR.MIDDLE
        
        # Box
        box = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height
        )
        box.fill.solid()
        box.fill.fore_color.rgb = JBFColors.LIGHT_BG
        box.line.color.rgb = JBFColors.PRIMARY
        box.line.width = Pt(1.5)
        
        text_frame = box.text_frame
        text_frame.text = icon
        p = text_frame.paragraphs[0]
        p.font.size = Pt(28)
        p.alignment = PP_ALIGN.CENTER
        
        p = text_frame.add_paragraph()
        p.text = text
        p.font.size = Pt(12)
        p.font.color.rgb = JBFColors.DARK_SLATE
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(8)
        
        # Seta (exceto no último)
        if i < len(steps) - 1:
            arrow_left = left + width + Inches(0.05)
            arrow_top = top + Inches(0.8)
            arrow = slide.shapes.add_textbox(arrow_left, arrow_top, Inches(0.3), Inches(0.4))
            arrow.text_frame.text = "→"
            arrow.text_frame.paragraphs[0].font.size = Pt(24)
            arrow.text_frame.paragraphs[0].font.color.rgb = JBFColors.PRIMARY
            arrow.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    
    # Box resultado
    result_left = Inches(1.5)
    result_top = Inches(5.2)
    result_width = Inches(7)
    result_height = Inches(0.8)
    
    result_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        result_left, result_top, result_width, result_height
    )
    result_box.fill.solid()
    result_box.fill.fore_color.rgb = JBFColors.PRIMARY
    result_box.line.fill.background()
    
    text_frame = result_box.text_frame
    text_frame.text = "Resultado: Experiência simples, rápida e transparente"
    p = text_frame.paragraphs[0]
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = JBFColors.WHITE
    p.alignment = PP_ALIGN.CENTER
    text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    
    add_footer(slide, "Pitch Deck Institucional", 4, prs)

def create_slide_9_arquitetura_tecnica(prs):
    """Slide 9: Arquitetura Técnica"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    add_title(slide, "Arquitetura Técnica", "Escalável, Segura e Cloud-Native")
    
    # Camadas de arquitetura
    layers = [
        ("🌐 Apresentação", ["Web App (React)", "Mobile (React Native)", "Portal Parceiros"]),
        ("🔐 API Gateway", ["OAuth 2.0", "Rate Limiting", "Load Balancer"]),
        ("⚙️ Microserviços", ["Usuários", "Crédito", "Integração", "Notificações"]),
        ("🗄️ Dados", ["PostgreSQL", "MongoDB", "Redis", "ElasticSearch"]),
        ("☁️ Infraestrutura", ["AWS Cloud", "Docker/K8s", "CI/CD"])
    ]
    
    for i, (layer_name, components) in enumerate(layers):
        top = Inches(2.0 + i * 0.9)
        left = Inches(0.7)
        width = Inches(5.5)
        height = Inches(0.7)
        
        # Box da camada
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height
        )
        shape.fill.solid()
        color_intensity = 30 + i * 20
        r_val = min(255, 102 + color_intensity)
        g_val = min(255, 126 + color_intensity)
        b_val = 234
        shape.fill.fore_color.rgb = RGBColor(r_val, g_val, b_val)
        shape.line.fill.background()
        
        text_frame = shape.text_frame
        text_frame.text = f"{layer_name}\n{' • '.join(components)}"
        p = text_frame.paragraphs[0]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = JBFColors.WHITE
        
        if len(text_frame.paragraphs) > 1:
            text_frame.paragraphs[1].font.size = Pt(9)
            text_frame.paragraphs[1].font.color.rgb = JBFColors.WHITE
    
    # Destaques técnicos
    highlights_left = Inches(6.5)
    highlights_top = Inches(2.0)
    highlights_width = Inches(3)
    highlights_height = Inches(4.5)
    
    highlights_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        highlights_left, highlights_top, highlights_width, highlights_height
    )
    highlights_box.fill.solid()
    highlights_box.fill.fore_color.rgb = JBFColors.LIGHT_BG
    highlights_box.line.color.rgb = JBFColors.SUCCESS_GREEN
    highlights_box.line.width = Pt(2)
    
    text_frame = highlights_box.text_frame
    text_frame.text = "DESTAQUES TÉCNICOS"
    p = text_frame.paragraphs[0]
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = JBFColors.SUCCESS_GREEN
    p.alignment = PP_ALIGN.CENTER
    
    highlights = [
        "✅ Uptime: 99.9%",
        "✅ Latência: < 200ms",
        "✅ Escalabilidade horizontal",
        "✅ Backup 3x/dia",
        "✅ PCI-DSS & ISO 27001"
    ]
    
    for highlight in highlights:
        p = text_frame.add_paragraph()
        p.text = highlight
        p.font.size = Pt(12)
        p.font.color.rgb = JBFColors.COOL_GRAY
        p.space_before = Pt(8)
    
    add_footer(slide, "Pitch Deck Institucional", 9, prs)

def create_slide_10_arquitetura_integracao(prs):
    """Slide 10: Arquitetura de Integração"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    add_title(slide, "Arquitetura de Integração", "API RESTful - Integração em 30 dias")
    
    # Fluxo de integração
    flow_text = """
    Cliente → JBF Platform → API Gateway → Parceiros (Creditas, BV, Bradesco)
                                ↓
                        Motor de Crédito
                                ↓
                        Proposta ao Cliente
    """
    
    flow_left = Inches(0.7)
    flow_top = Inches(2.2)
    flow_width = Inches(8.6)
    flow_height = Inches(2.5)
    
    flow_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        flow_left, flow_top, flow_width, flow_height
    )
    flow_box.fill.solid()
    flow_box.fill.fore_color.rgb = RGBColor(245, 247, 250)
    flow_box.line.color.rgb = JBFColors.PRIMARY
    flow_box.line.width = Pt(2)
    
    text_frame = flow_box.text_frame
    text_frame.text = "FLUXO DE INTEGRAÇÃO"
    p = text_frame.paragraphs[0]
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = JBFColors.PRIMARY
    p.alignment = PP_ALIGN.CENTER
    
    p = text_frame.add_paragraph()
    p.text = "\n1. Solicitação do Cliente"
    p.font.size = Pt(12)
    p.font.color.rgb = JBFColors.DARK_SLATE
    
    p = text_frame.add_paragraph()
    p.text = "2. Validação e Roteamento JBF"
    p.font.size = Pt(12)
    p.font.color.rgb = JBFColors.DARK_SLATE
    
    p = text_frame.add_paragraph()
    p.text = "3. Integração com Parceiros via API"
    p.font.size = Pt(12)
    p.font.color.rgb = JBFColors.DARK_SLATE
    
    p = text_frame.add_paragraph()
    p.text = "4. Scoring e Matching Inteligente"
    p.font.size = Pt(12)
    p.font.color.rgb = JBFColors.DARK_SLATE
    
    p = text_frame.add_paragraph()
    p.text = "5. Entrega da Proposta"
    p.font.size = Pt(12)
    p.font.color.rgb = JBFColors.DARK_SLATE
    
    # Benefícios
    benefits = [
        "⚡ Integração em 30 dias (vs. 6 meses)",
        "🔌 Plug-and-play para parceiros",
        "📡 API RESTful + OpenAPI",
        "🔄 Webhooks em tempo real",
        "🧪 Sandbox para testes",
        "📊 Dashboard de monitoramento"
    ]
    
    benefits_left = Inches(0.7)
    benefits_top = Inches(5.0)
    benefits_width = Inches(8.6)
    benefits_height = Inches(1.5)
    
    for i, benefit in enumerate(benefits):
        col = i % 3
        row = i // 3
        
        b_left = benefits_left + col * Inches(2.9)
        b_top = benefits_top + row * Inches(0.5)
        b_width = Inches(2.7)
        b_height = Inches(0.4)
        
        benefit_box = slide.shapes.add_textbox(b_left, b_top, b_width, b_height)
        text_frame = benefit_box.text_frame
        text_frame.text = benefit
        p = text_frame.paragraphs[0]
        p.font.size = Pt(11)
        p.font.color.rgb = JBFColors.SUCCESS_GREEN
        p.font.bold = True
    
    add_footer(slide, "Pitch Deck Institucional", 10, prs)

def create_slide_11_valores(prs):
    """Slide 11: Valores da Empresa"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    add_title(slide, "Nossos Valores e Cultura")
    
    # Grid de valores
    valores = [
        ("🎯", "FOCO NO CLIENTE", "Cliente no centro\nde todas decisões"),
        ("🤝", "TRANSPARÊNCIA", "Comunicação clara\ne honesta"),
        ("🚀", "INOVAÇÃO", "Tecnologia como\ndiferencial"),
        ("💼", "EXCELÊNCIA", "Qualidade em\ncada entrega"),
        ("🌱", "CRESCIMENTO\nSUSTENTÁVEL", "Impacto positivo\nde longo prazo")
    ]
    
    positions = [
        (0.7, 2.0), (3.4, 2.0), (6.1, 2.0),
        (2.0, 4.2), (4.7, 4.2)
    ]
    
    for i, (icon, title, desc) in enumerate(valores):
        if i >= len(positions):
            break
            
        left = Inches(positions[i][0])
        top = Inches(positions[i][1])
        width = Inches(2.4)
        height = Inches(1.8)
        
        # Box
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = JBFColors.PRIMARY
        shape.line.fill.background()
        
        # Conteúdo
        text_frame = shape.text_frame
        text_frame.text = icon
        p = text_frame.paragraphs[0]
        p.font.size = Pt(32)
        p.alignment = PP_ALIGN.CENTER
        
        p = text_frame.add_paragraph()
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = JBFColors.WHITE
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(8)
        
        p = text_frame.add_paragraph()
        p.text = desc
        p.font.size = Pt(10)
        p.font.color.rgb = JBFColors.WHITE
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(5)
    
    # Missão e Visão
    mission_left = Inches(0.7)
    mission_top = Inches(6.3)
    mission_width = Inches(8.6)
    mission_height = Inches(0.35)
    
    mission_box = slide.shapes.add_textbox(mission_left, mission_top, mission_width, mission_height)
    text_frame = mission_box.text_frame
    text_frame.text = "Missão: Democratizar o acesso ao crédito através de tecnologia, transparência e parcerias"
    p = text_frame.paragraphs[0]
    p.font.size = Pt(11)
    p.font.color.rgb = JBFColors.PRIMARY
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    
    add_footer(slide, "Pitch Deck Institucional", 11, prs)

def create_slide_12_valor_agregado(prs):
    """Slide 12: Valor Agregado ao Cliente"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    add_title(slide, "Valor Agregado ao Cliente", "Impacto Real na Vida das Pessoas")
    
    # Tabela comparativa (simulada com text boxes)
    headers = ["Aspecto", "Tradicional", "JBF Capital", "Benefício"]
    rows = [
        ["Taxa de Juros", "2,5% a.m.", "1,2% a.m.", "52% menor"],
        ["Aprovação", "30-60 dias", "48 horas", "15-30x mais rápido"],
        ["Processo", "Presencial", "100% digital", "Total comodidade"],
        ["Transparência", "Taxas ocultas", "Tudo às claras", "Sem surpresas"],
        ["Suporte", "Comercial", "24/7", "Sempre disponível"]
    ]
    
    # Headers
    header_top = Inches(2.2)
    col_widths = [Inches(2.2), Inches(2.0), Inches(2.0), Inches(2.0)]
    
    for i, header in enumerate(headers):
        left = Inches(0.7) + sum(col_widths[:i])
        width = col_widths[i]
        
        header_box = slide.shapes.add_textbox(left, header_top, width, Inches(0.4))
        text_frame = header_box.text_frame
        text_frame.text = header
        p = text_frame.paragraphs[0]
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = JBFColors.WHITE
        p.alignment = PP_ALIGN.CENTER
        
        # Background
        bg = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            left, header_top, width, Inches(0.4)
        )
        bg.fill.solid()
        bg.fill.fore_color.rgb = JBFColors.PRIMARY
        bg.line.fill.background()
        bg.z_order = 0
        header_box.z_order = 1
    
    # Rows
    for row_idx, row_data in enumerate(rows):
        row_top = Inches(2.7 + row_idx * 0.5)
        
        for col_idx, cell_data in enumerate(row_data):
            left = Inches(0.7) + sum(col_widths[:col_idx])
            width = col_widths[col_idx]
            
            cell_box = slide.shapes.add_textbox(left, row_top, width, Inches(0.4))
            text_frame = cell_box.text_frame
            text_frame.text = cell_data
            p = text_frame.paragraphs[0]
            p.font.size = Pt(10)
            p.font.color.rgb = JBFColors.COOL_GRAY
            p.alignment = PP_ALIGN.CENTER
            
            if col_idx == 3:  # Coluna de benefício
                p.font.color.rgb = JBFColors.SUCCESS_GREEN
                p.font.bold = True
    
    # Testemunhos
    testimonials = [
        ("Maria S.", "Empresária", "R$ 200k em 2 dias.\nEconomizei R$ 40k"),
        ("Carlos A.", "Proprietário", "Home Equity com\ntaxa 60% menor"),
        ("Ana L.", "Autônoma", "Aprovada com\nanálise justa")
    ]
    
    for i, (name, role, text) in enumerate(testimonials):
        left = Inches(0.7 + i * 3.0)
        top = Inches(5.2)
        width = Inches(2.7)
        height = Inches(1.3)
        
        box = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height
        )
        box.fill.solid()
        box.fill.fore_color.rgb = JBFColors.LIGHT_BG
        box.line.color.rgb = JBFColors.PRIMARY
        
        text_frame = box.text_frame
        text_frame.text = f'"{text}"'
        p = text_frame.paragraphs[0]
        p.font.size = Pt(10)
        p.font.italic = True
        p.font.color.rgb = JBFColors.COOL_GRAY
        
        p = text_frame.add_paragraph()
        p.text = f"\n— {name}, {role}"
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = JBFColors.PRIMARY
        p.space_before = Pt(5)
    
    add_footer(slide, "Pitch Deck Institucional", 12, prs)

def create_slide_16_encerramento(prs):
    """Slide 16: Encerramento & Call to Action"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Gradiente suave
    background = slide.background
    fill = background.fill
    fill.gradient()
    fill.gradient_angle = 135.0
    fill.gradient_stops[0].color.rgb = RGBColor(240, 242, 250)
    fill.gradient_stops[1].color.rgb = RGBColor(250, 250, 255)
    
    # Título
    title_left = Inches(1)
    title_top = Inches(1.5)
    title_width = Inches(8)
    title_height = Inches(1.5)
    
    title_box = slide.shapes.add_textbox(title_left, title_top, title_width, title_height)
    text_frame = title_box.text_frame
    text_frame.text = "Vamos Construir o Futuro do Crédito Juntos"
    p = text_frame.paragraphs[0]
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = JBFColors.PRIMARY
    p.alignment = PP_ALIGN.CENTER
    
    # Call to Action
    cta_left = Inches(2)
    cta_top = Inches(3.5)
    cta_width = Inches(6)
    cta_height = Inches(2.5)
    
    cta_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        cta_left, cta_top, cta_width, cta_height
    )
    cta_box.fill.solid()
    cta_box.fill.fore_color.rgb = JBFColors.PRIMARY
    cta_box.line.fill.background()
    
    text_frame = cta_box.text_frame
    text_frame.text = "💼 INVESTIDORES\nRodada Serie A - R$ 20 MM"
    p = text_frame.paragraphs[0]
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = JBFColors.WHITE
    p.alignment = PP_ALIGN.CENTER
    
    p = text_frame.add_paragraph()
    p.text = "\n🤝 PARCEIROS\nIntegração em 30 dias"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = JBFColors.WHITE
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(15)
    
    p = text_frame.add_paragraph()
    p.text = "\n📧 contato@jbfcapital.com.br"
    p.font.size = Pt(16)
    p.font.color.rgb = JBFColors.WHITE
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(20)
    
    # Frase de fechamento
    closing_left = Inches(1)
    closing_top = Inches(6.3)
    closing_width = Inches(8)
    closing_height = Inches(0.5)
    
    closing_box = slide.shapes.add_textbox(closing_left, closing_top, closing_width, closing_height)
    text_frame = closing_box.text_frame
    text_frame.text = "Obrigado pela atenção. Estamos prontos para responder suas perguntas."
    p = text_frame.paragraphs[0]
    p.font.size = Pt(16)
    p.font.color.rgb = JBFColors.DARK_SLATE
    p.alignment = PP_ALIGN.CENTER

def create_presentation():
    """Cria a apresentação completa"""
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    print("Gerando Slide 1: Capa...")
    create_slide_1_capa(prs)
    
    print("Gerando Slide 2: Contexto & Oportunidade...")
    create_slide_2_contexto(prs)
    
    print("Gerando Slide 3: Problema...")
    create_slide_3_problema(prs)
    
    print("Gerando Slide 4: Solução...")
    create_slide_4_solucao(prs)
    
    print("Gerando Slide 9: Arquitetura Técnica...")
    create_slide_9_arquitetura_tecnica(prs)
    
    print("Gerando Slide 10: Arquitetura de Integração...")
    create_slide_10_arquitetura_integracao(prs)
    
    print("Gerando Slide 11: Valores da Empresa...")
    create_slide_11_valores(prs)
    
    print("Gerando Slide 12: Valor Agregado ao Cliente...")
    create_slide_12_valor_agregado(prs)
    
    print("Gerando Slide 16: Encerramento...")
    create_slide_16_encerramento(prs)
    
    # Salvar apresentação
    output_file = "/home/runner/work/jbfCapital-poc/jbfCapital-poc/pitch-deck/JBF_Capital_Pitch_Deck.pptx"
    prs.save(output_file)
    print(f"\n✅ Apresentação gerada com sucesso: {output_file}")
    print(f"📊 Total de slides: {len(prs.slides)}")
    
    return output_file

if __name__ == "__main__":
    print("=" * 60)
    print("JBF CAPITAL - GERADOR DE PITCH DECK")
    print("=" * 60)
    print("\nIniciando geração da apresentação...\n")
    
    output_file = create_presentation()
    
    print("\n" + "=" * 60)
    print("✨ CONCLUÍDO!")
    print("=" * 60)
    print(f"\nArquivo gerado: {output_file}")
    print("\nPróximos passos:")
    print("1. Abra o arquivo .pptx no PowerPoint ou Google Slides")
    print("2. Adicione imagens e logos conforme necessário")
    print("3. Complete os slides restantes (5, 6, 7, 8, 13, 14, 15)")
    print("4. Ajuste cores e formatação conforme preferência")
    print("\nConsulte IDENTIDADE_VISUAL.md e STORYTELLING.md para diretrizes completas.")
