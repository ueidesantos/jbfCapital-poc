#!/usr/bin/env python3
"""
JBF Capital - Gerador de Pitch Deck com Imagens
Gera apresentação PowerPoint usando as imagens do diretório imagens_exemplo
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os

# Cores da Identidade Visual JBF Capital
class JBFColors:
    PRIMARY = RGBColor(102, 126, 234)  # #667EEA
    SECONDARY = RGBColor(118, 75, 162)  # #764BA2
    DARK_SLATE = RGBColor(30, 41, 59)   # #1E293B
    SLATE_GRAY = RGBColor(100, 116, 139)  # #64748B
    WHITE = RGBColor(255, 255, 255)

def create_presentation_from_images():
    """
    Cria apresentação PowerPoint usando as imagens do diretório imagens_exemplo
    """
    print("=" * 60)
    print("JBF CAPITAL - GERADOR DE PITCH DECK COM IMAGENS")
    print("=" * 60)
    print()
    
    # Criar apresentação com proporção 16:9
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(5.625)
    
    # Diretório com as imagens
    images_dir = "imagens_exemplo"
    
    # Verificar se o diretório existe
    if not os.path.exists(images_dir):
        print(f"❌ Erro: Diretório '{images_dir}' não encontrado!")
        return
    
    # Listar todas as imagens PNG no diretório
    image_files = sorted([f for f in os.listdir(images_dir) if f.endswith('.png')])
    
    if not image_files:
        print(f"❌ Erro: Nenhuma imagem PNG encontrada em '{images_dir}'!")
        return
    
    print(f"Encontradas {len(image_files)} imagens:")
    for img in image_files:
        print(f"  • {img}")
    print()
    
    # Criar um slide para cada imagem
    for idx, image_file in enumerate(image_files, 1):
        print(f"Adicionando Slide {idx}: {image_file}...")
        
        # Caminho completo da imagem
        image_path = os.path.join(images_dir, image_file)
        
        # Adicionar slide em branco
        blank_slide_layout = prs.slide_layouts[6]  # Layout em branco
        slide = prs.slides.add_slide(blank_slide_layout)
        
        # Calcular dimensões para centralizar a imagem
        # Manter aspecto ratio da imagem original (aproximadamente 1212x688)
        img_width = Inches(9.5)  # Usar quase toda a largura
        img_height = Inches(5.34)  # Manter proporção ~16:9
        
        # Centralizar
        left = (prs.slide_width - img_width) / 2
        top = (prs.slide_height - img_height) / 2
        
        # Adicionar imagem ao slide
        try:
            slide.shapes.add_picture(image_path, left, top, width=img_width, height=img_height)
        except Exception as e:
            print(f"  ⚠️  Erro ao adicionar imagem {image_file}: {e}")
            continue
        
        # Adicionar número do slide (pequeno, no canto)
        add_slide_number(slide, idx, len(image_files))
    
    # Salvar apresentação
    output_file = "JBF_Capital_Pitch_Deck.pptx"
    prs.save(output_file)
    
    print()
    print("=" * 60)
    print(f"✅ Apresentação gerada com sucesso!")
    print(f"📊 Arquivo: {os.path.abspath(output_file)}")
    print(f"📸 Total de slides: {len(image_files)}")
    print("=" * 60)
    print()
    print("Próximos passos:")
    print("1. Abra o arquivo .pptx no PowerPoint, Keynote ou Google Slides")
    print("2. Revise cada slide")
    print("3. Ajuste conforme necessário")
    print()

def add_slide_number(slide, current, total):
    """Adiciona número do slide no canto inferior direito"""
    # Posição no canto inferior direito
    left = Inches(9)
    top = Inches(5.2)
    width = Inches(0.8)
    height = Inches(0.3)
    
    textbox = slide.shapes.add_textbox(left, top, width, height)
    text_frame = textbox.text_frame
    text_frame.text = f"{current}/{total}"
    
    # Formatação do texto
    p = text_frame.paragraphs[0]
    p.font.size = Pt(10)
    p.font.color.rgb = JBFColors.SLATE_GRAY
    p.alignment = 2  # Alinhamento à direita

if __name__ == "__main__":
    create_presentation_from_images()
