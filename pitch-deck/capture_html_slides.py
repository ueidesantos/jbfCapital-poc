#!/usr/bin/env python3
"""
JBF Capital - Capturador de Screenshots dos Slides HTML
Captura screenshots de todos os slides HTML em teste_apresentacao e salva como PNG
"""

import os
import sys
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("❌ Erro: Playwright não está instalado!")
    print("Execute: pip3 install playwright && playwright install chromium")
    sys.exit(1)

def capture_html_slides():
    """
    Captura screenshots de todos os slides HTML em teste_apresentacao
    """
    print("=" * 70)
    print("JBF CAPITAL - CAPTURADOR DE SCREENSHOTS DOS SLIDES HTML")
    print("=" * 70)
    print()
    
    # Diretórios
    html_dir = Path("teste_apresentacao")
    output_dir = Path("slides_from_html")
    
    # Criar diretório de saída se não existir
    output_dir.mkdir(exist_ok=True)
    
    # Verificar se o diretório HTML existe
    if not html_dir.exists():
        print(f"❌ Erro: Diretório '{html_dir}' não encontrado!")
        return False
    
    # Listar todos os arquivos HTML
    html_files = sorted([f for f in html_dir.glob("slide*.html")])
    
    if not html_files:
        print(f"❌ Erro: Nenhum arquivo slide*.html encontrado em '{html_dir}'!")
        return False
    
    print(f"Encontrados {len(html_files)} slides HTML:")
    for html_file in html_files:
        print(f"  • {html_file.name}")
    print()
    
    # Iniciar Playwright
    print("Iniciando navegador...")
    with sync_playwright() as p:
        # Lançar navegador headless
        browser = p.chromium.launch(headless=True)
        
        # Criar contexto com tamanho exato do slide
        context = browser.new_context(
            viewport={'width': 1280, 'height': 720},
            device_scale_factor=2  # Para melhor qualidade
        )
        
        page = context.new_page()
        
        # Capturar cada slide
        for idx, html_file in enumerate(html_files, 1):
            print(f"Capturando Slide {idx}: {html_file.name}...")
            
            # Caminho absoluto do arquivo HTML
            html_path = html_file.resolve().as_uri()
            
            try:
                # Abrir o arquivo HTML
                page.goto(html_path, wait_until='networkidle', timeout=10000)
                
                # Aguardar um pouco para garantir que tudo foi renderizado
                time.sleep(0.5)
                
                # Nome do arquivo de saída
                output_file = output_dir / f"Slide_{idx}.png"
                
                # Capturar screenshot
                page.screenshot(
                    path=str(output_file),
                    full_page=False,
                    type='png'
                )
                
                print(f"  ✅ Salvo: {output_file}")
                
            except Exception as e:
                print(f"  ⚠️  Erro ao capturar {html_file.name}: {e}")
                continue
        
        # Fechar navegador
        browser.close()
    
    print()
    print("=" * 70)
    print(f"✅ Screenshots capturados com sucesso!")
    print(f"📂 Diretório: {output_dir.resolve()}")
    print(f"📸 Total de slides: {len(html_files)}")
    print("=" * 70)
    print()
    
    return True

if __name__ == "__main__":
    # Mudar para o diretório pitch-deck
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    success = capture_html_slides()
    
    if success:
        print("Próximos passos:")
        print("1. Verifique os screenshots em slides_from_html/")
        print("2. Execute: python3 generate_pptx_from_html_slides.py")
        print("3. Apresentação PowerPoint será gerada automaticamente")
        print()
    else:
        sys.exit(1)
